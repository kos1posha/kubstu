def slices(string):
    return string[2] + "\n" + \
           string[-2] + "\n" + \
           string[:5] + "\n" + \
           string[:-2] + "\n" + \
           string[::2] + "\n" + \
           string[1::2] + "\n" + \
           string[::-1] + "\n" + \
           string[::-2] + "\n" + \
           str(len(string))