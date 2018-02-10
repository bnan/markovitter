import random
import copy


def train(data, input_model = {'START':[], 'END':[]}):
    model = copy.deepcopy(input_model)
    for i, element in enumerate(data):
        if i == len(data)-1:
            model['END'].append(element)
        else:
            if i == 1:
                model['START'].append(element)
            if element in model:
                model[element].append(data[i+1])
            else:
                model[element] = [data[i+1]]

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

