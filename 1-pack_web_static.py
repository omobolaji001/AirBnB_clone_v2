#!/usr/bin/python3
from fabric.api import *
from datetime import datetime


def do_pack():
    """ generates a tgz archive from the content of web_static/ """
    date_time = datetime.now()
    date_time = date_time.strftime('%Y%m%d%H%M%S')

    try:
        local('mkdir versions')
        local('tar -czvf versions/web_static_{}.tgz web_static/'
              .format(date_time))

        return "versions/web_static_{}.tgz".format(date_time)

    except Exception as e:
        return None
