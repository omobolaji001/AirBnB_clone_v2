#!/usr/bin/python3
from fabric.api import *
from os import path


env.hosts = ['54.160.124.59', '54.160.95.91']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """ Distributes archive to web servers """

    try:
        # check if file path exist
        if not (path.exists(archive_path)):
            return False

        # partiton the file path to obtain the filename with extension
        archive = archive_path.partition('/')[2]
        # obtain the file name without extension
        filename = archive.split('.')[0]

        # uploead the archived file to the web servers
        put(archive_path, '/tmp/')
        # create the target directory
        run("sudo mkdir -p /data/web_static/releases/{}".format(filename))
        # extract the archived file to the target directory
        run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}"
            .format(archive, filename))
        # delete the archive file from the web servers
        run("sudo rm /tmp/{}".format(archive))
        # move the contents into hosts' web_static
        run("sudo mv /data/web_static/releases/{}/web_static/*\
            /data/web_static/releases/{}".format(filename, filename))
        # delete the empty foleder
        run("sudo rm -rf /data/web_static/releases/{}/web_static"
            .format(filename))
        # delete target symbolic link
        run("sudo rm -rf /data/web_static/current")
        # create symbolic link that links to the target directory
        run("sudo ln -s /data/web_static/releases/{} /data/web_static/current"
            .format(filename))

    except Exception as e:
        return False

    # return on success
    return True
