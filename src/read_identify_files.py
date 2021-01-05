"""
#ne fonctionne pas, à refaire
#erreur "'str' object does not support item assignment"
def correct_accent(text):
    for i in range(len(text)):
        if text[i-1] == 'Ã' and text[i] == '¨':
            text[i-1:i] = 'è'
        elif text[i-1] == 'Ã' and text[i] == '¢':
            text[i-1:i] = 'â'
        elif text[i-1] == 'Ã' and text[i] == '©':
            text[i-1:i] = 'é'
        elif text[i-1] == 'Ã' and text[i] == 'ª':
            text[i-1:i] = 'ê'
        elif text[i-1] == 'Ã' and text[i] == '«':
            text[i-1:i] = 'ë'
        elif text[i-1] == 'Ã' and text[i] == '¹':
            text[i-1:i] = 'ù'
        #pb pour "à"
        elif text[i-3] == 'Ã' and text[i-2] == 'x' and text[i-1] == 'a' and text[i] == '0':
            text[i-3:i] = 'à'
    return text
"""


def read_files(file):
    """Read the file and return all the titles and partion

    :param file: The name of the file 
    :return: A list of partion and a list titles
    """
    Rfile = open(file, "r")

    aff = []
    titre = []
    aff_temp = []
    n = 0
    lignes = Rfile.readlines()
    for ligne in lignes:
        n += 1
        if ligne[-1] == '\n':
            ligne = ligne[0:-1]
        # ligne = correct_accent(ligne)
        aff_temp.append(ligne)
        if n == 1:
            titre.append(aff_temp)
            aff.append(aff_temp)
            aff_temp = []
            n = 0
        else:
            aff.append(aff_temp)
            aff_temp = []
            n = 1
    return aff, titre
