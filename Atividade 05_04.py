qtap = 0
qtfinal = 0
qtrep = 0

print ('Digite as 40 notas em sequência:')

for i in range (1,41):
    nota = int (input(''))

    if nota >= 0 and nota <= 100:
        if nota >= 70 and nota <= 100:
           qtap = qtap + 1
        elif nota >= 40:
            qtfinal = qtfinal + 1
        else:
            qtrep = qtrep + 1
    else:
        print ('Nota inválida.')

print('Alunos aprovados:', qtap)
print('Alunos na final:', qtfinal)
print('Alunos reprovados:', qtrep)



           
        
            
