my_list=[]

#Adding items to  my empty list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)


print(my_list)

#inserting 15 at the second position of my list
my_list.insert(1, 15)

print(my_list)

#Creating another list and merging both by extending
my_list2=[50, 60, 70]
my_list.extend(my_list2)

print(my_list)

#Removing the last element in my list
my_list.remove(70)
print(my_list)

#sorting the list in ascending order
my_list.sort()
print(my_list)

#Finding and printing 30 in the list
index= my_list.index(30)
print(f"30 is at {index}")
