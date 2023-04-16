num = int (input('Digite um número: '))
div = 0
somadiv = 0
fat = 1

#QUANTIDADE DE NÚMEROS INTEIROS
print ('Os inteiros do intervalo [ 1,', num,']', 'são:')
for i in range (1, num + 1):
    print (i)
    
print()

#DIVISORES DO NÚMERO
print ('Os divisores inteiros desse número são: ')
for i in range (1, num + 1):
    fat = i * fat
    if (num % i) == 0:
        div = div + 1
        somadiv = somadiv + i
        print (i)
somadiv = somadiv - num
#print ('A soma dos divisores, excluindo o número digitado é:', i)

print ()

#NÚMERO É PRIMO?
#print ('O número tem,',div, 'divisores.')
if div == 2:
    print ('Este número é primo.')
else:
    print ('Este número não é primo.')

print ()

#NÚMERO É PERFEITO?
if somadiv == num:
    print ('Este número é perfeito.')
else:
    print ('Este número não é perfeito.')

print()

#FATORIAL
print ('O fatorial é:', fat)
