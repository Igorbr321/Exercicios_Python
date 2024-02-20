from teste_funcoes import calcular_notas_saque, imprimir_notas

print('==' * 25)
print('{:^45}'.format('BANCO CEV'))
print('==' * 25)

cash = int(input('What amount do you want to withdraw? R$'))

notas_50, notas_20, notas_10, notas_1 = calcular_notas_saque(cash)
imprimir_notas(notas_50, notas_20, notas_10, notas_1)

