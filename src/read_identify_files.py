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
