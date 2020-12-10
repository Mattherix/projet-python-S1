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
