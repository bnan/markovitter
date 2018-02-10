import random
import copy


def train(data):
    model = {}
    for line in data:
        line = line.lower().split()
        for i, word in enumerate(line):
            if i == len(line)-1:
                model['END'] = model.get('END', []) + [word]
            else:
                if i == 0:
                    model['START'] = model.get('START', []) + [word]
                model[word] = model.get(word, []) + [line[i+1]]
    return model

def generate(model, length = 5):
    generated_data = []
    for i in range(length):
        if len(generated_data) == 0:
            potential_words = model['START']
        else:
            potential_words = model[generated_data[-1]]

        next_word = potential_words[random.randint(0, len(potential_words)-1)]
        generated_data.append(next_word)

        if next_word in model['END']:
            break

    return generated_data

