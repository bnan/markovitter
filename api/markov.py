import random
import copy
import scrape
import json
import collections
from tokenizer import tokenizer


def train(input_text):
    T = tokenizer.TweetTokenizer()
    mc = collections.defaultdict(dict)
    mr = collections.defaultdict(dict)
    for i in input_text:
        tokens = T.tokenize(i)
        tokens.insert(0,'START')
        tokens.append('END')
        mc = add_to_model(tokens, mc)
        mr = add_to_reverse_model(tokens, mr)
    return mc, mr

def add_to_model(data, model):
    for i, element in enumerate(data):
        if i < 2:
            continue
        try:
            model[data[i-2]][data[i-1]].append(element)
        except KeyError:
            model[data[i-2]][data[i-1]] = [element]
    return model

def add_to_reverse_model(data, rmodel):
    for i, element in enumerate(data):
        if i > len(data) - 2:
            break
        try:
            rmodel[element][data[i-1]].append(data[i-2])
        except KeyError:
            rmodel[element][data[i-1]] = [data[i-2]]
    return rmodel


def generate_with(model, rmodel, word, length = 10):
    generated_data = [word]
    i = 0
    next_word = ''
    # generate in front
    while next_word != 'START':
        if i==0:
            fword = word
            sword = list(rmodel[word].keys())[random.randint(0, len(list(rmodel[word].keys()))-1)]
            generated_data.insert(0,sword)

        potential_words = rmodel[fword][sword]

        if i > length/2 and 'START' in potential_words:
            next_word = 'START'
        else:
            next_word = potential_words[random.randint(0, len(potential_words)-1)]

        generated_data.insert(0,next_word)

        fword = sword
        sword = next_word

        i = i+1

    # generate end
    i = 0
    while next_word != 'END':
        if i==0:
            fword = word
            sword = list(model[word].keys())[random.randint(0, len(list(model[word].keys()))-1)]
            generated_data.append(sword)

        potential_words = model[fword][sword]

        if i > length/2 and 'END' in potential_words:
            next_word = 'END'
        else:
            next_word = potential_words[random.randint(0, len(potential_words)-1)]

        generated_data.append(next_word)

        fword = sword
        sword = next_word

        i = i+1

    return generated_data[1:-1]


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

