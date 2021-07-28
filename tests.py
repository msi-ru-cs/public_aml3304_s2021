a = 2
b = 3
c = a + b

if (c >= 5):
    c = c + 1
    # Swap the values of a and b
    a = a + b
    b = a - b
    a = a - b
else:
    c = c + 10
    temp = a
    a = b
    b = temp
    