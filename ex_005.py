import matplotlib.pyplot as plt
def extrair_dados(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        arquivo = open(caminho_arquivo, encoding='utf8')
        conteudo = arquivo.read()

    anos = []

    conteudo = conteudo.splitlines()

    paises = conteudo[0]
    paises = paises.split(',')


    conteudo = conteudo[1:]

    dados = []

    for elemento in conteudo:
        elemento = elemento.split(',')
        dados.append(elemento)


    for i in range(8):
        anos.append(dados[i][0])

    return paises, dados, anos


extrair_dados('Assessment_PIBs - modelo 2.csv')

def pib_pais(pais, ano):
    paises, dados, anos = extrair_dados('Assessment_PIBs - modelo 2.csv')
    if pais not in paises:
        print("País não diponível :c")
        exit()
    if ano not in anos:
        print("Ano não disponível :c")
        exit()
    indice_pais = paises.index(pais)
    indice_ano = anos.index(ano)

    print(f"PIB {pais} em {ano}: US${dados[indice_ano][indice_pais]} trilhões.")

def estimativa_pib():
    paises, dados, anos = extrair_dados('Assessment_PIBs - modelo 2.csv')
    cont = 1
    for i in paises[1:]:
        primeiro_pib = float(dados[0][cont])
        segundo_pib = float(dados[7][cont])
        cont = cont + 1
        calculo_variacao = (segundo_pib/primeiro_pib - 1) * 100
        print(f"{i} Variação de {calculo_variacao:.2f}% entre 2013 e 2020.")

def plotar_grafico(pais):
    paises, dados, anos = extrair_dados('Assessment_PIBs - modelo 2.csv')
    listar_pibs = []
    indice = paises.index(pais)
    for i in range(8):
        listar_pibs.append(float(dados[i][indice]))
    plt.title(pais)
    plt.xlabel("Anos")
    plt.ylabel("PIB")
    plt.plot(anos, listar_pibs)
    plt.show()



# pais = input("Informe um País: ")
# ano = input("Informe um ano entre 2013 e 2020: ")
# pib_pais(pais, ano)


print("1- Mostrar PIB de um pais em um ano em específico.")
print("2- Listar estimativa da variação do PIB dos Países.")
print("3- Mostrar gráfico da evolução do PIB de um País.")
alternativa = input("Digite uma opção: ")


if alternativa == "1":
    pais = input("Informe um país: " )
    ano = input("Informer um ano entre 2013 e 2020: ")
    pib_pais(pais, ano)


elif alternativa == "2":
    estimativa_pib()

elif alternativa == "3":
    pais = input("Digite o nome do país: ")
    plotar_grafico(pais)

else:
    print("Opção inexistente")
    exit()
