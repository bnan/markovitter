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
    data.append('END')
    for i, element in enumerate(data):
        if i < 2:
            continue
        try:
            model[data[i-2]][data[i-1]].append(element)
        except KeyError:
            model[data[i-2]][data[i-1]] = [element]
    return model

def generate(model, length = 5, fword = "I", sword = "am"):
    generated_data = []
    generated_data.append(fword)
    generated_data.append(sword)
    for i in range(length):
        potential_words = model[fword][sword]

        next_word = potential_words[random.randint(0, len(potential_words)-1)]
        generated_data.append(next_word)

        fword = sword
        sword = next_word
        if next_word == 'END':
            break

    generated_data.pop(-1)
    return generated_data


if __name__ == '__main__':
    print("Just for tests")
#    i = 0;
#    mc = train([])
#    tweets = scrape.scrape("BarackObama")
#
#    l = []
#    for t in tweets:
#        l.append(t['full_text'])
#        print(i)
#        i = i+1
#
#    mc = train(l)
#
#    with open('data.txt', 'w') as outfile:
#        json.dump(mc, outfile)
#
#    with open('data.txt', 'r') as f:
#        mc = json.load(f)
#
#    ri = random.randint(0, len(tweets)-1)
#    tokens = T.tokenize(tweets[ri]['full_text'])
#
    #with open('donald.json','r') as f:
    #    tweets = f.readline()
    #    print(len(tweets))

    #tweets = json.loads(tweets)
    #for t in tweets:
    #    tokens = T.tokenize(t['text'])
    #    mc = train(tokens, mc)
    #    print(i)
    #    i = i+1


    print(generate(mc, 100, tokens[0], tokens[1]))
