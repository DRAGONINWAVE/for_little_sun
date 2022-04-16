fruits = ['strawberry','fig','apple','cherry','raspberry','banana']
print(sorted(fruits,key=len)) #['fig', 'apple', 'cherry', 'banana', 'raspberry', 'strawberry']


def reverse(word):
    return word[::-1]

print(reverse('testing')) #gnitset

print(sorted(fruits,key=reverse)) #['banana', 'apple', 'fig', 'raspberry', 'strawberry', 'cherry']  it's funny hah?!
