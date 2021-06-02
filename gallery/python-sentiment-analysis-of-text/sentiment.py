import requests
import json

def is_positive(text) :
    """Use a web service to determine whether the sentiment of text is positive"""
    r = requests.post("http://text-processing.com/api/sentiment/", data={'text': text})
    return r.json()['probability']['pos'] > r.json()['probability']['neg']

positive_sentences = [
    "we love our fans",
    "i love cake",
    "i love you",
    "you are great",
    "he is smart"]

negative_sentences = [
    "we hate our fans",
    "i hate cake",
    "i hate you",
    "you are horrible",
    "he is dumb"]

for sentence in positive_sentences:
    print(sentence, is_positive(sentence))

for sentence in negative_sentences:
    print(sentence, is_positive(sentence))
