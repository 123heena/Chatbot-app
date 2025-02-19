import nltk
import random
import string  # Helps with text processing
from nltk.chat.util import Chat, reflections
from nltk.tokenize import word_tokenize

nltk.download("punkt")  # Download tokenizer

# Define chatbot responses using (Pattern, Response) pairs
faq_pairs = [
    (r"hi|hello|hey", ["Hello! How can I help you?", "Hi there! What do you need help with?"]),
    (r"what is your name?", ["I am a chatbot created to assist you."]),
    (r"how are you?", ["I'm just a bot, but I'm doing great! How can I assist you?"]),
    (r"what is AI?", ["Artificial Intelligence (AI) is the simulation of human intelligence in machines."]),
    (r"what is machine learning?", ["Machine Learning is a subset of AI that enables computers to learn from data."]),
    (r"what is NLP?", ["Natural Language Processing (NLP) is a field of AI that helps machines understand human language."]),
    (r"bye|goodbye", ["Goodbye! Have a great day!", "Bye! Take care."]),
]

# Create chatbot model
chatbot = Chat(faq_pairs, reflections)

# Function to start the chatbot
def chatbot_response(user_input):
    return chatbot.respond(user_input.lower())  # Convert to lowercase for better matching

# Main loop to interact with the chatbot
print("Chatbot: Hello! Type 'bye' to exit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot: Goodbye! Have a great day!")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response if response else 'Sorry, I did not understand that.'}")
