import random
import copy
import scrape
import json
import collections
from tokenizer import tokenizer


def train(input_text):
    T = tokenizer.TweetTokenizer()
    mc = collections.defaultdict(dict)
    for i in input_text:
        tokens = T.tokenize(i)
        mc = add_to_model(tokens, mc)
    return mc

def add_to_model(data, model):
    data.insert(0,"START")
    data.append('END')
    for i, element in enumerate(data):
        if i < 2:
            continue
        try:
            model[data[i-2]][data[i-1]].append(element)
        except KeyError:
            model[data[i-2]][data[i-1]] = [element]
    return model

def generate(model, length = 10):
    generated_data = []
    i = 0
    next_word = ''
    while next_word != 'END':
        if i==0:
            fword = "START"
            sword = list(model["START"].keys())[random.randint(0, len(list(model["START"].keys()))-1)]
            generated_data.append(sword)

        potential_words = model[fword][sword]

        if i > length and 'END' in potential_words:
            next_word = 'END'
        else:
            next_word = potential_words[random.randint(0, len(potential_words)-1)]

        generated_data.append(next_word)

        fword = sword
        sword = next_word

        i = i+1

    return generated_data[:-1]

