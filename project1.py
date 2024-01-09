#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import nltk
from nltk.tokenize import word_tokenize


# In[3]:


import random
from nltk.tokenize import word_tokenize

class Chatbot:
    def __init__(self):
        self.greetings = [
            "Hello! How can I assist you today?",
            "Hi there! What can I do for you?",
            "Greetings! What brings you here?",
            "Hey! How can I help you?"
        ]
        self.farewells = [
            "Goodbye! If you have more questions, feel free to ask.",
            "See you later! Don't hesitate to return if you need help.",
            "Farewell! Have a great day!",
            "Take care! Feel free to come back anytime."
        ]
        self.humor_responses = [
            "Why did the computer catch a cold? It left its Windows open!",
            "I told my computer I needed a break, and now it won't stop sending me vacation ads.",
            "Why don't programmers like nature? It has too many bugs.",
            "What do computers snack on? Microchips!"
        ]
        self.additional_responses = [
            "I'm here to assist you with any questions you have.",
            "Feel free to ask me anything!",
            "I'm glad you're here! How can I assist you today?",
            "Welcome! How may I be of help?"
        ]

    def greet(self):
        print(random.choice(self.greetings))

    def respond_to_basic_questions(self, question):
        words = word_tokenize(question.lower())
        if any(word in words for word in ["your", "name"]):
            print("I'm just a chatbot designed to assist you. You can call me ChatPro.")
        elif "purpose" in words:
            print("My purpose is to provide information and assistance. How may I help you today?")
        elif "capabilities" in words:
            print("I can answer your questions, provide information, and engage in conversation. Feel free to ask anything.")
        elif any(word in words for word in ["how", "are", "you"]):
            print("Thank you for asking! I'm a computer program, so I don't have feelings, but I'm here to assist you.")
        elif any(word in words for word in ["bye", "goodbye"]):
            print(random.choice(self.farewells))
            return True
        else:
            print("I'm not sure how to respond to that. Can you please rephrase your question?")
        return False


    def respond_to_user_input(self, user_input):
        if any(word in word_tokenize(user_input.lower()) for word in ["hello", "hi", "hey"]):
            self.greet()
        elif "?" in user_input:
            return self.respond_to_basic_questions(user_input)
        elif any(word in word_tokenize(user_input.lower()) for word in ["joke", "funny"]):
            print(random.choice(self.humor_responses))
        elif any(word in word_tokenize(user_input.lower()) for word in ["bye", "goodbye"]):
            print(random.choice(self.farewells))
            return True
        else:
            print(random.choice(self.additional_responses))
        return False

    def farewell(self):
        print(random.choice(self.farewells))

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.greet()

    while True:
        user_response = input("User: ")
        if chatbot.respond_to_user_input(user_response):
            break

    chatbot.farewell()


# In[ ]:




