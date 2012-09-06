# -*- encoding: utf-8 -*-
"""
    Arxer & Vagrant deployment scripts.
    May the fab-force be with you.
"""
from __future__ import with_statement

##from fabric.api import run, sudo, env, local, cd, prefix, settings, confirm
from fabric.api import *
from termcolor import cprint
from contextlib import contextmanager as _contextmanager
import os, sys

DIR = os.path.abspath(os.path.dirname(__file__))
TMP = os.path.abspath('/tmp')

local_settings = {
    'project': 'heelys', ## change this to your project name
    'url': 'git@amygdala.servebeer.com:heelys.git', ## change this to your project github url
    ##'url': 'git@amygdala.local:arxer.get', ## change this to your project github url
    'tmp': TMP,
    'dir': DIR,
}

## set these to your desire
env.hosts = ['cortex.local']
env.user = 'faris'
env.keyfile = ['$HOME/.ssh/id_rsa']
env.directory = DIR
env.activate = 'source %s/bin/activate' % DIR

@_contextmanager
def virtualenv():
    with cd(env.directory):
        with prefix(env.activate):
            yield

# internal scripts
def fetch():
    '''
        grab the latest master branch from dev or github
        depends on url
    '''
    with settings(warn_only=True):
        run('mkdir src')
        with cd('src'):
            result = run('git clone %s' % local_settings['url'])
    if result.failed and not \
      (prompt("Failed to download source. Continue anyway? [Y/[N]]") == 'Y'):
        abort("Aborting at user request")
    else:
        cprint(result, 'red', 'on_green')

# packaging
def freeze():
    '''
    pip freeze all requirements into a local file
    '''
    with virtualenv():
        run('pip freeze --local > requirements.txt')

def pack():
    '''
    pack the entire project into a tar file
    '''
    local('tar czf %s/%s.tgz .' % (TMP, local_settings['project']))

# depackaging
def clean_virtualenv():
    '''
    update pip and virtualenv
    install reqs based on requirements files
    '''
    with virtualenv():
        run('pip install -U pip')
        run('pip install -U virtualenv')
        with cd("%s/.." % DIR):
            run('virtualenv %s' % local_settings['project'])

def get_reqs():
    '''
        get the required packages for nefarious installation
    '''
    run('pip install -r %s/requirements/project.txt' % local_settings['project'])
    run('pip install -r requirements.txt')

# deployment
# Vagrant
def get_box():
    '''
        get a box for a vagrant to move into
    '''
    box_url = "http://files.vagrantup.com/lucid32.box"
    boxname = "%sbox" % local_settings['project']
    run('/var/lib/gems/1.8/bin/vagrant box add %s %s' % (boxname, box_url))

def init_box():
    '''
        initialize the box
    '''
    boxname = "%sbox" % local_settings['project']
    run("/var/lib/gems/1.8/bin/vagrant init %s" % boxname)

def up_box():
    '''
        START ‘ER UP!
    '''
    run("/var/lib/gems/1.8/bin/vagrant up")

def movein():
    '''
        deploy a box
    '''
    get_box()
    init_box()
    up_box()

# install nginx

# install memcached

# install postgresql?

# vcs

# sanity check: check and see if the site runs after deployment

# testing
def test():
    '''
    test verbena and rose, the modified apps
    '''
    apps = [
        'verbena',
        'rose',
    ]
    with settings(warn_only=True):
        with virtualenv():
            with cd("%s/arxer" % DIR):
                for app in apps:
                    result = run('./manage.py test %s' % app)
    if result.failed and not \
    (prompt("Tests failed. Continue anyway? [Y/[N]]") == "Y"):
        abort("Aborting at request of user")
    else:
        cprint(result, 'red', 'on_green')

def testall():
    '''
    test all included django apps
    '''
    with virtualenv():
        with cd("%s/arxer" % DIR):
            run('./manage.py test')

# resetall → nuke the server
def resetall():
    '''
    nukes the local sqlite database and reinstalls sync, fixtures, and
    migrations
    '''
    fixtures = [
        "flatpages",
        "sites",
        "chunks",
        "photologue",
    ]
    with cd("%s/arxer" % DIR):
        run("rm dev.db")
    with virtualenv():
        with cd("%s/arxer" % DIR):
            run('./manage.py syncdb')
            run('./manage.py migrate')
            for fix in fixtures:
                run('./manage.py loaddata apps/verbena/fixtures/%s.json' % fix)

def prepare_deploy():
    test()
    pack()

def deploy():
    '''
    the main deployment function
    '''
    pass

# main scripts
def dev():
    '''
    main DEV script for development environment.
    deploys all dev settings and starts a dev server
    '''
    with virtualenv():
        run('pip freeze --local')

def prod():
    '''
    main production script for production environment
    deploys production settings including:
        - caching
        - asset-smooshing
        - postgresql db
        - gunicorn
        - nginx:
            - static server
            - upstream server (reverse proxy)
    '''
    pass


