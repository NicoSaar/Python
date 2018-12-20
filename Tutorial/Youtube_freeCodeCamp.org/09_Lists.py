lucky_numbers = [3, 6 , 16 , 23 , 27, 42]
friends = ["Pascal", "Laura", "Sascha", "Elle", "Steff"]
############# 0         1        2        3       4
#access list items
print(friends[1])
print(friends[-1])
print(friends[1:])
print(friends[1:3])

## modify
friends[3] = "Matze"
print(friends[3])


##functions


friends.extend(lucky_numbers)   #extend function adds items at the end of the list
print(friends)

friends.insert(1, "NewItem")  #insert adds items at index position
print(friends)

friends.remove("Steff") #remove deletes items from list
print(friends)

friends.pop() #removes last item from list
print(friends)

print(friends.index("Laura"))  #returns index of spesific list item

### more functions
# count -> returns count of specific list item
# sort -> sort list in alphabetical/ ascending order
# reverse -> returns lists in reverse order
# copy -> creates another list as a copy 

