def calcular_notas_saque(cash):
    notas_50 = cash // 50
    cash -= notas_50 * 50 # ou eu posso usar cash %= 50

    notas_20 = cash // 20
    cash -= notas_20 * 20 # ou eu posso usar cash %= 20

    notas_10 = cash // 10
    cash -= notas_10 * 10 # ou eu posso usar cash %= 10

    notas_1 = cash // 1

    return notas_50, notas_20, notas_10, notas_1


def imprimir_notas(notas_50, notas_20, notas_10, notas_1):
    print(f"Notas de R$50: {notas_50}")
    print(f"Notas de R$20: {notas_20}")
    print(f"Notas de R$10: {notas_10}")
    print(f"Notas de R$1: {notas_1}")



