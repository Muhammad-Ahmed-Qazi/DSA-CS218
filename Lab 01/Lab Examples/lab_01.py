a = 10
b = 10
c = 10
print(id(a), id(b), id(c))

a += 1
print(id(a))

x = 1000
y = 1000
print(id(x), id(y)) # Once addresses were different, but mostly same

s1 = "hello"
s2 = "hello"
print(id(s1), id(s2))

s3 = "hello, world!"
s4 = "hello, world!"
print(id(s3), id(s4)) # Once addresses were different (for 'hello, world!'), but mostly same