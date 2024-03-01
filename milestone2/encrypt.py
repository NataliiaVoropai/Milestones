def encrypt() -> str:
    message = input('Enter a message to encrypt: ')
    key = ''
    while key.isdigit() is not True:
        key = input('Enter int as key: ')
    key = int(key)
    abc = 'abcdefghijklmnopqrstuvwxyz'
    new_message = ''
    for i in message:
        if i.lower() in abc:
            if i.isupper():
                new_message += abc[(abc.find(i.lower()) + key) % 26].upper()
            else:
                new_message += abc[(abc.find(i) + key) % 26]
        else:
            new_message += i
    return new_message


print(encrypt())
