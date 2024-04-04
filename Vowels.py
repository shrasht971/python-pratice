def vowel(ch):  #user define function
    Switcher = {
        'a':"Vowel",
        'e':"Vowel",
        'i':"Vowel",
        'o':"Vowel",
        'u':"Vowel",
        'A':"Vowel",
        'E':"Vowel",
        'I':"Vowel",
        'O':"Vowel",
        'U':"Vowel",
    }
    return Switcher.get(ch,"not vowel")

    #input from user
ch=input("enter the character:")

    #calling the function and display the result
print(ch,'is a'+vowel(ch))