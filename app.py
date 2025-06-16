from flask import Flask, render_template
import requests
import random

app = Flask(__name__)

# Function to get fun fact from API
def get_random_fun_fact():
    try:
        response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
        return response.json()["text"]
    except:
        return "Did you know that this app is trying its best to bring you amazing facts?"

# Function to get trending fact (simulated since Reddit API requires auth)
def get_trending_fact():
    trending_facts = [
        "TIL that honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
        "TIL that octopuses have three hearts and blue blood, and two of their hearts stop beating when they swim.",
        "TIL that bananas are berries, but strawberries aren't. Botanically speaking, berries must have seeds inside their flesh.",
        "TIL that a group of flamingos is called a 'flamboyance' and they can only eat with their heads upside down.",
        "TIL that wombat poop is cube-shaped, making them the only known animal to produce square feces.",
        "TIL that sharks have been around longer than trees. Sharks evolved around 400 million years ago, while trees appeared around 350 million years ago.",
        "TIL that there are more possible games of chess than there are atoms in the observable universe.",
        "TIL that a single cloud can weigh more than a million pounds, but it floats because it's less dense than the air around it."
    ]
    return random.choice(trending_facts)

@app.route('/')
def index():
    fact = get_random_fun_fact()
    trending_fact = get_trending_fact()
    return render_template("index.html", fact=fact, trending_fact=trending_fact)

if __name__ == "__main__":
    app.run(debug=True)
