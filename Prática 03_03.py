a, b, c = int(input('Primeiro valor: ')), int(input('Segundo valor: ')), int(input('Terceiro valor: '))
if a > b and a > c:
    if b > c:
        print(c, b, a, sep = '\n')
        print()
        print(a, b, c, sep = '\n')
    else:
        print(b, c, a, sep = '\n')
        print()
        print(a, b, c, sep = '\n')
if b > a and b > c:
    if a > c:
        print(c, a, b, sep = '\n')
        print()
        print(a, b, c, sep = '\n')
    else:
        print(a, c, b, sep = '\n')
        print()
        print(a, b, c, sep = '\n')
else:
    if a > b:
        print (b, a, c, sep = '\n')
        print()
        print(a, b, c, sep = '\n')
    else:
        print (a, b, c, sep = '\n')
        print()
        print(a, b, c, sep = '\n')                                  
