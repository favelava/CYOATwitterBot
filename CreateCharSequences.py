from random import shuffle


def load_doc(filename):
    file = open(filename, 'r')
    text = file.read()
    file.close()
    return text


# Path to desired recipe list
path = './CocktailRecipes/AllLiquors.txt'

raw_text = load_doc(path)

# Count the number of recipes being trained on
recipes = raw_text.split('_')
print('{} Recipes in corpus'.format(len(recipes)))

# Shuffle recipes twice for added randomness
shuffle(recipes)
shuffle(recipes)
# Rejoin recipes into one long string, separated by end character '_'
recipes = '_'.join(recipes)

# Seperate recipe string into words, removing newline characters
tokens = recipes.split()
# Rejoin all recipes into one long string
raw_text = ' '.join(tokens)

length = 25
sequences = list()

for i in range(length, len(raw_text)):
    seq = raw_text[i-length:i+1]
    sequences.append(seq)

print('Total Sequences: {}'.format(len(sequences)))


def save_doc(lines, filename):
    data = '\n'.join(lines)
    file = open(filename, 'w')
    file.write(data)
    file.close()


out_filename = 'char_sequences.txt'
save_doc(sequences, out_filename)
