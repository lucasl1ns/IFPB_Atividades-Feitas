x, y = float(input('X: ')), float(input('Y: '))
if x == 0 and y == 0:
    print ('ORIGEM')
elif x == 0 and (y != 0 ):
    print ('EIXO Y')
elif y == 0 and (x != 0 ):
    print ('EIXO X')
elif x > 0 and y > 0:
    print ('Q1')
elif x < 0 and y > 0:
    print ('Q2')
elif x < 0 and y < 0:
    print ('Q3')
else:
    print ('Q4')
