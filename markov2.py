import random
import copy
import scrape
import json
import collections
from tokenizer import tokenizer


def train(data, input_model = collections.defaultdict(dict)):
    model = input_model
    data.append('END')
    for i, element in enumerate(data):
        #print(str(element))
        if i < 2:
            continue
        try:
            model[data[i-2]][data[i-1]].append(element)
        except KeyError:
            model[data[i-2]][data[i-1]] = [element]
    return model

def generate(model, length = 5):
    generated_data = []
    fword = "I"
    sword = "am"
    for i in range(length):
        potential_words = model[fword][sword]

        next_word = potential_words[random.randint(0, len(potential_words)-1)]
        generated_data.append(next_word)

        fword = sword
        sword = next_word
        if next_word == 'END':
            break

    return generated_data


if __name__ == '__main__':
    T = tokenizer.TweetTokenizer()
    tweets = scrape.scrape("realDonaldTrump")

    mc = train([])
    i = 0;
    for t in tweets:
        tokens = T.tokenize(t['full_text'])
        mc = train(tokens, mc)
        print(i)
        i = i+1

    with open('data.txt', 'w') as outfile:
        json.dump(mc, outfile)

    with open('data.txt', 'r') as f:
        mc = json.load(f)

    #print(mc)
    print(generate(mc, 100))
