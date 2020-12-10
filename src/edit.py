from math import inf


def transposition(notes, k):
    """Apply a transposition to all the notes

    :param notes: The list of notes
    :param k: The number use in the transposition
    :return: All the notes transposed by k
    """
    maxi = -inf
    frequencies = []
    for frequency, _ in notes:
        if len(frequencies) == 8:
            # There is only 8 type of notes (including the silence)
            break
        if frequency not in frequencies:
            frequencies.append(frequency)
        if frequency > maxi:
            maxi = frequency

    new_notes = []
    for frequency, duration in notes:
        if frequency > 0:
            new_notes.append((
                (frequency + k) % maxi,
                duration
            ))
        else:
            new_notes.append((
                frequency,
                duration
            ))
    return new_notes

