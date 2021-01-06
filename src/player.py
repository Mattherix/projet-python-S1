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


def play(partition, canvas, k=None, invert=False, m=False, partition_markov=""):
    """Play a give partion

    :param partition: The partion as a strings
    :param canvas: The canvas used to draw
    :param k: The number used in the transposition, by default none
    :param invert: Do an inverion on the partition, by default at False
    :param m: Use the markov transformation, by default at False
    :param partition_markov: The partition used for markov
    :return: Nothing
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
    partition = decode_partition(partition, NOTE_TO_FREQUENCY, quaver)
    if m:
        partition = markov(partition_markov, partition, number_of_note=20)
    if k:
        partition = transposition(partition, k)
    if invert:
        partition = invertion(partition)
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

    :param freq: The frequency of the note
    :param duration: The duration in second
    :return: Nothing
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
