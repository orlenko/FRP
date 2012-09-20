# -*- encoding: utf-8 -*-
'''Deployment
'''
import os
import time
from fabric.api import local
from fabric.operations import run, sudo
from fabric.contrib.files import exists
from fabric.state import env
from fabric.context_managers import cd


# Project-specific settings
PROJECT_NAME = 'frp'
BRANCH = 'master'
DOMAIN = 'frp-staging.bjola.ca'
#DOMAIN_NAME = 'frpbc.ca'
GIT_CLONE_PATH = 'orlenko/FRP.git'
PRODUCTION_USERNAME = 'web'
PRODUCTION_HOST = DOMAIN # Change this to an IP if your DNS isn't resolving yet
ADMIN_EMAIL = 'frp@bjola.ca'

# General settings
GIT_CLONE_USERNAME = 'git'
PROJECT_DIR = '/home/web/%s' % PROJECT_NAME
GIT_CLONE_HOST = 'github.com'
GIT_CLONE_PSEUDOHOST = PROJECT_NAME # Used to specify site-specific behavior for SSH if multiple projects are hosted on e.g. github.com
DJANGO_PORT = 81
BRANCH = 'master'
SERVER_GROUP = 'web'
ROLES = ['nginx', 'django', 'database', 'smtp']
VIRTUALENV = '/home/web/workspace/projects/bcfrp'
DB_PASS = 'family98'
PG_VERSION = (8, 4)
PYTHON_VERSION = (2,6)

class Deploy(object):

    run_time = time.time()

    @classmethod
    def get_current_commit(cls):
        return local('git rev-parse --verify %s' % BRANCH,
                     capture=True).strip()

    @classmethod
    def get_time_str(cls):
        return time.strftime('%Y-%m-%d-%H-%M-%S',
                             time.localtime(cls.run_time))

    @classmethod
    def get_release_name(cls):
        return Deploy.get_time_str() + '_' + cls.get_current_commit()

    @classmethod
    def switch_symlink(cls, name):
        assert name
        new_target = os.path.join(PROJECT_DIR, 'releases', name)
        symlink_location = os.path.join(PROJECT_DIR, 'current')
        make_symlink_atomically(new_target, symlink_location)

    @staticmethod
    def get_release_dir(name):
        assert name
        return os.path.join(PROJECT_DIR, 'releases', name)

    @staticmethod
    def get_git_repo():
        return GIT_CLONE_USERNAME + '@' + GIT_CLONE_PSEUDOHOST + ':' + GIT_CLONE_PATH

    @staticmethod
    def upload_new_release():
        name = Deploy.get_release_name()
        release_dir = Deploy.get_release_dir(name)
        if exists(release_dir):
            assert release_dir.startswith(os.path.join(PROJECT_DIR, 'releases'))
            run('rm -rf %s' % release_dir)
        run('git clone %s %s' % (Deploy.get_git_repo(), release_dir))
        set_up_permissions(release_dir)
        current_commit = Deploy.get_current_commit()
        with cd(release_dir):
            run('git reset --hard %s' % current_commit)
        return name

    @staticmethod
    def prep_release(name):
        """Prepares all the files in the release dir."""
        assert name
        release_dir = Deploy.get_release_dir(name)
        django_dir = os.path.join(release_dir, PROJECT_NAME)
        # If you run a preprocessor, like JS/CSS compilation, do that here, e.g. :
        #run(os.path.join(PROJECT_DIR, 'bin', 'processor') + ' ' + release_dir)
        print 'Setting up Django settings symlinks'
        with cd(django_dir):
            run('ln -nfs %s .' % os.path.join(PROJECT_DIR, 'stagesettings.py'))
            run('ln -nfs %s .' % os.path.join(PROJECT_DIR, 'localsettings.py'))

        print 'Doing Django database updates'
        with cd(django_dir):
            with_ve =  'source ' + os.path.join(VIRTUALENV, 'bin', 'activate') + ' && '
            run(with_ve + 'python manage.py syncdb --noinput')
            run(with_ve + 'python manage.py migrate --noinput')
            run(with_ve + 'python manage.py loaddata initial_data')
            run(with_ve + 'python manage.py collectstatic --noinput')


        print 'Installing crontab'
        crontab_path = os.path.join(release_dir, 'server/crontab')
        # need to use the stdin formulation. For some reason the path in the normal form
        # gets truncated.
        run('crontab - < %s' % crontab_path)

    @staticmethod
    def cleanup_release(name):
        pkg_filename = "%s.tar.gz" % name
        if os.path.exists(pkg_filename):
            local('rm %s' % pkg_filename)


