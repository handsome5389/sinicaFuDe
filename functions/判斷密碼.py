while True:
    print('Account name:')
    name = input()
    if name != 'success':
        continue
    print('Password, please:')
    password = input()
    if password == 'selflearning':
        break
print('Welcome to Self Learning Success!')