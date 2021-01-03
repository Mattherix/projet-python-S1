import random

#fonctionne pas
def ampli_tab(tab):
    new_tab = []
    for i in range(len(tab)):
        if tab[i] > 0:
            n = tab[i]
            for t in range(n):
                new_tab.append(n)
    return new_tab

#non tester
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

#fonctionne
def Markov_reset(mark, ver):
    if (ver == True) or (mark == []):
        #                Do=0                   Ré=1                   Mi=2                  Fa=3                   Sol=4                  La=5                  Si=6            Do Ré Mi Fa Sol La Si
        # indice mark((Do, Ré, Mi, Fa, Sol, La, Si),(Do, Ré, Mi, Fa, ...), ...)
        mark = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]

    return mark

#ne fonctionne pas correctment
def Markov_set(parti, mark):
    #pas tester correctement      {
    ntab = []
    for i in range(1, len(parti)):
        if (parti[i-1:i] == 'DO'):
            ntab.append(0)
        if (parti[i-1:i] == 'RE'):
            ntab.append(1)
        if (parti[i-1:i] == 'MI'):
            ntab.append(2)
        if (parti[i-1:i] == 'FA'):
            ntab.append(3)
        if (parti[i-1:i+1] == 'SOL'):
            ntab.append(4)
        if (parti[i-1:i] == 'LA'):
            ntab.append(5)
        if (parti[i-1:i] == 'SI'):
            ntab.append(6)
            #                     }
    #ind1 et ind2 sont vide sans raison?
    for i in range(1, len(ntab)):
        ind1 = ntab[i-1]
        ind2 = ntab[i]
        mark[7][ind1] = mark[7][ind1]+1
        mark[ind1][ind2] = mark[ind1][ind2]+1
    return mark

#bloqué par 'ampli_tab'
def Markov_use(tab, nb):
    T = []
    file = open("markov.txt", 'w')
    T.append(ampli_tab(tab(7)))
    r = random.randint(0, len(T)-1)
    ind = T(r)
    wrgt = write_note(ind)
    file.write(wrgt + " ")
    for i in range(nb-1):
        T = ampli_tab(tab(ind))
        r = random.randint(0, len(T)-1)
        ind = T(r)
        wrgt = write_note(ind)
        file.write(wrgt + " ")

#test
TAB = []
A = Markov_reset(TAB, False)
B = Markov_set('SOLc p Zc SOLn LAn SOLn DOn Zc SIb SOLc p Zc SOLn LAn SOLn REn Zc DOb SOLc', A)
print(B)
C = Markov_use(B, 10)
