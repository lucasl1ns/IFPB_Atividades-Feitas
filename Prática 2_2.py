a, b, c = float(input('Digite a primeira nota: ')), float (input('Digite a segunda nota: ')), float (input('Digite a terceira nota: '))
ponderada = (a * 4 + b * 6 + c * 8) / 18
aritmetica = (a + b + c) / 3
print('Ponderada:',ponderada,'Aritmética:',aritmetica)
if (ponderada > aritmetica):
    print('Melhor opção é a média ponderada')
elif (ponderada == aritmetica):
    print ('Tanto faz')
else:
    print ('Melhor opção é a média aritmética')
    

                                                                                              
                            


                                                                                              
                                            
