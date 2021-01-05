import numpy as np
import simpleaudio as sa

from src.edit import transposition, invertion
from src.utils import decode_partition, NOTE_TO_FREQUENCY


def play(partition, k=None, invert=False):
    """Play a give partion

    :param partition: The partion as a strings
    :param k: The number used in the transposition, by default none
    :param invert: Do an inverion on the partition, by default at False
    :return: Nothing
    """
    partition = decode_partition(partition, NOTE_TO_FREQUENCY, 0.25)
    print(partition)
    if k:
        partition = transposition(partition, k)
    if invert:
        partition = invertion(partition)
    print(partition)
    last_frequency = 0
    for frequency, duration in partition:
        if frequency != -1:
            sound(frequency, duration)
        else:
            sound(last_frequency, duration)
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

