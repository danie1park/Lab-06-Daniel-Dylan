def main():
    encoded_password = ''
    while True:
        print('Menu')
        print('-' * 13)
        print('1. Encode')
        print('2. Decode')
        print('3. Quit\n')
        choice = input('Please enter an option: ')
        if choice == '1':
            password = input('Please enter your password to encode: ')
            encoded_password = encode(password)
            print(encoded_password)
            print('Your password has been encoded and stored!')

        if choice == '2':
            print(f'The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.')

        if choice == '3':
            break


def encode(password):
    encoded_password = ''
    for char in password:
        new_char = str((int(char) + 3) % 10)
        encoded_password += new_char

    return encoded_password


def decode(password):
    # decoded_password = ''
    # for char in password:
    #     if char > '2':
    #         new_char = str(int(char) - 3)
    #         decoded_password += new_char
    #     else:
    #         new_char = str(int(char) + 7)
    #         decoded_password += new_char
    # return decoded_password
    return None


if __name__ == '__main__':
    main()
