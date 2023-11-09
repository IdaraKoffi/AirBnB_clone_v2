#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers using the function do_deploy.
"""
from fabric.api import run, put, env
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'  # Update with your actual username
env.key_filename = 'my_ssh_private_key'  # Update with your actual private key file path

def do_deploy(archive_path):
    """
    Distributes an archive to the web servers.

    Args:
        archive_path (str): Path to the archive to be deployed.

    Returns:
        bool: True if all operations have been done correctly, otherwise False.
    """
    if not exists(archive_path):
        return False

    try:
        archive_name = archive_path.split('/')[-1]
        archive_no_ext = archive_name.split('.')[0]

        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/{}'.format(archive_name))

        # Create the release directory
        run('mkdir -p /data/web_static/releases/{}/'.format(archive_no_ext))

        # Uncompress the archive to the release directory
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
            archive_name, archive_no_ext))

        # Remove the archive from the web server
        run('rm /tmp/{}'.format(archive_name))

        # Move contents to the proper location
        run('mv /data/web_static/releases/{}/web_static/* '
            '/data/web_static/releases/{}/'.format(archive_no_ext, archive_no_ext))

        # Remove the unnecessary web_static directory
        run('rm -rf /data/web_static/releases/{}/web_static'.format(archive_no_ext))

        # Remove the current symbolic link
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link
        run('ln -s /data/web_static/releases/{}/ '
            '/data/web_static/current'.format(archive_no_ext))

        print("New version deployed!")
        return True

    except Exception as e:
        return False
