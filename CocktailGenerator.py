from pickle import load
from keras.models import load_model
from keras.utils import to_categorical
from keras.preprocessing.sequence import pad_sequences

model_file = './SavedModels/model04092020-133048.h5'
model = load_model(model_file)

mapping_file = './SavedMappings/mapping04092020-133048.pkl'
mapping = load(open(mapping_file, 'rb'))


def generate_seq(model, mapping, seq_length, seed_text, n_chars):
    in_text = seed_text
    len(in_text)
    # Generate a set number of characters
    for _ in range(n_chars):
        encoded = [mapping[char] for char in in_text]
        encoded = pad_sequences([encoded], maxlen=seq_length, truncating='pre')
        encoded = to_categorical(encoded, num_classes=len(mapping))
        encoded.shape

        # Predict character
        yhat = model.predict_classes(encoded, verbose=0)
        out_char = ''
        for char, index in mapping.items():
            if index == yhat:
                out_char = char
                break
        in_text += out_char

        # Exit early if end character is predicted
        if out_char == '_':
            return in_text

    return in_text


print(generate_seq(model, mapping, 12, 'The Test ', 300))
