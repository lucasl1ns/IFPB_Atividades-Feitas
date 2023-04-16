#COLETA DE INFORMAÇÕES
produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: R$"))

#CÁLCULO DE DESCONTO E PREÇO FINAL
desconto = 0.2 * preco
precofinal = 0.8 * preco

#RESULTADOS A EXIBIR
print ("\nPreço R$:{:.2f}".format(preco))
print ("Desconto R$:{:.2f}\n".format(desconto))

#TEXTO PARA O CLIENTE
print ("O produto", produto, end="")
print (" recebe desconto de R${:.2f}".format(desconto), end = "")
print (" e custará R${:.2f}".format(precofinal))
