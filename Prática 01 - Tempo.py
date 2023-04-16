hora = float(input ("Digite o tempo em hora(s): "))
minuto = float(input ("Digite o tempo em minuto(s): "))
segundo = float(input ("Digite o tempo em segundo (s): "))

tempo_segundos = float(hora*60*60 + minuto*60 + segundo)

print ("O tempo total em segundos é: ", tempo_segundos)
input()
