def fixed_length(file_path, length=80):
    file_content = [word for word in [line.split(' ')[0] for line in open(file_path).read().split('\n')]]
    print('-' * length)
    current_line = ''
    for i in file_content:
        if len(current_line + i) > length:
            print(current_line)
            current_line = ''
        else:
            current_line += i + ' '
    print(current_line)
