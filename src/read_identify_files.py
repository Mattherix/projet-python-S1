def read_files(file):
    Rfile = open(file, "r")

    aff = []
    aff_temp = []
    n = 0
    lignes = Rfile.readlines()
    for ligne in lignes:
        n += 1
        if ligne[-1] == '\n':
            ligne = ligne[0:-1]
        aff_temp.append(ligne)
        if n >= 2:
            aff.append(aff_temp)
            aff_temp = []
            n = 0

    return aff
