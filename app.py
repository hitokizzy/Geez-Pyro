import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("git clone -b main https://github.com/hitokizzy/Geez-Pyro && cd Geez-Pyro && pip3 install -r requirements.txt && python3 -m Geez-Pyro")
