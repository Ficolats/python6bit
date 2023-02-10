normaldict={
    " ": "111111",
    "a": "111110",
    "b": "111100",
    "c": "111101",
    "d": "111000",
    "e": "111011",
    "f": "111001",
    "g": "110111",
    "h": "110011",
    "i": "110001",
    "j": "110101",
    "k": "110000",
    "l": "110010",
    "m": "110110",
    "n": "110100",
    "o": "111010",
    "p": "100000",
    "q": "100001",
    "r": "100011",
    "s": "100010",
    "t": "100101",
    "u": "100111",
    "v": "100100",
    "w": "101011",
    "x": "011111",
    "y": "011110",
    "z": "011100",
    "0": "000111",
    "1": "010101",
    "2": "000000",
    "3": "000110",
    "4": "001010",
    "5": "011101",
    "6": "001100",
    "7": "010011",
    "8": "001110",
    "9": "010001",
    ",": "101000",
    ".": "000010",
    ";": "000001",
    ":": "011000"
}
#defining standard variables
keys=list(normaldict.keys())
values, oldvalues=list(normaldict.values()),list(normaldict.values())
output=str("")

def makenewdict():
    #make random integer to create a new dict
    import random
    randomint=random.randint(1, len(normaldict))
    for i in range(1, randomint+1):
        values.insert(-1, values[0])
        values.pop(0)
    newdict = dict(map(lambda i,j : (i,j) , keys,values))
    return newdict


def encrypt():
    x=input("Input for encryption: ")
    x.lower()
    
    newdict=makenewdict()
    #loop through the input and encode it
    for i in x:
        global output
        output=str(output)+str(newdict.get(i))
    #add an a to output to identify dict for decryption
    output=str(newdict.get("a"))+output
    return output


def splitsix(x):
    length = 6
    x=[x[i:i+length] for i in range(0, len(x), length)]
    return x
    
    
def decrypt():
    decryptmsg=input("Input for decryption: ")
    #split input every 6 chars
    splitmsg=splitsix(decryptmsg)
    newa=list(normaldict.keys())[list(normaldict.values()).index(splitmsg[0])]
    splitmsg.pop(0)
    diff=keys.index("a")-keys.index(newa)
    #find the dict that was used to encrypt
    for i in range(1, abs(diff)+1):
        oldvalues.insert(-1, oldvalues[0])
        oldvalues.pop(0)
    solutiondict=dict(map(lambda i,j : (i,j) , keys,oldvalues))
    for i in splitmsg:
        global output
        output=str(output)+list(solutiondict.keys())[list(solutiondict.values()).index(i)]
    return str(output)

enorde=input("1 for encrypt, 2 for decrypt: ")
if enorde=="1":
    print(encrypt())
elif enorde=="2": 
   print(decrypt())
