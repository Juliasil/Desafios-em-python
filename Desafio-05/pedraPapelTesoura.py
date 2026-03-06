import random

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

game_images = [pedra, papel, tesoura]

user_choice = int(input('Qual opção você deseja? (0) Pedra, (1) Papel ou (2) Tesoura: '))

if user_choice >= 3 or user_choice < 0:
    print("Você digitou uma opção inválida")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0,2)
    print("Computador escolheu:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("Você ganhou")
    elif computer_choice == 0 and user_choice == 2:
        print("Você perdeu")
    elif computer_choice > user_choice:
        print("Você perdeu")
    elif user_choice > computer_choice:
        print("Você ganhou")
    else:
        print("Empate")
    

    