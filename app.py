from flask import Flask, request
from logging.handlers import RotatingFileHandler

from flask_redis import FlaskRedis

import logging
import datetime
import os

#Create the App
app = Flask(__name__)

server = os.getenv('REDIS_URL','redis')

#Redis Connection URL
app.config['REDIS_URL'] = "redis://{}:6379/0".format(server)

#Bind Redis Connection to app
redis_store = FlaskRedis(app)

#Create logs
handler = RotatingFileHandler('/tmp/foo.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
app.logger.addHandler(handler)

#Send Values to Redis.
redis_store.set('Start Time', datetime.datetime.now())

@app.route("/")
def hello():
    app.logger.error(('The referrer was {}'.format(request.referrer)))
    return "Hello World! Cap 3 - Exercício 2"
