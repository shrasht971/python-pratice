                                        ##LIST#
# LIST are just like dynamically sized arrays, a list is a collection of things,
#encolsed in [] and separated by commas.

# var = ["What", "you", "Want?"]
# print(var)

index=[1,2,4,7,6,8,9]
# # print(index)                  #List returns
# # print(index[0])               #indexing returns the item
# # print(index[-1])              #indexing returns first-last items
# # print(index[-3:])             #slicing returns a new list
# # print(index[:-1])            

# #Lists also support operations 
# addList =index+[36,49,64,81,90]
# # print(addList)
# addList.append(216)             #append() method Adds an element at the end of the list
# print(addList)

# index.insert(2,3)                 #The insert() method iserts the specified value at the specified position
# print(index)                      #SYNTAX: list.insert(pos,elmnt)

index1=[2,5,6,7]                    #add second index1 in index position in 0
# index.insert(0,index1)
# print(index)

# index.extend(index1)                #Add the elements of a list (or any iterable), to the end of the current list
# print(index)                        #SYNTAX:list.extend(iterable)
 
# index.remove(2)                     #Removes the first item with the specified value
# print(index)                        #SYNTAX:list.remove(elmnt)

# popped=index.pop()                  #The pop() method removes the element at the specified position.
# print(index)                        #SYNTAX:list.pop(pos)

# index.reverse()                     #The reverse() method reverses the sorting order of the elements.
# print(index)                        #SYNTAX:list.reverse()

index.sort()                          #List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
print(index)

index.sort(reverse = True)            #To sort descending, use the keyword argument-> reverse = True
print(index)

print(min(index))                     #returns the minimum number
print(max(index))                     #returns the maximum number
print(sum(index))                     #sum() method total the sum of element

 


