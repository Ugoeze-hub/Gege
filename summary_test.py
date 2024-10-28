a_list = [1,2]
for v in range(2):
    a_list.insert(-1, a_list[v])
print(a_list)

lst = [i for i in range(-1, -2)]
print(len(lst))

for i in range(-1, -2):
    print(i)
    

tup = (1,2,4,8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)

x = 1
y = 2
x,y,z = x,x,y
print(x,y,z)
z,y,z = x,y,z 
print(x,y,z)

dd = {'1':'0', '0':'1'}
for x in dd.vals():
    print(x, end='')