print('=============Calculadora IMC=============')

weight = float(input('Qual é o seu peso? '))
height = float(input('Qual é a sua altura? '))

bmi = weight /(height ** 2)
if bmi < 18.5:
    print('Abaixo do peso')
elif bmi >= 18.5 and bmi < 25:
    print('Peso normal')

else:
    print('Acima do peso')