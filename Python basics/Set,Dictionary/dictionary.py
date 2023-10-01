a = {"data ":"Information,facts or figures",
     "internet":"Network of Network",
     "marks":[1,2,3],
     "anotherdict":{"harsh":"data scientist"}
     }
print(a)
print(a["internet"])#-> prints Value
print(a["anotherdict"]["harsh"])

#changing values in dictionary
a["marks"] = [34,56] 
print(a.keys()) #-> returns keys
print(type(a.keys()))
print(a.values())#->Returns value
print(a.items()) #Returns all keys,value of dictionary in form of tuple

update_dict = {
    "H1":"Friend"
}
a.update(update_dict) #Updates dictionary by adding key,value pairs from updateDict
print(a)
print(a.get("H1")) #Imp .get method return none if the key is not present,aslo prints value associated with h1




