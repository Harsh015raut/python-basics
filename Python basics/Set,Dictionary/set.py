a = {1,3,5,7,8,1}
print(type(a))
print(a)

#Empty Dict

c = {}
print(type(c))

#Creating Empty Set

b = set()
print(type(b))

#SET METHODS

#Adding values in set
b.add(4)
b.add(7)
b.add(5)
b.add(4)
b.add((6,2,3,4,5,7,9))
#Dictionary or list cannot be added to sets
#Hashable-not changing,hashable objects cannot be added to set
print(b)

print(len(b)) #Prints the length of this set

b.remove(5) #Removes element from set
print(b)
#b.remove(15) #Throws an error while trying to remove 15(Which is not present in the set)
print(b)
print(b.pop())#Removes a random value from set
print(b)




b.clear() #Empties set


