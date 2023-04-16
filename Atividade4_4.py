n1, n2, n3 = float(input('Digite primeiro valor: ')), float(input ('Digite o segundo valor: ')), float(input ('Digite o terceiro valor: '))

if (n1 + n2 > n3 and n2 + n3 > n1 and n1 + n3 > n2):
    print ('Os valores formam um triângulo.')
else:
    print ('Os valores NÃO formam um triângulo.')
