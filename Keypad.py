from collections import OrderedDict
import sys

print("\n\n_________________________________Keypad Cipher_________________________________\n")
print("Note: There may be different amount of spaces between characters based on the input.\n")
print("Example : 222 444 7 44 33 777 \t-> c  i  p  h  e  r")
print("\t: 22244474433777 \t-> cipher")
print("\t: 222-444-7-44-33-777 \t-> c- i- p- h- e- r\n")
print("Note: When a character in the same key repeats more than once consecutively,\n Leave a non-digit character in between.\n")
print("Example : 9999-666-666 \t-> z- o- o\n")
print("Enter 'e' to exit\n\n")


mat = [[],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]

while(1):
    print("Enter keypad number : " ,end ="")
    text = str(input())
    if(text == 'e'):
        sys.exit()
    i = 0
    while(i < len(text)-1):
        if(text[i] != text[i+1]):
            text = text[:i+1] + ' ' + text[i+1:]
            i = i + 1
        i = i + 1

    text = text.split(" ")
    for n in text:
        if(not n.isdigit()):
            print (n,end =" ")
        else:
            print (mat[int("".join(OrderedDict.fromkeys(n)))-1][len(n)-1], end ="")

    print("\n")
