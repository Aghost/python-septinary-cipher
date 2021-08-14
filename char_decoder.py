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
    print("henk {1}:{0}".format(str(val), cod))

with open('./data.txt', 'r') as file:
    data = file.read().replace('\n', '')
        
print("data :" + data + "\n\n")

henk = to_ascii(data)   # convert henk to ascii values
the_print_f(henk, "to ascii")

henk = to_cypher(henk, 10)  # convert henk to cypher values
the_print_f(henk, "to cypher +10")

henk = to_str(henk) # convert henk to string
the_print_f(henk, "to string")

henk = to_ascii(data)   # convert henk to ascii values
the_print_f(henk, "to ascii")

henk = to_str(henk)
the_print_f(henk, "to string")

print("done")

#henk = henk.encode('utf-8', 'strict')
#print(henk.decode('utf-8', 'strict'))
