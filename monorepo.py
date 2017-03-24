import os, shutil
from subprocess import call

import click

@click.command()
@click.option('--current', envvar='REPO_CURRENT', default='current',
              help='Git clones of current repos')
@click.option('--destination', envvar='REPO_DESTINATION', default='monofied',
              help='Destination of the created monorepo')
def cli(current, destination):
    """
    Create a monorepo from multiple individual repos.
    """
    click.echo('''
###################################################
### Welcome to the wonderful world of monorepos ###
###################################################
    ''')

    baseWorkingDir = os.getcwd()

    recreate_destination(current)
    recreate_destination(destination)

    click.secho('Working on the following repos:', fg='green')

    repos = []

    f = open(baseWorkingDir + '/endpoints.txt')
    for remote in f.readlines():
        endpoint = remote.strip()

        cloned_at = endpoint.split('/')[-1].replace('.git', '')
        repos.append(cloned_at)
        click.secho(cloned_at, fg='red')
        print(repos)

        os.chdir('{0}/{1}'.format(baseWorkingDir, current))
        clone_to_folder(os.getcwd(), endpoint)
        os.chdir('{0}/{1}/{2}'.format(baseWorkingDir, current, cloned_at))

        os.mkdir(cloned_at)

        for subfolder in os.listdir('{0}/{1}/{2}'.format(baseWorkingDir, current, cloned_at)):
            if subfolder == cloned_at or subfolder in repos:
                continue
            click.echo(subfolder)
            execute('git mv {0} {1}/'.format(subfolder, cloned_at))

        execute('git add .')
        execute('git commit -m "{0}"'.format(cloned_at))

        # execute('rm -rf {0}/{1}/{2}'.format(baseWorkingDir, current, cloned_at))

    change_dir(baseWorkingDir, destination)
    execute('git init')

    for subfolder in os.listdir('{0}/{1}'.format(baseWorkingDir, current)):
        click.secho(subfolder, fg='red')
        execute('git remote add subrepo ../{0}/{1}'.format(current, subfolder))
        execute('git fetch subrepo master')
        execute('git merge --allow-unrelated-histories subrepo/master')
        execute('git remote rm subrepo')
        execute('git add .')
        execute('git commit -m "{0}"'.format(subfolder))

def recreate_destination(destination):
    click.echo('Recreating destination folder ' + destination)

    shutil.rmtree(destination, True)
    os.mkdir(destination)

def clone_to_folder(destination, endpoint):
    """
    Clone `endpoint` in the indicated `destination` folder
    """
    click.echo('... cloning ' + endpoint + ' to ' + destination)
    execute('git clone -q ' + endpoint)

def execute(command):
    call(command.split())

def change_dir(path, dir=None):
    if dir is not None:
        path = path + '/' + dir
    os.chdir(path)
