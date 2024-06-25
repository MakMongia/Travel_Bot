from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Function to initialize and train the chatbot
def initialize_chatbot():
    chatbot = ChatBot(name="TravelBot")
    trainer = ListTrainer(chatbot)
    return chatbot

if __name__ == "__main__":
    chatbot = initialize_chatbot()

    # Test the chatbot in a loop
    while True:
        user_input = input("You: ")
        response = chatbot.get_response(user_input)
        print("TravelBot:", response)
