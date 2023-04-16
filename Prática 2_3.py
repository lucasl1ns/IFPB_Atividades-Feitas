renda = float(input('Digite sua renda: R$'))
if (renda >= 0 and renda <= 1903.98):
    aliq = 0
    deducao = 0
    imposto = aliq * renda - deducao
    print ('Renda mensal de R$', renda,', indice de alíquota de 0% e o imposto a ser pago é de R$', imposto) 
if (renda >= 1903.99 and renda <= 2826.65):
    aliq = 7.5/100
    deducao = 142.8
    imposto = aliq * renda - deducao
    print ('Renda mensal de R$', renda,', indice de alíquota de 7,5% e o imposto a ser pago é de R$', imposto) 
if (renda >= 2826.66 and renda <= 3751.05):
    aliq = 15/100
    deducao = 354.8
    imposto = aliq * renda - deducao
    print ('Renda mensal de R$', renda,', indice de alíquota de 15% e o imposto a ser pago é de R$', imposto) 
if (renda >= 3751.06 and renda <= 4664.68):
    aliq = 22.5/100
    deducao = 636.13
    imposto = aliq * renda - deducao
    print ('Renda mensal de R$', renda,', indice de alíquota de 22,5% e o imposto a ser pago é de R$', imposto) 
if (renda > 4664.68):
    aliq = 27.5/100
    deducao = 869.36
    imposto = aliq * renda - deducao
    print ('Renda mensal de R$', renda,', indice de alíquota de 27,5% e o imposto a ser pago é de R$', imposto) 

    
