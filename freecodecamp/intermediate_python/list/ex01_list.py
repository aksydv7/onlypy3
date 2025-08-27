
mylist = ["banana", "cherry", "apple"]
# print(mylist)

# print the list one by one
for i in mylist:
    print(i)


# checking the elements in the list
if "apple" in mylist:
    print("Present")
else:
    print("Not present")

# list methods
mylist.append("lemon")
print("New List: ", mylist)

# insert at the specific place
mylist.insert(1, "grapes")
print("insert new fruite: ", mylist)

# remove the element from the list

mylist.remove("cherry")
print(mylist)

# clear the list

# mylist.clear()

# print(mylist)

# reverse the list

rev_list = mylist.reverse()
print(mylist, rev_list)