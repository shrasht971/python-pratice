                                            ##NUMBER TOPIC##
"""The interpreter acts as a simple caculator:you can type an expression at it and it will write the value.
 Expression syntax is straightforward: the operators +, -, * and / can be used to perform arithmetic; parentheses (()) can be used for grouping"""
print(2 + 2)
print(50 - 5*6)
print((50-5*6)/4)
print(8/5)           #classic division(/) always returns a floating number{output-1.6}
print(17//3)         #floor division discards the fractional part{output-5}
print(17%3)          #The % operator returns the remainder of the division{output-2}
print(5**2)          #5 squared{output-25}
print(2**8)          #2 to the power of 7{output-256}


##The equal sign (=) is used to assign a value to a variable.Afterwards, np result is displayed before the next interactive prompt:##
width = 20
height= 5
print(width*height)      #output is 100

##full support for floating point; operators with mixed type operands to floating point:
print(4*3.75-1)

print('doesn\'t')          #use \' to escape the single quote or use double quotes instead

word = 'Python'
print(word[0])               #character in position 0
print(word[-4])              #character fourth-last characer
print(word[1:4])             #characters from position 1(included) to 4(excluded)
print(word[:8])              #characters from the beginning to position 8(excluded)
print(word[2:])              #characters from position 2(included) to  the end


