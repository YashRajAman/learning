# data types
# int/float/str
# list/tuple/dictionary

x = [1,2,3,"Sandwip",1.5]

y = (1,2,3,"Sandwip",1.5)

z = {"key":"value", 1:"Myname"}

print(z["key"])
x[1] = 1212
print(x[1])

# var = input("Input a number")

# print(int(var))

print(type(y))

# for x in range(1,6, 2):
#     print(x)

print(x[1:4:2])

# while x:
#     print(x)
#     x.pop(0)

if len(x) > 0:
    print("hola")
else:
    print("no hola")