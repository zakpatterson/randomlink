from flask import Flask, redirect
import random
app = Flask(__name__)

links = [
    '//bing.com',
    '//google.com',
    '//yahoo.com',
    '//cnn.com'
]


@app.route('/')
def random_link():
    return redirect(random.choice(links))
