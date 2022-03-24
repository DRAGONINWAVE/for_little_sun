import dis

a = (1,2,[20,30])
print(id(a))
# a[2] +=  [40,50] False
a[2].append(40)
print(a)
print(id(a))
b = a[2] + [40,50]
print(b)
print(id(b))

print(dis.dis('s[a] += b')) #show how the expression happens