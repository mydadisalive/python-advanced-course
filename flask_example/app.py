from flask import Flask, render_template
import random

app = Flask(__name__)

# List of famous quotes
quotes = [
    "The only way to do great work is to love what you do. – Steve Jobs",
    "In the end, we will remember not the words of our enemies, but the silence of our friends. – Martin Luther King Jr.",
    "It does not matter how slowly you go as long as you do not stop. – Confucius",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. – Albert Schweitzer",
    "The only limit to our realization of tomorrow will be our doubts of today. – Franklin D. Roosevelt"
]

@app.route('/')
def random_quote():
    # Pick a random quote from the list
    random_index = random.randint(0, len(quotes) - 1)
    random_quote = quotes[random_index]
    return render_template('quote.html', quote=random_quote)

if __name__ == '__main__':
    app.run(debug=True)
