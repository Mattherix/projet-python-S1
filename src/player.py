"""
All the functions used to play the notes and partitions
Author: Matthieu ROQUEJOFFRE The Professor who made the subject and don't sign it (for the sound functions)

Project python S1 is a program used to play musical partition and apply effet on it
Copyright (C) 2021  Matthieu ROQUEJOFFRE Titouan DUPUIS

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""
from random import choice

import numpy as np
import simpleaudio as sa

from src.edit import transposition, invertion
from src.markov import markov
from src.utils import decode_partition, NOTE_TO_FREQUENCY

FREQUENCY_TO_COLOR = {
    264: 'white',
    297: 'red',
    330: 'green',
    352: 'cyan',
    396: 'yellow',
    440: 'blue',
    495: 'magenta',
    -1: 'black'
}


def play(partition, markov_notes, markov_reset, canvas, k=None, invert=False, m=False, partition_markov=""):
    """Play a give partion

    :param partition: The partion as a strings ie: "SOLc p Zc"
    :param canvas: The canvas used to draw ie: tk.Canvas(...)
    :param k: The number used in the transposition, by default none ie: 15
    :param invert: Do an inverion on the partition, by default at False
    :param m: Use the markov transformation, by default at False
    :param partition_markov: The partition used for markov ie: "LAn SOLn DOn Zc SIb SOLc p Zc SOLn"
    :return: Nothing, The sound of the partition played in the speaker, Clean the canvas and play the animation on it
    """
    quaver = 0.25
    duration_to_size = {
        (8 * quaver): 15,
        (4 * quaver): 10,
        (2 * quaver): 5,
        (1 * quaver): 2.5,
        (quaver / 2): 1.25,
        (quaver / 4): 0.75,
        (quaver / 8): 0.375,
        (quaver / 16): 0.1875
    }

    if m:
        partition = markov(partition_markov, partition, markov_notes, markov_reset)
    partition = decode_partition(partition, NOTE_TO_FREQUENCY, quaver)
    if k:
        partition = transposition(partition, k)
    if invert:
        partition = invertion(partition)

    canvas.delete("all")

    i = 0
    j = 0
    last_frequency = 0
    for frequency, duration in partition:
        if frequency != -1 and not m and not k and not invert:
            sound(frequency, duration)
            canvas.create_oval(5 + i * 30 - duration_to_size[duration], 10 + j * 30 - duration_to_size[duration],
                               15 + i * 30 + duration_to_size[duration], 20 + j * 30 + duration_to_size[duration],
                               fill=FREQUENCY_TO_COLOR[frequency])
            canvas.update()
        elif frequency == 1 and not m and not k and not invert:
            sound(last_frequency, duration)
            canvas.create_oval(5 + i * 30 - duration_to_size[duration], 10 + j * 30,
                               15 + i * 30 - duration_to_size[duration], 20 + j * 30 + duration_to_size[duration],
                               fill=FREQUENCY_TO_COLOR[last_frequency])
            canvas.update()
        else:
            # Put a random color and size if it have be transform, not in the dictionnary
            sound(frequency, duration)
            colors = ['white', 'red', 'green', 'cyan', 'yellow', 'blue', 'magenta', 'black']
            canvas.create_oval(5 + i * 30 - duration_to_size[duration], 10 + j * 30,
                               15 + i * 30 - duration_to_size[duration], 20 + j * 30 + duration_to_size[duration],
                               fill=choice(colors))
            canvas.update()
        i += 1
        if i == 17:
            j += 1
            i = 0
        if j == 17:
            j = 0
        last_frequency = frequency


def sound(freq, duration):
    """Play a note

    :param freq: The frequency of the note ie: 396
    :param duration: The duration in second ie: 1
    :return: Nothing, The sound of the note in the speaker ie: SOL for 1 second
    """
    # get time steps for each sample , "duration" is note duration in seconds
    sample_rate = 44100
    t = np.linspace(0, duration, int(duration * sample_rate), False)
    # generate sine wave tone
    tone = np.sin(freq * t * (6) * np.pi)
    # normalize to 24−bit range
    tone *= 8388607 / np.max(np.abs(tone))
    # convert to 32−bit data
    tone = tone.astype(np.int32)
    # convert from 32−bit to 24−bit by building a new byte buffer,
    # skipping every fourth bit
    # note: this also works for 2−channel audio
    i = 0
    byte_array = []
    for b in tone.tobytes():
        if i % 4 != 3:
            byte_array.append(b)
        i += 1
    audio = bytearray(byte_array)
    # start playback
    play_obj = sa.play_buffer(audio, 1, 3, sample_rate)
    # wait for playback to finish before exiting
    play_obj.wait_done()
