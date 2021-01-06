import random

#used to set the RNG to create the partition
def ampli_tab(tab):
    new_tab = []
    for i in range(len(tab)):
        if tab[i] > 0:
            n = tab[i]
            for t in range(n):
                new_tab.append(i)
    return new_tab

#identify a note by the number inside the note frequency list, and return the str note
def write_note(n):
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

#Reset all the settings if ver = True or if the note frequency list is empty, else it will do nothing
def Markov_reset(mark, ver, markov_partition):
    if (ver == True) or (mark == []):
        #                Do=0                   Ré=1                   Mi=2                  Fa=3                   Sol=4                  La=5                  Si=6            Do Ré Mi Fa Sol La Si
        # indice -> ((Do, Ré, Mi, Fa, Sol, La, Si),(Do, Ré, Mi, Fa, ...), ...)
        mark = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
        markov_partition = ''

    return mark, markov_partition

#Take the reference partition and the note frenquency, and return a new note frequency list
def Markov_set(parti, mark):
    ntab = []
    for i in range(0, len(parti)):
        if (parti[i] == 'D'):
            ntab.append(0)
        if (parti[i] == 'R'):
            ntab.append(1)
        if (parti[i] == 'M'):
            ntab.append(2)
        if (parti[i] == 'F'):
            ntab.append(3)
        if (parti[i] == 'S' and parti[i+1] == 'O'):
            ntab.append(4)
        if (parti[i] == 'L' and parti[i+1] == 'A'):
            ntab.append(5)
        if (parti[i] == 'S' and parti[i+1] == 'I'):
            ntab.append(6)

    for i in range(1, len(ntab)):
        ind1 = ntab[i - 1]
        ind2 = ntab[i]
        mark[7][ind1] = mark[7][ind1] + 1
        mark[ind1][ind2] = mark[ind1][ind2] + 1


    return mark

#Take the note frequency and the existing Markov partition, and you set the number of note you want in your new Markov partition
def Markov_use(tab, nb, markov_partition):
    T = []
    T = ampli_tab(tab[7])
    r = random.randint(0, len(T)-1)
    ind = T[r]
    wrgt = write_note(ind)
    markov_partition = markov_partition + (wrgt + 'n ')
    for i in range(nb-1):
        T = ampli_tab(tab[ind])
        r = random.randint(0, len(T)-1)
        ind = T[r]
        wrgt = write_note(ind)
        markov_partition = markov_partition + (wrgt + 'n ')

    return markov_partition
