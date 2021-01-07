"""
All the functions used to read and writes the file - add_partition() -> main.py
Author: Titouan DUPUIS

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


def correct_accent(text):
    """Fix the encoding problem with the accent
    
    :param text: The text full of encoding problem
    :return: The free of these problem
    """
    for i in range(len(text)):
        if text[i - 1] == 'Ã' and text[i] == '¨':
            text = text[:i - 1] + 'è' + text[i + 1:]
        elif text[i - 1] == 'Ã' and text[i] == '¢':
            text = text[:i - 1] + 'â' + text[i + 1:]
        elif text[i - 1] == 'Ã' and text[i] == '©':
            text = text[:i - 1] + 'é' + text[i + 1:]
        elif text[i - 1] == 'Ã' and text[i] == 'ª':
            text = text[:i - 1] + 'ê' + text[i + 1:]
        elif text[i - 1] == 'Ã' and text[i] == '«':
            text = text[:i - 1] + 'ë' + text[i + 1:]
        elif text[i - 1] == 'Ã' and text[i] == '¹':
            text = text[:i - 1] + 'ù' + text[i + 1:]
        elif text[i - 4] == 'Ã' and text[i - 2] == 'x' and text[i - 1] == 'a' and text[i] == '0':
            text = text[:i - 4] + 'à' + text[i + 1:]

    return text


def read_files(filepath):
    """Read a file and return the list of all music

    :param filepath: The path to file containing all musics ie: "partitions.txt"
    :return: A list of all the music and there [("#1 Joyeux anniversaire", "SOLc p Zc SOLn")]
    """
    file_read = open(filepath, "r")
    aff = []
    aff_temp = []
    n = 0
    lignes = file_read.readlines()
    for ligne in lignes:
        n += 1
        if ligne[-1] == '\n':
            ligne = ligne[0:-1]
        ligne = correct_accent(ligne)
        aff_temp.append(ligne)
        if n >= 2:
            aff.append(aff_temp)
            aff_temp = []
            n = 0
    file_read.close()
    return aff
