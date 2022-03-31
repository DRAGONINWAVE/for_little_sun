import haystack as haystack

i = ['spam', 'spam','spam','spam','spam','dragon','dragon','dragon','dragon']
print(set(i))
print(list(set(i)))
print(dict.fromkeys(i).keys())


# found = len(needles & haystck)
#first way
found = 0
for n in 'needles':
    if n in 'haystck':
        found += 1
print(found)

#second way
found = len(set('needles') & set('haystack'))
print(found)

#third way
found = len(set('needles').intersection('haystack'))
print(found)

print(frozenset(range(10)))

from unicodedata import name
print({chr(i) for i in range(32,256) if 'SIGN' in name(chr(i),'')})