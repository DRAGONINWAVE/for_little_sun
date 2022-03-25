fruits = ['apple', 'orange','banana','grape','lemon']
print(sorted(fruits)) #sorted() can't sort the list
print(fruits)
print(fruits.sort(reverse=True,key=len,)) #.sort() can sort it
print(fruits)