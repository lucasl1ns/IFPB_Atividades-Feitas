ano = int(input('Digite o ano:'))
rest400 = ano % 400
rest4 = ano % 4
rest100 = ano % 100
if (rest400 == 0):
    print ('O ano é bissexto')
else:
    if (rest4 == 0) and (rest100 != 0):
        print ('O ano é bissexto')
    else:
        print ('O ano não e bissexto')
        
