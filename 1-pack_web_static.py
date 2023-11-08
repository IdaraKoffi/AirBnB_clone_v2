from fabric.api import local
from datetime import datetime

def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        Archive path if the archive is generated, otherwise None.
    """
    try:
        # Create the "versions" directory if it doesn't exist
        local("mkdir -p versions")

        # Generate archive filename (web_static_<year><month><day><hour><minute><second>.tgz)
        now = datetime.now()
        archive_name = "web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))

        # Compress the web_static folder and save it in the versions directory
        local("tar -cvzf versions/{} web_static".format(archive_name))

        # Return the path to the generated archive
        return "versions/{}".format(archive_name)
    except Exception:
        return None
