#!/usr/bin/python3

activate_this = '/var/www/vhosts/raydlee.org.uk/flask-twt.raydlee.org.uk/env-flask/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/vhosts/raydlee.org.uk/flask-twt.raydlee.org.uk/")
sys.path.insert(1, '/var/www/vhosts/raydlee.org.uk/flask-twt.raydlee.org.uk/env-flask/bin/python3.8')

def application(environ, start_response):
    status = '200 OK'
    output = 'Hello World!'
#	output += str(sys.version)
    response_headers = [('Content-type', 'text/plain'), ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]
#from website import app as application
#app = create_app()
# app.secret_key = 'random text to be secured later'

#if __name__ == '__main__':
#    app.run()
