import os
import json
from flask import Flask, request
from word_dictionary import WordDictionary
from utils import Utils

DICTIONARY_FILE = 'word_dictionary.json'


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'Welcome'

@app.route('/get/<word>', methods=['GET'])
def get(word):
    return "true" if word_dictionary.has_word(word) else "false"


@app.route('/upload', methods=['POST'])
def getfile():
    file = request.files['file']
    
    words = Utils.words_from_file(file)
    word_dictionary.enhance(words)

    return "file uploaded to the dictionary successfully."


if __name__ == '__main__':
    global word_dictionary 
    word_dictionary = WordDictionary()
    app.run(host = '0.0.0.0')