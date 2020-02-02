x = input().split("print(")
b = list(x[-1])
    a = []
for x in b[0]: a.append(x)
a.pop()
x = "".join(a)
print(eval(x))