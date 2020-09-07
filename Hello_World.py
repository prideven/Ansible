import os
from flask import Flask
import socket

app = Flask(__name__)

hostname = socket.gethostname()
hostIP = socket.gethostbyname(hostname)

@app.route("/")
def index():
    h=hostname.split(".")
    ret= "Hello World from %s" %(h[0])
    return ret

app.run(host=hostIP, port=8080)

