#!/usr/bin/python3
from __future__ import absolute_import
import os

activate_this = '/var/www/vhosts/raydlee.org.uk/flask-twt.raydlee.org.uk/env-flask/bin/activate_this.py'
if os.path.exists(activate_this):
    with open(activate_this) as file_:
        exec(file_.read(), dict(__file__=activate_this))

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/vhosts/raydlee.org.uk/flask-twt.raydlee.org.uk/")
sys.path.insert(0, '/var/www/vhosts/raydlee.org.uk/flask-twt.raydlee.org.uk/env-flask/bin/python3.8')

#def application(environ, start_response):
#    status = '200 OK'
#    output = 'Hello World!'
#	output += str(sys.version)
#    response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(output)))]
#    start_response(status, response_headers)
#    return [output]
from website import flask_web_app as application
#application = website.create_app()
# app.secret_key = 'random text to be secured later'

#if __name__ == '__main__':
#    app.run()
