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


def encode_partition(partition, note_to_frequency, quaver):
    """Encode the partition as a strings

    :param partition: The partition ie: [(396, 5), (396, 2.5), (-1, 20)]
    :param note_to_frequency: A dictionary with note associate with there frequency
    :param quaver: The lenght of the quaver (croche)
    :return: The encoded strings ie: "SOLc p Zb" if quaver is 5
    """
    figures_to_durations = get_figures_duration(quaver)
    durations_to_figures = {duration: figure for figure, duration in figures_to_durations.items()}

    frequency_to_note = {frequency: note for note, frequency in note_to_frequency.items()}

    last_note = (None, 0)
    encoded_partition = []
    for frequency, duration in partition:
        if frequency == last_note[0] and duration == (last_note[1] / 2):
            encoded_partition.append('p')
        else:
            encoded_partition.append(frequency_to_note[frequency] + durations_to_figures[duration])
        last_note = (frequency, duration)

    return ' '.join(encoded_partition)
