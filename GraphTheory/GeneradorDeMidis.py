# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 22:26:43 2023

@author: fenix
"""

import numpy as np
from music21 import stream, note, tempo, meter
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.utils import to_categorical

# Función para preparar los datos de entrada para la red neuronal
def prepare_sequences(notes, n_vocab):
    sequence_length = 100
    pitchnames = sorted(set(item for item in notes))
    note_to_int = dict((note, number) for number, note in enumerate(pitchnames))

    network_input = []
    network_output = []

    for i in range(0, len(notes) - sequence_length, 1):
        sequence_in = notes[i:i + sequence_length]
        sequence_out = notes[i + sequence_length]
        network_input.append([note_to_int[char] for char in sequence_in])
        network_output.append(note_to_int[sequence_out])

    n_patterns = len(network_input)

    network_input = np.reshape(network_input, (n_patterns, sequence_length, 1))
    network_input = network_input / float(n_vocab)

    network_output = to_categorical(network_output)

    return network_input, network_output

# Función para generar música
def generate_music(model, network_input, pitchnames, n_vocab):
    start = np.random.randint(0, len(network_input)-1)

    int_to_note = dict((number, note) for number, note in enumerate(pitchnames))

    pattern = network_input[start]
    prediction_output = []

    for note_index in range(500):  # Puedes ajustar el número de notas generadas
        prediction_input = np.reshape(pattern, (1, len(pattern), 1))
        prediction_input = prediction_input / float(n_vocab)

        prediction = model.predict(prediction_input, verbose=0)

        index = np.argmax(prediction)
        result = int_to_note[index]
        prediction_output.append(result)

        pattern = np.append(pattern, index)
        pattern = pattern[1:len(pattern)]

    return prediction_output

# Cargar y procesar datos de música MIDI (puedes proporcionar tus propios datos)
# Aquí se usa un archivo de ejemplo, puedes reemplazarlo con tu propia música.
file_path = 'path/to/your/midi/file.mid'
midi_stream = stream.Score().read(file_path)

notes = []

for element in midi_stream.flat.notes:
    if isinstance(element, note.Note):
        notes.append(str(element.pitch))
    elif isinstance(element, chord.Chord):
        notes.append('.'.join(str(n) for n in element.pitches))

# Crear la entrada y salida de la red neuronal
n_vocab = len(set(notes))
network_input, network_output = prepare_sequences(notes, n_vocab)

# Crear el modelo LSTM
model = Sequential()
model.add(LSTM(
    256,
    input_shape=(network_input.shape[1], network_input.shape[2]),
    return_sequences=True
))
model.add(Dropout(0.3))
model.add(LSTM(512, return_sequences=True))
model.add(LSTM(256))
model.add(Dense(256))
model.add(Dropout(0.3))
model.add(Dense(n_vocab, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam')

# Entrenar el modelo (esto puede llevar mucho tiempo dependiendo de tus datos y hardware)
model.fit(network_input, network_output, epochs=50, batch_size=64)

# Generar música utilizando el modelo
generated_music = generate_music(model, network_input, pitchnames, n_vocab)

# Crear una partitura con la música generada
generated_score = stream.Score()
generated_part = stream.Part()

for element in generated_music:
    if '.' in element:
        notes_in_chord = element.split('.')
        chord_notes = [note.Note(int(note_str)) for note_str in notes_in_chord]
        new_chord = chord.Chord(chord_notes)
        generated_part.append(new_chord)
    else:
        new_note = note.Note(int(element))
        generated_part.append(new_note)

generated_score.append(generated_part)

# Guardar la partitura generada en un archivo MIDI
generated_score.write('midi', fp='generated_music.mid')