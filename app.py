from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://giphy.com/gifs/uSYQsJQWEv6O4/html5",
    "https://giphy.com/gifs/41hO5LMF4YMz6/html5",
    "https://giphy.com/gifs/kLLvH1EOtCwQ8/html5"
]

@app.route('/')
def index():
    url = random.choice(images)
    return render_template('index.html', url=url)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
