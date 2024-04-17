def synonyms(dictionary: dict, word):
    try:
        return dictionary[word]
    except:
        dictionary = {value: key for key, value in dictionary.items()}
        return dictionary[word]