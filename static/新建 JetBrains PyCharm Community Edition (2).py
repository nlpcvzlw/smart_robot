a = '2)(1+2+)'
b = None
for i in a:

    if b != None:
        if i == ')':
            b -= 1

        if i == '(':
            b += 1
    else:
        if i == '(':
            b = 1

print(b == 0)

