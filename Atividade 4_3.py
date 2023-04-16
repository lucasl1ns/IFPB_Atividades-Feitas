#VARIÁVEIS
dia, mes, ano = int(input('Digite o dia do seu nascimento: ')), int(input('Digite o mês do seu nascimento: ')), int(input('Digite o ano do seu nascimento: '))
dia_ref = int(30)
mes_ref = int(3)
ano_ref = int(2023)
sub_ano = ano_ref - ano

#TESTES E RESULTADOS
if (mes < mes_ref) or (mes == mes_ref and dia <= dia_ref):
    print ('A idade é:', sub_ano)
else:
    print ('A idade é:', sub_ano - 1)
