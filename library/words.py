import json
import random as rnd
import requests

word_json_url = "https://randomwordgenerator.com/json/words.json"
word_json_local = "assets/words.json"


def getAllWords():
    #s = requests.get(word_json_url).json()
    s = json.loads(open(word_json_local, mode='r').read())
    tuples = s['data']
    return [t['word'] for t in tuples]

def getWords(n=10):
    words = getAllWords()
    return rnd.sample(words, n)
