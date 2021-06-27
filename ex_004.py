import matplotlib.pyplot as plt

valor_inicial = float(input("Digite o valor inicial em R$: "))
rendimento = float(input("Digite o rendimento mensal em (%): "))
aporte_mensal = float(input("Digite o aporte mensal R$: "))
total_meses = int(input("Digite a quantidade de meses: "))

print(f"Valor inicial: R${valor_inicial}")
print(f"Rendimento por período: R${rendimento}%")
print(f"Aporte a cada período: R${aporte_mensal}")
print(f"Total de períodos: {total_meses}")


def rendimento_total(valor_inicial, rendimento, aporte_mensal, total_meses):

    porcentagem = rendimento / 100
    saldo = valor_inicial
    valor_acumulado = []
    montante_meses = []



    for mes in range(total_meses):
        resultado_juros = saldo * porcentagem
        saldo = saldo + resultado_juros + aporte_mensal

        print(f"No {mes + 1} mes o seu saldo será de: R${saldo:.2f}")
        valor_acumulado.append(saldo)
        montante_meses.append(mes)


    x = montante_meses
    y = valor_acumulado
    plt.xlabel("Meses")
    plt.ylabel("Valor")
    plt.plot(x,y)
    plt.show()

rendimento_total(valor_inicial, rendimento, aporte_mensal, total_meses)






