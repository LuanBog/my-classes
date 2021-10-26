#!/usr/bin/env python

def encode(text):
    result = ''

    for letter in text:
        result += '0' + bin(ord(letter))[2:] + ' '

    return result.rstrip()

def decode(binaries):
    result = ''

    for binary in binaries.split(' '):
        result += chr(int(binary, 2))

    return result

def main():
    try:
        mode = input('\n[A] Encode\n[B] Decode\n\nMode: ').lower()

        if mode == 'a':
            text = input('\nEnter text: ')
            encoded = encode(text.strip())

            print('Encoded: {}'.format(encoded))
        elif mode == 'b':
            binaries = input('\nEnter binaries: ')
            decoded = decode(binaries.strip())

            print('Decoded: {}'.format(decoded))
        else:
            print('\nThat mode doesn\'t exist!')
    except KeyboardInterrupt:
        print('\n\nQuiting. Have fun learning!')

if __name__ == '__main__':
    main()
