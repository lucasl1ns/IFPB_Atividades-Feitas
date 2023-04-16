nome = input ("Nome do vendedor: ")
qtd_vendas = int(input ("Quantidade de veículos vendidos: "))
valor_vendas = float (input ("Digite o total vendido no mês: R$"))

salario_base = float(1000)
comissao = float(200)
comissao_percentual = 0.05
salario = salario_base + comissao * qtd_vendas + comissao_percentual*valor_vendas

print ("O salário final do vendedor é: R$", float(salario))

'''
print(f'Salário final: R$ {salario: .2f'}
'''
