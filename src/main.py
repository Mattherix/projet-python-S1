from tkinter import Tk, Canvas, BOTTOM, Button, Label, TOP, Listbox, Checkbutton, filedialog, Scale, IntVar, \
    BooleanVar, Text, LEFT

from src.edit import transposition, invertion
from src.markov import markov
from src.player import play
from src.read_identify_files import read_files
from src.utils import decode_partition, NOTE_TO_FREQUENCY, encode_partition


def add_partition(text, partition, file, liste, k=None, invert=False, m=False, partition_markov=""):
    """Write the file, add a partition

    :param text: The text field with the title
    :param partition: The partition field with the partition
    :param file: The name of the file
    :param liste: A Listbox(window) object
    :param k: The number used in the transposition, by default none
    :param invert: Do an inverion on the partition, by default at False
    :param m: Use the markov transformation, by default at False
    :param partition_markov: The partition used for markov
    :return: Nothing
    """
    global partitions
    title = ''.join(text.get("1.0", "end").split('\n'))
    partition = ''.join(partition.get("1.0", "end").split('\n'))

    quaver = 0.25
    partition = decode_partition(partition, NOTE_TO_FREQUENCY, quaver)
    if m:
        partition = markov(partition_markov, partition, number_of_note=20)
    if k:
        partition = transposition(partition, k)
    if invert:
        partition = invertion(partition)
    partition = encode_partition(partition, NOTE_TO_FREQUENCY, quaver)

    with open(file, 'a') as f:
        f.write(title + '\n')
        f.write(partition + '\n')
    liste.insert(len(partitions) + 1, title)

    partitions.append(partition)


def main():
    """The main function

    :return: Notion
    """
    window = Tk()
    window['bg'] = "#9E9E9E"
    window.geometry('400x200')
    window.title("Projet python")

    filepath = filedialog.askopenfilename(initialdir="/", title="Choisir un fichier", filetypes=(
        ("partitions files", "*.txt"), ("all files", "*.*")))
    if not filepath:
        filepath = 'partition.txt'

    global partitions
    liste = Listbox(window)
    partitions = []
    for i, title_and_partitions in enumerate(read_files(filepath)):
        liste.insert(i + 1, title_and_partitions[0])
        partitions.append(title_and_partitions[1])
    liste.pack(side=LEFT)

    label = Label(window, text="Titre de la nouvelle musique ex: Yesterday")
    label.pack()
    title = Text(window, height=5, width=20)
    title.pack(side=TOP)
    label = Label(window, text="Partition, ex: SOLc p Zc SOLn LAn SOLn DOn Zc SIb SOLc p Zc SOLn")
    label.pack()
    text = Text(window, height=5, width=20)
    text.pack(side=TOP)

    btn_2 = Button(window, text="Sauvegarder", width=15,
                   command=lambda: add_partition(title, text, filepath, liste, k.get(), invert.get(), m.get(), text.get("1.0", "end")))
    btn_2.pack(side=TOP, pady=5)

    canvas = Canvas(window, bg='#EEEEEE', height=500, width=500, bd=0, highlightthickness=0)
    canvas.pack()

    def get_index():
        if liste.curselection():
            return liste.curselection()[0]
        else:
            return 0

    k = IntVar()
    invert = BooleanVar()
    m = BooleanVar()
    btn_transposition = Scale(window, orient='horizontal', from_=-100, to=100, tickinterval=1, length=350, variable=k)
    btn_invertion = Checkbutton(window, text="Invertion", variable=invert)
    btn_markov = Checkbutton(window, text="Chaine de Markov, sélectionez une musique et entré une partition", variable=m)
    btn_transposition.pack()
    btn_invertion.pack()
    btn_markov.pack()
    btn_1 = Button(window, text="Jouer", width=15,
                   command=lambda: play(partitions[get_index()], canvas, k.get(), invert.get(), m.get(), text.get("1.0", "end")))
    btn_1.pack()

    btn_3 = Button(window, text="Quitter", width=15, command=window.destroy)
    btn_3.pack(side=BOTTOM)

    window.mainloop()

    return False