def make_symlink_atomically(new_target, symlink_location, sudo=False):
    # From http://blog.moertel.com/articles/2005/08/22/how-to-change-symlinks-atomically
    runner = sudo if sudo else run
    params = {
            'new_target': new_target,
            'symlink_location': symlink_location,
            'tempname': 'current_tmp',
            }
    cmd = "ln -s %(new_target)s %(tempname)s && mv -Tf %(tempname)s %(symlink_location)s" % params
    runner(cmd)


def set_up_permissions(dirname):
    sudo('chown -R %s:%s %s' % (env.user, SERVER_GROUP, dirname))
    sudo('chmod -R g+w %s' % dirname)


def adduser(username):
    # Idempotent (non-failing) version of adduser
    base_cmd = 'useradd --user-group %s' % username
    sudo(base_cmd + ' || [[ $? == 9 ]]') # 9 is failure code for already exists
    # alt: getent passwd username || useradd, also thanks to \amethyst


#
# Main methods
#


def list_releases():
    with cd(os.path.join(PROJECT_DIR, 'releases')):
        run('''ls -ltc | grep -v total | awk '{print $6 " " $7 " " $8 " " $9}' | head -n 10''')
        #run('ls -l %s | cut -d " " -f "10"' % os.path.join(PROJECT_DIR, CURRENT_RELEASE_DIR))

# Two-step Deploy; use this for HA multi-server setup:
# 1. deploy_prep_new_release
# 2. deploy_activate_release:<release_name>

def deploy_prep_new_release():
    local('git push')
    release_name = Deploy.upload_new_release()
    Deploy.prep_release(release_name)
    print '*'*20
    print "Prepped new release", release_name
    print 'You probably want to deploy_activate_release:%s' % release_name
    print '*'*20

def deploy_activate_release(release_name):
    assert release_name
    Deploy.switch_symlink(release_name)
    restart_after_deploy()
    Deploy.cleanup_release(release_name)

# One-step Deploy; use this for one-server setup or if lazy
# 1. simple_deploy

def deploy():
    release_name = Deploy.upload_new_release()
    Deploy.prep_release(release_name)
    Deploy.switch_symlink(release_name)
    Deploy.cleanup_release(release_name)

def restart_after_deploy():
    restart_django()

def simple_deploy():
    local('git push')
    deploy()
    restart_after_deploy()

#
# Service control
#

def reload_nginx():
    sudo('initctl reload nginx')

def reload_django():
    sudo('apache2ctl graceful')

def reload_database():
    if PG_VERSION < (9, 0):
        sudo('/etc/init.d/postgresql-8.4 reload')
    else:
        sudo('/etc/init.d/postgresql reload')

def restart_nginx():
    sudo('/etc/init.d/nginx restart')

def restart_django():
    sudo('apache2ctl graceful || apache2ctl start')

def restart_database():
    if PG_VERSION < (9, 0):
        sudo('/etc/init.d/postgresql-8.4 restart || /etc/init.d/postgresql-8.4 start')
    else:
        sudo('/etc/init.d/postgresql restart || /etc/init.d/postgresql start')

def restart_smtp():
    sudo('/etc/init.d/postfix restart')
