#!/usr/bin/python3
"""
    Fabric script generates a .tgz archive of
    web_static folder
"""
from fabric.operations import local
from datetime import datetime


def do_pack():
    """
        All archives must be stored in the folder versions
    """
    local("mkdir -p versions")
    status = local("tar -cvzf versions/web_static_{}.tgz web_static"
                   .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
                   capture=True)
    if status.failed:
        return None
    print(status)
    return status
