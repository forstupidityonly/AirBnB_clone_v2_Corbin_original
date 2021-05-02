#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""
from fabric.api import local
import datetime


def do_pack():
    """Fabric script that generates a .tgz archive"""
    local("mkdir -p versions")
    time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    the_file = "versions/web_static_{}.tgz".format(time)
    result = local("tar -czvf {} web_static".format(the_file))
    if result.failed:
        return None
    return (the_file)
