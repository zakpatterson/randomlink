from flask import Flask, redirect
import random
app = Flask(__name__)

links = [
    '//www.gsdigitalcookie.com/cookie/landing/3/d4bb81a4-2c2b-40c1-a6a1-afdd8e5af9fc',
    '//www.gsdigitalcookie.com/cookie/landing/3/ad7357b0-ca9a-4668-ab99-2386e5389e5b',
    '//www.gsdigitalcookie.com/cookie/landing/0/e027908f-0c06-4cc7-a3d3-6ce2b44684b5'
]


@app.route('/')
def random_link():
    return redirect(random.choice(links))
