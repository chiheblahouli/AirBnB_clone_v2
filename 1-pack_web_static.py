#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
"""


from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """generate a tgz archive"""
    try:
        if isdir("versions") is False:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        path = os.getcwd() + "/versions"
        local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        return None
