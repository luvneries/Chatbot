#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 09:29:04 2017

@author: pankaj
"""

from flask import Flask, render_template, request, jsonify
#from chatterbot import ChatBot
#from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
#app.debug=True
#english_bot = ChatBot("Chatterbot", storage_adapter = "chatterbot.storage.SQLStorageAdapter")

#english_bot.set_trainer(ChatterBotCorpusTrainer)
#english_bot.train("chatterbot.corpus.english")


#languages = [{'name':'Java'}, {'name': 'Python'}]
#def test():
 #   return jsonify({'message': "It works})
 
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/")
def get_bot_response():
    userText = request.args.get('msg')
    print(userText)
#    return str(english_bot.get_response(userText))


if __name__ == "__main__":
    app.run()