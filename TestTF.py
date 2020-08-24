# Setup
import tensorflow as tf

import numpy as np
import os
import time


# Test on tensorflow example for generating Shakesperian text
web_page = 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt'

path_to_file = tf.keras.utils.get_file('shakespeare.txt', web_page)

# Read the data
# Read then decode for py2 compat
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')

# length of text is the number of characters in it
print('Length of text: {} characters'.format(len(text)))

# Take a look at the first 250 characters in text
print(text[:250])

# The unique characters in the file
vocab = sorted(set(text))
print('{} unique characters'.format(len(vocab)))

# Process the text
# Vectorize the text
# Creating a mapping from unique character to indices and back
char2idx = {u: i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)

# Add text to map
text_as_int = np.array([char2idx[c] for c in text])

# Show how characters are mapped to integers
print('{')
for char, _ in zip(char2idx, range(20)):
    print(' {:4s} : {:3d},'.format(repr(char), char2idx[char]))
print(' ...\n}')

# Show how the first 13 characters from the text are mapped to integers
print('{} ---- characters mapped to int ---- > {}'.format(repr(text[:13]),
                                                          text_as_int[:13]))

# The Prediction Task
# The maximum length sentence we want for a single input
seq_length = 100
examples_per_epoch = len(text) // (seq_length + 1)

# Create training examples/targets
char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)

for i in char_dataset.take(5):
    print(idx2char[i.numpy()])

sequences = char_dataset.batch(seq_length+1, drop_remainder=True)

for item in sequences.take(5):
    print(repr(''.join(idx2char[item.numpy()])))


def split_input_target(chunk):
    input_text = chunk[:-1]
    target_text = chunk[1:]
    return input_text, target_text


dataset = sequences.map(split_input_target)

for input_example, target_example in dataset.take(1):
    print('Input data: ', repr(''.join(idx2char[input_example.numpy()])))
    print('Target data: ', repr(''.join(idx2char[target_example.numpy()])))

for i, (input_idx, target_idx) in enumerate(zip(input_example[:5],
                                                target_example[:5])):
    print("Step {:4d}".format(i))
    print(" input: {} ({:s})".format(input_idx, repr(idx2char[input_idx])))
    print(" expected output: {} ({:s})".format(target_idx,
                                               repr(idx2char[target_idx])))

# Create Training Batches
# Batch size
BATCH_SIZE = 64

# Buffer the size to shuffle the Dataset
# (TF data is designed to work with possibly infinte sequences,
# so it doesn't attempt to shuffle the entire sequence in memory.
# Instead, it maintains a buffer in which it shuffles elements)
BUFFER_SIZE = 10000

dataset = dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)

dataset

# Build the Model
# Length of the vocabulary in chars
vocab_size = len(vocab)

# The embedding dimension
embedding_dim = 256

# Number of RNN units
rnn_units = 1024


def build_model(vocab_size, embedding_dim, rnn_units, batch_size):
    model = tf.keras.Sequential([
        tf.keras.layers.Embedding(vocab_size,
                                embedding_dim,
                                batch_input_shape=[batch_size, None]
                                  ),
        tf.keras.layers.GRU(rnn_units,
                            return_sequences=True,
                            stateful=True,
                            recurrent_initializer='glorot_uniform'
                            ),
        tf.keras.layers.Dense(vocab_size)
    ])
    return model


model = build_model(
    vocab_size=len(vocab),
    embedding_dim=embedding_dim,
    rnn_units=rnn_units,
    batch_size=BATCH_SIZE)

# Try the model
for input_example_batch, target_example_batch in dataset.take(1):
    example_batch_predictions = model(input_example_batch)
    print(example_batch_predictions.shape,
          "# (batch_size, sequence_length, vocab_size)")

model.summary()
