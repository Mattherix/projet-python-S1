import random


# TODO: @Tidoulidou Add the parameter in the docstrings(""" Blabla """) of your functions

def ampli_tab(tab):
    """Used to set the RNG to create the partition

    :param tab:
    :return:
    """
    new_tab = []
    for i in range(len(tab)):
        if tab[i] > 0:
            n = tab[i]
            for t in range(n):
                new_tab.append(i)
    return new_tab


def write_note(n):
    # TODO: @Tidoulidou Use a dictionnary
    """Identify a note by the number inside the note frequency list, and return the str note

    :param n: the number
    :return: The str note
    """
    text = ''
    if n == 0:
        text = "DO"
    elif n == 1:
        text = "RE"
    elif n == 2:
        text = "MI"
    elif n == 3:
        text = "FA"
    elif n == 4:
        text = "SOL"
    elif n == 5:
        text = "LA"
    elif n == 6:
        text = "SI"

    return text


def markov_reset(mark, ver, markov_partition):
    """Reset all the settings if ver = True or if the note frequency list is empty, else it will do nothing

    :param mark:
    :param ver:
    :param markov_partition:
    :return:
    """
    if ver or (mark == []):
        # Do=0                   Ré=1                   Mi=2                  Fa=3                   Sol=4
        # La=5                  Si=6            Do Ré Mi Fa Sol La Si indice -> ((Do, Ré, Mi, Fa, Sol, La, Si),(Do,
        # Ré, Mi, Fa, ...), ...)
        mark = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        markov_partition = ''

    return mark, markov_partition


def markov_set(parti, mark):
    """Take the reference partition and the note frenquency, and return a new note frequency list

    :param parti:
    :param mark:
    :return:
    """
    ntab = []
    for i in range(0, len(parti)):
        if parti[i] == 'D':
            ntab.append(0)
        if parti[i] == 'R':
            ntab.append(1)
        if parti[i] == 'M':
            ntab.append(2)
        if parti[i] == 'F':
            ntab.append(3)
        if parti[i] == 'S' and parti[i + 1] == 'O':
            ntab.append(4)
        if parti[i] == 'L' and parti[i + 1] == 'A':
            ntab.append(5)
        if parti[i] == 'S' and parti[i + 1] == 'I':
            ntab.append(6)

    for i in range(1, len(ntab)):
        ind1 = ntab[i - 1]
        ind2 = ntab[i]
        mark[7][ind1] = mark[7][ind1] + 1
        mark[ind1][ind2] = mark[ind1][ind2] + 1

    return mark


def markov_use(tab, nb, markov_partition):
    """Take the note frequency and the existing Markov partition, and you set the number of note you want in your new
    Markov partition

    :param tab:
    :param nb:
    :param markov_partition:
    :return:
    """
    t = []
    t = ampli_tab(tab[7])
    r = random.randint(0, len(t) - 1)
    ind = t[r]
    wrgt = write_note(ind)
    markov_partition = markov_partition + (wrgt + 'n ')
    for i in range(nb - 1):
        t = ampli_tab(tab[ind])
        r = random.randint(0, len(t) - 1)
        ind = t[r]
        wrgt = write_note(ind)
        markov_partition = markov_partition + (wrgt + 'n ')

    return markov_partition


def markov(partition, partition_origin, number_of_note=20):
    """Create a partition with markov

    :param partition: The partion as a string i.e. "SOLc p Zb"
    :param partition_origin: The original partition
    :param number_of_note: Number of note in the new partition, default 20
    :return: The partition as a strings
    """
    mark, markov_partition = markov_reset([], False, partition)
    tab = markov_set(partition_origin, mark)
    return markov_use(tab, number_of_note, markov_partition)
