nome = input ('Nome: ')
salario = float (input('Salário: R$'))
vendas = float (input('Total de vendas: R$'))
perc = 15/100
total = salario + perc * vendas
'''
print ('TOTAL = R${:.2f}'.format(total))
'''

print (f'TOTAL = R${total:.2f}')
