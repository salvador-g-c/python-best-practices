from flask import Flask
import random
import logging  # Added import

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

quotes = [
    {"text": "Code is like humor. When you have to explain it, it’s bad.", "author": "Cory House"},
    {"text": "Fix the cause, not the symptom. A thing to do.", "author": "Steve Maguire"},
    {"text": "Optimism is an occupational hazard of programming. A test.", "author": "Kent Beck"},
    {"text": "Simplicity is the soul of efficiency.", "author": "Austin Freeman"}
]

@app.route('/')
def hello():
    quote = random.choice(quotes)
    return f"{quote['text']} - {quote['author']}"

if __name__ == '__main__':
    logger.info("Starting the Flask app...")  # Added logging
    app.run(debug=True)
