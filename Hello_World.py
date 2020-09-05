import os
import socket
from flask import Flask

app = Flask(__name__)

hostname = socket.gethostname()
host = socket.gethostbyname(hostname)

@app.route("/")
def index():
    
    return "Hello World from"

app.run(host=host, port=8080)

