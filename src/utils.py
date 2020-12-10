NOTE_TO_FREQUENCY = {
    "DO": 264,
    "RE": 297,
    "MI": 330,
    "FA": 352,
    "SOL": 396,
    "LA": 440,
    "SI": 495,
    "Z": -1
}


def get_figures_duration(quaver):
    """Calculate the lenght of every figures

    :param quaver: The lenght of the quaver (croche)
    :return: A dict with every figures associate with there lenght
    """
    return {
        'r': 8 * quaver,
        'b': 4 * quaver,
        'n': 2 * quaver,
        'c': quaver
    }


def decode_partition(partition, note_to_frequency, quaver):
    """Decode the partition read from the file

    :param partition: The partition read ie: "SOLc p Zb"
    :param note_to_frequency: A dictionary with note associate with there frequency
    :param quaver: The lenght of the quaver (croche)
    :return: A list of frequency and duration ie: [(396, quaver), (396, quaver/2), (-1, 2 * quaver)]
    """
    figures_to_durations = get_figures_duration(quaver)
    decoded_partition = []
    for note in partition.split():
        if note == 'p':
            decoded_partition.append((
                decoded_partition[-1][0],
                decoded_partition[-1][1] / 2
            ))
        else:
            decoded_partition.append((
                note_to_frequency[note[:-1]],
                figures_to_durations[note[-1]]
            ))
    return decoded_partition
