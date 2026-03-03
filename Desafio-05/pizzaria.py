print('Bem-vindo(a) Pizzaria!')

pedido = input('Qual será o tamanho da pizza? Pequena (P), Médio (M), Grande (L)')
pepperoni = input('Você quer Pepperoni? Sim(S) ou Não(N):')
adicional = input('Deseja queijo extra? Sim(s) ou Não(n): ')

conta = 0


if pedido == 'p':
    conta += 15
elif pedido == 'm':
    conta += 20
elif pedido == 'l':
    conta += 25
else:
    print('Seleção de campo inválida')

if pepperoni == 's':
    if pedido == 'p':
        conta += 2
    else:
        conta += 3
    
if adicional == 's':
    conta += 1

        
print(f'O seu pedido final é R${conta} Reais')