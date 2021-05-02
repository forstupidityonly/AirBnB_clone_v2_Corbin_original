#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""
from fabric.api import run, put, env
import os

env.user = 'ubuntu'
env.hosts = ['104.196.51.56', '3.80.126.68']


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if not os.path.exists(archive_path):
        return False
    A_name = archive_path.split("/")[-1]
    # a_name is <web_static_20170314233357.tgz>


