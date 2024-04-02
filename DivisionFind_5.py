# accept marks from the user. Using if…….elif….  Else,  display whether result is  fail, pass, second class , first class, Distinction etc.
marks=float(input("Enter the Marks:"))
if marks < 35:
    print("Fail")
elif marks <= 50:
    print("Pass")
elif marks <=60:
    print("Second class")
elif marks <=75:
    print("First class")
else:
    print("Distinction")