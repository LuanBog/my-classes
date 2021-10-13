#!/usr/bin/env python

# If a's length is longer than b
def adjust(a, b):
    if len(a) == len(b):
        return b
    else:
        amount_to_add = len(a) - len(b)
        b = ' ' * amount_to_add + b

        return b

def binary_zip(a, b):
    b = adjust(a, b)

    return [list(x) for x in zip(a, b)]

def seperate(text, amount=1):
    text = str(text)

    new_text = ''

    for letter in text:
        new_text += letter + ' ' * amount
    
    return new_text.rstrip() 

def addition(a, b):
    sum = bin(int(a, 2) + int(b, 2))[2:]
    adjust_count = len(seperate(sum)) - len(seperate(a))
    adjust_string =  ' ' * adjust_count if adjust_count > 0 else ''

    # Handles carries
    carries = ''
    zipped = list(reversed(binary_zip(a, b)))

    for index, octet in enumerate(zipped):
        # This octet has a carry
        if len(octet) == 3:
            carries += '1'

            if octet[0] == '1' or octet[1] == '1':
                if index + 1 < len(zipped):
                    zipped[index + 1].append('1')
                else:
                    zipped.insert(index + 1, ['x', 'x', '1'])
        else:
            carries += ' '

            if octet[0] == '1' and octet[1] == '1':
                if index + 1 < len(zipped):
                    zipped[index + 1].append('1')
                else:
                    zipped.insert(index + 1, ['x', 'x', '1'])

    carries = carries[::-1]

    print('Addition:\n')
    print(seperate(carries))
    print(adjust_string + seperate(a))
    print(adjust_string + seperate(adjust(a, b)))
    print('-' * len(seperate(sum)))
    print(seperate(sum))

def main():
    top_binary = input('Top Binary: ')
    bottom_binary = input('Bottom Binary: ')
    operation = input('[+] Addition, [-] Subtraction, [*] Multiplication, [/] Division: ')

    if operation == '+':
        addition(top_binary, bottom_binary)
    else:
        print('That hasn\'t been implemented yet!')

if __name__ == '__main__':
    main()
