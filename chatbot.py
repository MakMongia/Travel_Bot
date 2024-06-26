import requests
from flask import Flask, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import yaml
import os
import sys
import threading
import tkinter as tk
from tkinter import scrolledtext

print(sys.path)

app = Flask(__name__)
chatbot = ChatBot(name="TravelBot")


# Function to get weather data from OpenWeatherMap API
def get_weather(city):
    api_key = '7dc2b9998128f4cd1423e9e9fbb70af2'
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    print(f"Requesting weather for city: {city}")
    print(f"API Response Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"API Response Data: {data}")
        weather = {
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "city": data["name"]
        }
        return weather
    else:
        print(f"Failed to get weather data: {response.text}")
        return None


# Function to load data from YAML file
def load_data_from_yaml(data_folder, file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(current_dir, data_folder, file_name)

    with open(full_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)

    return data


# Function to train the chatbot with NLU data
def train_chatbot_with_nlu_data(nlu_data):
    trainer = ListTrainer(chatbot)

    for intent_data in nlu_data['nlu']:
        if 'examples' in intent_data:
            examples = intent_data['examples']
            trainer.train(examples)


# Function to train the chatbot with stories
def train_chatbot_with_stories(stories_data):
    trainer = ListTrainer(chatbot)

    for story in stories_data['stories']:
        steps = story.get('steps', [])  # Get steps; default to empty list if 'steps' key doesn't exist
        for step in steps:
            intent = step.get('intent')  # Get 'intent' key from step; returns None if key doesn't exist
            if intent:
                trainer.train([intent])


# Load NLU data from YAML file
def load_and_train_nlu_data():
    nlu_data = load_data_from_yaml('data', 'nlu.yml')
    train_chatbot_with_nlu_data(nlu_data)


# Load stories from YAML file
def load_and_train_stories():
    stories_data = load_data_from_yaml('data', 'stories.yml')
    train_chatbot_with_stories(stories_data)


# Train the chatbot with loaded data
load_and_train_nlu_data()
load_and_train_stories()


# Route for root URL
@app.route('/', methods=['GET'])
def index():
    return "Welcome to the TravelBot API. Use the /chat endpoint for chat interactions."


# Route for chatbot interaction
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json['message']

    # Extract city name from user input if the input is a weather query
    if 'weather' in user_input.lower():
        city = user_input.split("in")[-1].strip().replace("?", "")  # Extract city name
        print(f"Extracted city: {city}")
        weather = get_weather(city)
        if weather:
            response = f"The weather in {weather['city']} is {weather['temperature']}°C with {weather['description']}."
        else:
            response = "Sorry, I couldn't retrieve the weather information. Please try again."
    else:
        response = chatbot.get_response(user_input).text

    return jsonify({"response": response})


def run_flask_app():
    app.run(debug=True, use_reloader=False)


# Function to start the Flask app in a separate thread
flask_thread = threading.Thread(target=run_flask_app)
flask_thread.start()


# Create a basic Tkinter GUI for the chat interface
def send_message():
    user_message = entry.get()
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "You: " + user_message + "\n")
    chat_window.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

    response = requests.post("http://127.0.0.1:5000/chat", json={"message": user_message}).json()
    bot_message = response['response']

    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, "Bot: " + bot_message + "\n")
    chat_window.config(state=tk.DISABLED)
    chat_window.yview(tk.END)


root = tk.Tk()
root.title("TravelBot Chat")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(root, width=80)
entry.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.X, expand=True)
entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT, padx=10, pady=10)

root.mainloop()

if __name__ == "__main__":
    run_flask_app()
