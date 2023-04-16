#INTERAÇÕES COM USUÁRIO
print("Para utilização deste programa, escolha dois números aleatórios e maiores que zero")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

#OPERAÇÕES 
soma = n1 + n2
subtracao = n1 - n2
produto = n1 * n2
divisãor = n1 / n2
divisaoint = int (n1 // n2)
resto = n1 % n2
potencia = n1 ** n2

#RESULTADOS A EXIBIR
print("A soma dos dois números é:", soma)
print("A subtração dos dois números (1° - 2°) é:", subtracao)
print("A multiplicação dos dois números é:", produto)
print("A divisão real dos dois números (1° / 2°) é:", divisãor)
print("A divisão inteira truncada dos dois números é:", divisaoint)
print("O resto da divisão (1° / 2°) entre os dois números é:", resto)
print("A potência do 1° elevado ao 2° é:", potencia)
