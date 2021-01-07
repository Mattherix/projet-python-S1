from math import inf


def get_maxi_notes(notes):
    """Get the the highest frequency from the notes

    :param notes: The list of notes ie: [(495, 5), (396, 2.5), (-1, 20)]
    :return: The maximum frequency ie: 495
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
    return maxi


def transposition(notes, k):
    """Apply a transposition to all the notes

    :param notes: The list of notes ie: [(396, 5), (396, 2.5), (-1, 20)]
    :param k: The number use in the transposition ie: 15
    :return: All the notes transposed by k ie: [(15, 5), (15, 2.5), (-1, 20)]
    """
    maxi = get_maxi_notes(notes)

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


def invertion(notes):
    """Invert all the notes

    :param notes: The list of notes ie: [(396, 5), (396, 2.5), (-1, 20)]
    :return: All the notes invert ie: [(0, 5), (0, 2.5), (-1, 20)]
    """
    maxi = get_maxi_notes(notes)
    new_notes = []
    for frequency, duration in notes:
        if frequency > 0:
            new_notes.append((
                (maxi - frequency) % maxi,
                duration
            ))
        else:
            new_notes.append((
                frequency,
                duration
            ))
    return new_notes
