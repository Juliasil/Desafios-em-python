print('Bem-vindo(a) à Ilha do Tesouro.')
print('Sua missão é encontrar o tesouro.')

print('''  
                 __________
            /\____;;___\
           | /         /
           `. ())oo() .
            |\(%()*^^()^\
           %| |-%-------|
          % \ | %  ))   |
          %  \|%________|
    ejm97  %%%%  
    ''')

choice1 = input('''Você está em uma encruzilhada, para onde você deseja ir? Digite "esquerda" ou "direita".''').lower()
if choice1 == 'esquerda':    
    choice2 = input('você deseja nadar ou esperar?').lower()
    if choice2 == 'nadar':
        choice3 = input('Qual porta desja abrir: vermelha, Amarelo, Azul').lower()
    if choice3 == 'vermelha':
        print('Gamer Over')
    elif choice3 == 'amarelo':
        print('Parabéns você achou o tesouro')
    elif choice3 == 'azul':
        print('codigo por feras')
    else:
        print('Você escolheu uma alternativa que não existe')
else:
    print('Game Over')