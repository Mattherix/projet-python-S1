from time import sleep
import numpy as np
import simpleaudio as sa


def play():
    pass


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



