from CreateCharSequences import load_doc
from numpy import array
from pickle import dump
from datetime import datetime
from keras.utils import to_categorical
from keras.utils.vis_utils import plot_model
from keras.models import Sequential
from keras.layers import RepeatVector
from keras.layers import LSTM
from keras.layers import Dense

in_filename = 'char_sequences.txt'
raw_text = load_doc(in_filename)
lines = raw_text.split('\n')

chars = sorted(list(set(raw_text)))
mapping = dict((c, i) for i, c in enumerate(chars))

sequences = list()
for line in lines:
    encoded_seq = [mapping[char] for char in line]
    sequences.append(encoded_seq)

vocab_size = len(mapping)
print('Vocabulary Size: {}'.format(vocab_size))

sequences = array(sequences)
X, y = sequences[:, :-1], sequences[:, -1]

sequences = [to_categorical(x, num_classes=vocab_size) for x in X]
X = array(sequences)
y = to_categorical(y, num_classes=vocab_size)


def define_model(X):
    model = Sequential()

    model.add(LSTM(75, input_shape=(X.shape[1], X.shape[2])))
    model.add(RepeatVector(3))
    model.add(LSTM(75))
    model.add(Dense(vocab_size, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='adam')
    model.summary()
    return model


model = define_model(X)
model.fit(X, y, epochs=100, verbose=2)

time = datetime.now().strftime('%d%m%Y-%H%M%S')

model.save('./SavedModels/model{}.h5'.format(time))
dump(mapping, open('./SavedMappings/mapping{}.pkl'.format(time), 'wb'))
