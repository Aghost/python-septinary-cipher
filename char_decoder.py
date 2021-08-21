def to_ascii(string):
    ascii_list = []
    for c in range(len(string)):
        ascii_list.append(ord(string[c]))
    return ascii_list

def to_cypher(ascii_list, offset = 5):
    new_list = []
    for c in range(len(ascii_list)):
        new_list.append(ascii_list[c] + offset)
    return new_list

def to_str(ascii_list):
    string = []
    for c in range(len(ascii_list)):
        string.append(chr(ascii_list[c])) 
    return ''.join(string)

def the_print_f(val, cod):
    print("inputstr {1}:{0}".format(str(val), cod))

with open('./data.txt', 'r') as file:
    data = file.read().replace('\n', '')
        
print("data :" + data + "\n\n")

inputstr = to_ascii(data)   # convert inputstr to ascii values
the_print_f(inputstr, "to ascii")

inputstr = to_cypher(inputstr, 10)  # convert inputstr to cypher values
the_print_f(inputstr, "to cypher +10")

inputstr = to_str(inputstr) # convert inputstr to string
the_print_f(inputstr, "to string")

inputstr = to_ascii(data)   # convert inputstr to ascii values
the_print_f(inputstr, "to ascii")

inputstr = to_str(inputstr)
the_print_f(inputstr, "to string")

print("done")

#inputstr = inputstr.encode('utf-8', 'strict')
#print(inputstr.decode('utf-8', 'strict'))
