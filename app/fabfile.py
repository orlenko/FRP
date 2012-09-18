# -*- encoding: utf-8 -*-
'''Deployment
'''
import os
import time
from fabric.api import local


# Project-specific settings
PROJECT_NAME = ''
BRANCH = 'master'


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

#
# Main methods
#

def deploy_staging():
    local('git push')
    release_name = Deploy.upload_new_release()