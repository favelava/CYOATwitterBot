from pickle import load
from keras.models import load_model
from keras.utils import to_categorical
from keras.preprocessing.sequence import pad_sequences
import numpy as np

# Load model of interest. ModelNotes.txt is in SavedModels for reference
model_file = './SavedModels/model10092020-215724.h5'
model = load_model(model_file)

# Load mapping corresponding to model
mapping_file = './SavedMappings/mapping10092020-215724.pkl'
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
        yhat = np.argmax(model.predict(encoded), axis=-1)
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


print(generate_seq(model, mapping, 25, "River ", 300))
