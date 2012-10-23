#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
This module is a launcher for GeoBases webservices.
'''

from DaemonModule import Daemon

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

import sys
import os.path as op


class WebSrvDaemon(Daemon):
    '''
    This class inherits the Daemon property
    and therefore support the start/stop/restart
    methods of daemons.
    '''

    def run(self):

        from GeoBases.Webservice.FlaskAppBuilder import app

        http_server = HTTPServer(WSGIContainer(app))
        http_server.listen(14003)
        IOLoop.instance().start()


def main():
    '''Main launcher.'''

    pid_path = op.realpath(op.join(op.dirname(__file__), 'daemon-geob.pid'))

    daemon = WebSrvDaemon(pid_path)

    if len(sys.argv) != 2:
        print "Usage: %s {start|stop|restart|status|foreground}" % sys.argv[0]
        sys.exit(2)

    if 'start' == sys.argv[1]:
        daemon.start()

    elif 'stop' == sys.argv[1]:
        daemon.stop()

    elif 'restart' == sys.argv[1]:
        daemon.restart()

    elif 'status' == sys.argv[1]:
        daemon.status()

    elif 'foreground' == sys.argv[1]:
        daemon.debug()

    else:
        print "Unknown command \"%s\"" % sys.argv[1]
        print "Usage: %s {start|stop|restart|status}" % sys.argv[0]
        sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":

    main()

