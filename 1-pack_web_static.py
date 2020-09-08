#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
"""


from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """do_pack function"""
    local("mkdir -p versions")
    file = "versions/web_static_" + dt.now().strftime("%Y%m%d%H%M%S") + ".tgz"
    local("tar -cvzf " + file + " web_static")
    if path.exists(file):
        return file
    else:
        return None
