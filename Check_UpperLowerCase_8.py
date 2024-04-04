#accept a character and display whether it is upper case or lower case or not an alphabet.
ch=input("Enter the character:")

if ch>='A' and ch<='Z':
    print("Upper case")
elif ch>='a' and ch<='z':
    print("Lower case")
else:
    print("not an alphabet")
