#!/usr/bin/python

activate_this = '/var/www/vhosts/raydlee.org.uk/flask-twt.raydlee.org.uk/env-flask/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/vhosts/raydlee.org.uk/flask-twt.raydlee.org.uk/website/")

from website import create_app
app = create_app()
# app.secret_key = 'random text to be secured later'

if __name__ == '__main__':
    app.run()
