n = int (input ('Digite o número para verificar os múltiplos: '))
x = int (input ('Digite o primeiro valor do intervalo: '))
y = int (input ('Digite o segundo valor do intervalo: '))

for i in range (x, y, n):
    if i % n == 0 and i != 0:
        print (i)
