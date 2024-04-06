                                        ##STRINGS TOPIC##
message = 'Hello World'
print(message.lower())         #All character are convert into lower letter
print(message.upper())         #All character convert into upper case
print(len(message))            #The len() function returns the length of a string

txt="The best things in life are free!"     #CHECK STRING {To check if a certain phrase or character is present in a string,we can use the keyword in.}
print("free" in txt)


if "free" in txt:
    print("Yes, 'free' is present.")       #    Use it in an if statement  #


print("expensive" not in txt)               #CHECK IF NOT{To check if a certain phrase or character is NOT present in a string,we can use the keyword not in.}

if "expensive" not in txt:
    print("Yes, 'expensive' is not present")

print(txt.find('best'))             #Find method find a string of characters that doesn't exist then it will just return negative one(-1)
# or
print(txt.find('world'))

x=txt.replace("free","busy")          #replace() method replace all the  occurrences of the old substring with the new substring. 
print(x)


##format() method formats the specified value and insert them inside the string's placeholder.
##The placeholder iss defined using curly brackets: {}, The format() method returns the formatted string.
##1>syntax:{}.format(value)  2>syntax:{} {}.format(value1,value2)

greeting ='Hello'
name ='Shri!'
result = '{}, {}. Welcome!'.format(greeting, name)
print(result)

result = f'{greeting}, {name.upper()}.Welcome!'
print(result)                                     # An f-string in Python is a concise and efficient way to format strings by embedding expressions and variables directly within the string literals, prefixed with f.