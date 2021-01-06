from tkinter import Tk, Canvas, BOTTOM, Button, Label, TOP, Listbox, Checkbutton, filedialog, Scale, IntVar, \
    BooleanVar

from src.player import play
from src.read_identify_files import read_files

window = Tk()
window['bg'] = "#9E9E9E"
window.geometry('400x200')
window.title("Projet python")

label = Label(window, text="Choisiser une partion")
label.pack()

filepath = filedialog.askopenfilename(initialdir="/", title="Choisir un fichier", filetypes=(
    ("partitions files", "*.txt"), ("all files", "*.*")))
if not filepath:
    filepath = '../partition.txt'

liste = Listbox(window)
partitions = []
for i, title_and_partitions in enumerate(read_files(filepath)):
    liste.insert(i + 1, title_and_partitions[0])
    partitions.append(title_and_partitions[1])
liste.pack()

canvas = Canvas(window, bg='#EEEEEE', height=500, width=500, bd=0, highlightthickness=0)
canvas.pack(side=TOP)


def get_index():
    if liste.curselection():
        return liste.curselection()[0]
    else:
        return 0


k = IntVar()
invert = BooleanVar()
btn_transposition = Scale(window, orient='horizontal', from_=-100, to=100, tickinterval=1, length=350, variable=k)
btn_invertion = Checkbutton(window, text="Invertion", variable=invert)
btn_transposition.pack()
btn_invertion.pack()
btn = Button(window, text="Jouer", width=15, command=lambda: play(partitions[get_index()], canvas, k.get(), invert.get()))
btn.pack(side=TOP, pady=5)

btn = Button(window, text="Quitter", width=15, command=window.destroy)
btn.pack(side=BOTTOM, pady=5)

window.mainloop()
