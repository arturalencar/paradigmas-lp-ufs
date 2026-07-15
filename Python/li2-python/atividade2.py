x = 0

def p(y):
    global x
    x += y

def bloco():
    x = 1
    p(3)
    print(x)

bloco()

p(4)
print(x)