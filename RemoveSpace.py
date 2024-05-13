class RemoveSpace:
    def modify(self, s):
        # Input string
        print("original string: ",s)
        print(s)
        # Count no. of spaces in a string
        space=s.count(" ")
        # replace all the space
        for i in range(space):
            s=s.replace(" ","")
        print("Removing space in string: ")
        print(s)

remover = RemoveSpace()
remover.modify("geeks for geeks")

