print('Seja bem-vindo(a) a APP Gorjeta!')

account = float(input('Imforme o valor da conta: R$ '))

percentage = int(input('Que porcentagem de gorjeta você gostaria de dar? 10%, 12% ou 15%? '))

people = int(input('Quantas pessoas vão pagar a conta? '))

accountWithTip = percentage / 100 * account + account

totalvalue = accountWithTip /people

print(f'Cada pessoa deve pagar: R$ {totalvalue:.2f}')

