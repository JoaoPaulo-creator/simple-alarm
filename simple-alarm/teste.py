user_input = str(input(': '))

if len(user_input) > 4:
    formatted = list(user_input)
    formatted.insert(2, ':')
    print(''.join(formatted[0:5]))
