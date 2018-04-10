import logging
import sys
from flask import Flask

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)

@app.route('/')
def home():
    app.logger.debug('Hello, World!')
    return 'Hello, World!'
