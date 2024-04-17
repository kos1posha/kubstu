def remove(list, index):
    for i, _ in enumerate(list):
        if i > index:
            list[i], list[i - 1] = list[i - 1], list[i]
    list.pop()
    return list