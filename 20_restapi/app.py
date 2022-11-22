'''
TNPG: Racing Leopards Aggressively Addicted :: Ameer Alnasser, Ryan Lee
SoftDev
k20--REST
2022-11-21
time spent: 1.0 hrs
'''

import requests
from flask import Flask, render_template

app = Flask(__name__)

with open('key_nasa.txt') as f:
    key = f.read()

url = 'https://api.nasa.gov/planetary/apod'

req = requests.get(url, params={'api_key': key})

dictionary = req.json()

#print(dictionary)

img = dictionary['hdurl']

expl = dictionary['explanation']

#print(expl)

@app.route("/")
def index():
    return render_template('main.html', img=img, expl=expl)
    
    
if __name__ == "__main__":
    app.debug = True 
    app.run()