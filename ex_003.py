renda_mensal = float(input("Digite aqui o total de sua renda mensal: "))
moradia = float(input("Digite quanto você gasta com moradia: "))
educacao = float(input("Digite quanto você gasta com educação: "))
transporte = float(input("Digite o quanto você gasta com transporte: "))

def diagnostico_renda(renda_mensal, moradia, educacao, transporte):
    max_renda_moradia = renda_mensal * 0.3
    max_renda_educacao = renda_mensal * 0.2
    max_renda_transporte = renda_mensal * 0.15
    moradia_porcento = (moradia * 100) / renda_mensal
    educacao_porcento = (educacao * 100) / renda_mensal
    transporte_porcento = (transporte * 100) / renda_mensal

    if moradia <= max_renda_moradia:
        print("Sua gastos totais com moradia comprometem {:.2f}% da sua renda total, o máximo recomendado é de 30%. Seus gastos estão dentro da margem recomendada. O total dos 30% baseado no seu salário é de R${}".format(moradia_porcento, max_renda_moradia))
    else:
        print("Sua gastos totais com moradia compromente {:.2f}% de sua renda total, o máximo recomendado é de 30%. Seus gastos estão fora da margem recomendada. O total dos 30% baseado no seu salário é de R${}".format(moradia_porcento, max_renda_moradia))

    if educacao <= max_renda_educacao:
        print("Seus gastos totais com educação comprometem {:.2f}% da sua renda total. O máximo recomendado é de 20%. Seus gastos estão dentro da margem recomendada. O total dos 20% baseado no seu salário é de R${} " .format(educacao_porcento, max_renda_educacao))
    else:
        print("Seus gastos totais com educação comprometem {:.2f}% da sua renda total. O máximo recomendado é de 20%. Seus gastos estão fora da margem recomendada. O total dos 20% baseado no seu salário é de R${} " .format(educacao_porcento, max_renda_educacao))
    if transporte <= max_renda_transporte:
        print("Seus gastos totais com transporte comprometem {:.2f}% da sua renda total. O máximo recomendado é de 15%. Seus gastos estão dentro da margem recomendada. O total dos 15% baseado no seu salário é de R${} " .format(transporte_porcento, max_renda_transporte))
    else:
        print("Seus gastos totais com transporte comprometem {:.2f}% da sua renda total. O máximo recomendado é de 15%. Seus gastos estão fora da margem recomendada. O total dos 15% baseado no seu salário é de R${} " .format(transporte_porcento, max_renda_transporte))

print(diagnostico_renda(renda_mensal, moradia, educacao, transporte))