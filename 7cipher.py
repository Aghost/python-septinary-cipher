import sys;

CIPHER = [ 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1 ]
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
OFFSET = 96 
OFFSET_ROT = 13

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def encipher26(string):
    new_list = list(range(len(string))) 
    for char in range(len(string)):
        new_list[char] = ord(string[char]) - OFFSET
    return new_list

def decipher26(int_list):
    new_string = ""
    for nr in range(len(int_list)):
        if 0 <= int_list[nr] <= 26:
            new_string += ALPHABET[int_list[nr] - 1]
        else:
            new_string += ' '
    return new_string 

def encipher7(string):
    key = list(range(len(string)))
    new_list = list(range(len(string))) 
    for char in range(len(string)):
        ordinal = ord(string[char]) - OFFSET
        if 0 <= ordinal <= 26:
            new_list[char] = CIPHER[ordinal - 1] 
            if (0 <= ordinal <= 6) or (14 <= ordinal <= 19): # if linksboven of linksonder
                key[char] = 0 # links +0
            elif (8 <= ordinal <= 13) or (21 <= ordinal <= 26): # if rechtsboven of rechtsonder
                key[char] = 1 # rechts +1
            else:
                key[char] = 2 # g/t
            if 14 <= ordinal <= 26:
                key[char] += 10 # onder +0 
        else:
            key[char] = 33
            new_list[char] = ord(string[char])
    return new_list, key

def decipher7(int_list, key_list):
    new_list = list(range(len(int_list))) 
    for nr in range(len(int_list)):
        if key_list[nr] == 0:
            new_list[nr] = int_list[nr]
        elif key_list[nr] == 1:
            new_list[nr] = 14 - int_list[nr] 
        elif key_list[nr] == 2:
            new_list[nr] = 7
        elif key_list[nr] == 10:
            new_list[nr] = int_list[nr] + 13
        elif key_list[nr] == 11:
            new_list[nr] = 27 - int_list[nr]
        elif key_list[nr] == 12:
            new_list[nr] = 20
        elif key_list[nr] == 33:
            new_list[nr] = -1
        else:
            print("unknown ordinal", key_list[nr])
    return new_list

def color_code(int_list):
    charstr = []
    for char in range(len(int_list)):
        ordinal = int_list[char]
        if 0 <= ordinal <= 26:
            if ordinal == 7 or ordinal == 20:
                character = print(bcolors.WARNING, end='')
            elif 0 <= ordinal <= 6 or 14 <= ordinal <= 19:
                character = print(bcolors.OKGREEN, end='')
            else:
                character = print(bcolors.FAIL, end='')
            if ordinal > 13:
                character = print(bcolors.UNDERLINE, end='')
            elif ordinal <= 13:
                character = print(bcolors.BOLD, end='')
            character = print(chr(ordinal + OFFSET) + bcolors.ENDC, end='')
        else:
            character = print(' ' + bcolors.ENDC, end='')
    print('')

def decode_sept(text):
    new_string = []
    for char in range(len(text)):
        value = ord(text[char]) - OFFSET
        print(value)
    print(new_string)
    return new_string 

def main(argv):
    argument = argv

    int_list_1, list_1_key = encipher7(ALPHABET)
    color_code(int_list_1)
    print(color_code(decipher7(int_list_1, list_1_key)))

    print("\nenciphering(26):", ALPHABET)
    enciphered = encipher26(ALPHABET)
    print("enciphered(26):", enciphered)
    deciphered = decipher26(enciphered)
    print("deciphered(26):", deciphered)

    print("\nenciphering(7):", deciphered)
    enciphered = encipher7(deciphered)
    print("enciphered(7):", enciphered[0])

    print("\ndeciphering(7) with key:", enciphered[1])
    deciphered = decipher7(enciphered[0], enciphered[1])
    print("deciphered(7 to 26):", deciphered)
    to_string = decipher26(deciphered)
    print("deciphered(26 to string):", to_string)

if __name__ == "__main__":
    main(sys.argv)
