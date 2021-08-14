import sys;

CIPHER = [ 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1 ]
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
MESSAGE = ""
OFFSET = 96 + 0

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# charstr.append(character)
def encipher(string):                       ### TODO : Ordinal to ASCII
    for char in range(len(string)):
        ordinal = ord(string[char]) - OFFSET
        print(str(ordinal))
        # ordinal %= 26
        if 0 <= ordinal <= 26:
            print(CIPHER[ordinal], end = '')
        else:
            print(' ', end = '')

def decipher(string):                       ### TODO : join / combine to a single string
    for char in range(len(string)):
        ordinal = ord(string[char]) - OFFSET
        print(str(ordinal))
        # ordinal %= 26
        if 0 <= ordinal <= 26:
            print(CIPHER[ordinal], end = '')
        else:
            print(' ', end = '')

def text_const(string):
    charstr = []
    for char in range(len(string)):
        ordinal = ord(string[char]) - OFFSET 
        #ordinal %= 26
        if 0 <= ordinal <= 26:
            if ordinal == 7 or ordinal == 20 :
                character = print(bcolors.WARNING, end='')
            elif (0 <= ordinal <= 6) or (14 <= ordinal <= 19):
                character = print(bcolors.OKGREEN, end='')
            else:
                character = print(bcolors.FAIL, end='')
            if ordinal > 13:
                character = print(bcolors.UNDERLINE, end='')
            elif ordinal <= 13:
                character = print(bcolors.BOLD, end='')
            #character = print(string[char] + bcolors.ENDC, end='')
            character = print(str(CIPHER[ordinal - 1]) + bcolors.ENDC, end='')
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

def test():
    a = ALPHABET 
    decode_sept(a)
    #text_const(a)

def main(argv):
    argument = argv
    print(ALPHABET)
    text_const(ALPHABET)
    print("hallo alles goed")
    text_const("hallo alles goed")
    # decipher("aardappel")
    #test()

if __name__ == "__main__":
    main(sys.argv)
