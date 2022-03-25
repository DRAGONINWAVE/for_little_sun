from array import array
octset = array('B',range(6))
m1 = memoryview(octset) #export the memory
m2 = m1.cast('B',[2,3]) #export the octset and cast 2 rows and 3 columns
m2.tolist() #m2 to be listed
print(m2.tolist())
m2[1,1] = 233
print(octset.tolist())  #all changes are for octset