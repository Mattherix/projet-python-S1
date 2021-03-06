"""
Made all the computation linked to Markov
Author: Titouan DUPUIS
Minor modification made by: Matthieu ROQUEJOFFRE

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
import random

def ampli_tab(tab):
    """Used to set the RNG's interval to create the partition by using the list of note frequency

    :param tab: Note frenquency list.  example [0, 3, 5, 1, 0, 4, 1]
    :return: RNG's interval list.  example [1, 1, 1, 2, 2, 2, 2, 2, 3, 5, 5, 5, 5, 6]
    """
    new_tab = []
    for i in range(len(tab)):
        if tab[i] > 0:
            n = tab[i]
            for t in range(n):
                new_tab.append(i)
    return new_tab


def write_note(n):
    """Identify a note by the number get in the RNG's interval list, and return the str note

    :param n: The number of the RNG's interval list
    :return: The str note
    """
    
    Dict = {
        0: 'DO',
        1: 'RE',
        2: 'MI',
        3: 'FA',
        4: 'SOL',
        5: 'LA',
        6: 'SI'
    }

    return Dict.get(n)


def markov_reset(mark, ver, markov_partition):
    """Reset all the settings if ver = True or if the note frequency list is empty, else it will do nothing

    :param mark: The note frquency list
    :param ver: Boolean that defined if the note frequency list should reset
    :param markov_partition: The final partition that will be return when all steps are done in markov.py
    :return: The frequency list and the partition
    """
    if ver or (mark == []):
        # Do=0                   Ré=1                   Mi=2                  Fa=3
        # Sol=4                   La=5                  Si=6            Do Ré Mi Fa Sol La Si
        #  indice -> ((Do, Ré, Mi, Fa, Sol, La, Si),(Do, Ré, Mi, Fa, ...), ...)
        mark = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        markov_partition = ''

    return mark, markov_partition


def markov_set(parti, mark):
    """Take the reference partition and the note frenquency, and return a new note frequency list

    :param parti: The reference partition str
    :param mark: The note frequency list
    :return: The modified note frequency list
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

    :param tab: The note frequency list
    :param nb: The number Int of notes for the partition in return
    :param markov_partition: The partition str that will be return
    :return: The new partition str
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


def markov(partition, partition_origin, number_of_note, reset_value):
    """Create a partition with markov

    :param partition: The partion as a string
    :param partition_origin: The original partition
    :param number_of_note: Number of note in the new partition
    :return: The partition as a strings
    """
    mark, markov_partition = markov_reset([], reset_value, partition)
    tab = markov_set(partition_origin, mark)
    return markov_use(tab, number_of_note, markov_partition)
