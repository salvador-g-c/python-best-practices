from flask import Flask
import random

app = Flask(__name__)

quotes = [
    "Code is like humor. When you have to explain it, it’s a bad thing.",
    "Fix the cause, not the symptom.",
    "Optimism is an occupational hazard of programming.",
    "Example"
]

@app.route('/')
def hello():
    return random.choice(quotes)

if __name__ == '__main__':
    app.run(debug=True)
