from tkinter import Tk, Canvas, BOTTOM, Button, Label, TOP, Listbox, Checkbutton, filedialog

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
for i, title in enumerate(read_files(filepath)):
    liste.insert(i + 1, title[0])
liste.pack()

canvas = Canvas(window, bg='#EEEEEE', height=500, width=500, bd=0, highlightthickness=0)
canvas.pack(side=TOP)

btn = Button(window, text="Jouer", width=15, command=play)
btn.pack(side=TOP, pady=5)
btn_transposition = Checkbutton(window, text="Transposition")
btn_invertion = Checkbutton(window, text="Invertion")
btn_transposition.pack()
btn_invertion.pack()

btn = Button(window, text="Quitter", width=15, command=window.destroy)
btn.pack(side=BOTTOM, pady=5)

window.mainloop()
