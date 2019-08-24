import json

class WordDictionary:

    DICT_FILE = 'data/word_dictionary.json'
    word_dict: dict = {}

    def __init__(self):
        self.load()

    def load(self):
        with open(self.DICT_FILE, 'r') as json_file:
            self.word_dict = json.loads(json_file.read())

    def dump(self):
        with open(self.DICT_FILE, 'w') as json_file:
            json.dump(self.word_dict, json_file, indent=4)

    def enhance(self, words):
        for word in words:
            if not self.has_word(word):
                self.word_dict[word] = "true"

        self.dump()

    def has_word(self, word):
        return word in self.word_dict