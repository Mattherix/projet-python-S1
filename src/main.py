"""
The main file. It manage the UI, it's the glue of the program. + the add_partition() functions
Author: Matthieu ROQUEJOFFRE
Minor modification made by: Titouan DUPUIS

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

from tkinter import Tk, Canvas, BOTTOM, Button, Label, TOP, Listbox, Checkbutton, filedialog, Scale, IntVar, \
    BooleanVar, Text, LEFT

from src.player import play
from src.read_identify_files import read_files

global partitions


def add_partition(text, partition, file, liste):
    """Write the file, add a partition

    Why do you use a global variable instead of return a variable
        -> You can't get the return value of a fuction call via a tkinter button
    Why is it in the main file ? Why not in the read_identify_files.py file ?
        -> If you put this function in the read_identify_files.py file you will be forced to import the main file to
        access the global variable, creating an import loop

    Sadly translation, invert and markov operation are not allowed,
    we won't be able to encode the partition after that.

    :param text: The text field with the title
    :param partition: The partition field with the partition
    :param file: The name of the file
    :param liste: A Listbox(window) object
    :return: Nothing, you can't return something if it's call by a tkinter button
    Side effet: edit the global variable partitions, partitions
    """
    global partitions
    title = ''.join(text.get("1.0", "end").split('\n'))
    partition = ''.join(partition.get("1.0", "end").split('\n'))

    with open(file, 'a') as f:
        f.write(title + '\n')
        f.write(partition + '\n')
    liste.insert(-1, title)

    partitions.append(partition)


def get_index(liste=None):
    """A function witch return the index of the musique selected by the user, if selected.

    :param liste: The Listbox() object containing the user input
    :return: The index of the selected item
    """
    if liste.curselection():
        return liste.curselection()[0]
    else:
        return 0


def get_partitions_in_liste(window, filepath):
    """Get all the partions and return a tk liste

    :param window: The windows where the list will be attach
    :param filepath: The filepath
    :return: The ListBox object and the partitions
    """
    liste = Listbox(window)
    partitions = []
    for i, title_and_partitions in enumerate(read_files(filepath)):
        liste.insert(i + 1, title_and_partitions[0])
        partitions.append(title_and_partitions[1])
    return liste, partitions


def main():
    """The main function, a warpper around the main code.
    Do everything about the UI.
    Linked the UI ("Jouer" button, "Sauvergarder" button) to there respective function.

    :return: False if the programme have correctly terminate
    """
    window = Tk()
    window['bg'] = "#9E9E9E"
    window.geometry('1000x980')
    window.title("Projet python")

    # Ask for the file and create the ListBox
    filepath = filedialog.askopenfilename(initialdir="/", title="Choisir un fichier", filetypes=(
        ("partitions files", "*.txt"), ("all files", "*.*")))
    if not filepath:
        filepath = 'partition.txt'

    liste, partitions = get_partitions_in_liste(window, filepath)
    liste.pack(side=LEFT)

    # Create the top sections
    label = Label(window, text="Création d'une partition")
    label.pack()
    label = Label(window, text="Titre de la nouvelle musique ex: Yesterday")
    label.pack()
    title = Text(window, height=5, width=20)
    title.pack(side=TOP)
    label = Label(window, text="Partition, ex: SOLc p Zc SOLn LAn SOLn DOn Zc SIb SOLc p Zc SOLn")
    label.pack()
    text = Text(window, height=5, width=20)
    text.pack(side=TOP)

    btn_2 = Button(window, text="Sauvegarder", width=15,
                   command=lambda: add_partition(title, text, filepath, liste))
    btn_2.pack(side=TOP, pady=5)

    # Canvas for the animation
    canvas = Canvas(window, bg='#EEEEEE', height=300, width=500, bd=0, highlightthickness=0)
    canvas.pack()

    # Create the edit partition section
    k = IntVar()
    invert = BooleanVar()
    m = BooleanVar()
    mn = IntVar()
    mr = BooleanVar()
    btn_transposition = Scale(window, orient='horizontal', from_=-100, to=100, tickinterval=1, length=350, variable=k)
    btn_invertion = Checkbutton(window, text="Invertion", variable=invert)
    btn_markov = Checkbutton(window, text="Chaine de Markov. Sélectionez une musique de référence puis le nombre de "
                                          "notes",
                             variable=m)
    label_nbnote_markov = Label(window, text="Mettre le nombre de notes à 0 facilite l'ajout de plusieurs musiques de "
                                             "référence")
    btn_nbnote_markov = Scale(window, orient='horizontal', from_=0, to=120, tickinterval=15, length=350, variable=mn)
    btn_reset_markov = Checkbutton(window, text="Réinitialiser les musiques de référence pour la prochaine chaine de "
                                                "Markov",
                                   variable=mr)
    btn_transposition.pack()
    btn_invertion.pack()
    btn_markov.pack()
    label_nbnote_markov.pack()
    btn_nbnote_markov.pack()
    btn_reset_markov.pack()
    btn_1 = Button(window, text="Jouer", width=15,
                   command=lambda: play(partitions[get_index(liste)], mn.get(), mr.get(), canvas, k.get(), invert.get(), m.get(),
                                        partition_markov=text.get("1.0", "end")))
    # Bottom section
    btn_1.pack()
    btn_3 = Button(window, text="Quitter", width=15, command=window.destroy)
    btn_3.pack(side=BOTTOM)

    window.mainloop()

    return False
