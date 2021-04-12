#--------------------------------------------------------------------------
#------------------------------ AT QUESTÃO 5 ------------------------------
#--------------------------------------------------------------------------

# ALIAS plt para a biblioteca usada
import matplotlib.pyplot as plt

# Função retirada do site "https://pt.stackoverflow.com/questions/66183/como-retornar-um-valor-no-formato-moeda-brasileiro-na-view-do-django"
# Função que recebe um valor
# Formata no valor americano (variavel a)
# Formata no valor brasileiro (variavel b, c e d)
# Independente do tamanho do número, troca as virgulas, quando existirem, por "v".
# Em seguida troca o ponto pela virgula.
# E caso exista a troca de de virgula por "v", troca todos os "v" por ponto.

def formatar_moeda(valor):
    a = '{:,.2f}'.format(float(valor))
    b = a.replace(',','v')
    c = b.replace('.',',')
    return c.replace('v','.')

def gera_matriz():
    # Abre o arquivo
    arquivo = open("Assessment_PIB.csv","r",encoding="utf8")
    # Variavel conteudo lê o arquivo todo
    cont_arq = arquivo.read()
    # Fecha o arquivo
    arquivo.close()
    # Divide conteudo em uma lista (Vetor)
    cont_arq = cont_arq.splitlines()
    # Cria uma lista nova (Matriz)
    matriz_pib = []
    for i in cont_arq:
        i = i.split(',')
        matriz_pib.append(i)
    return matriz_pib

def pib_pais_ano():
    print("\n" * 130)
    print("-------------------------------------------------------------------------------------------------------------------")
    print("------------------------------------------ PRODUTO INTERNO BRUTO DE UM PAÍS ---------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------------")
    # Gera a matriz
    matriz_pib = gera_matriz()
    # Imprime o nome dos países para escolha.
    paises = "Países: "
    # Imprime o nome dos países para escolha.
    for i in range(len(matriz_pib)-1):
        paises = paises + matriz_pib[i+1][0] + " | "
    
    print(paises)
    print("")
    # Pede para entrar com o país.
    pais = str(input("Dentre os países acima, escolha um para mostrar o seu PIB (em trilhões de US$): "))
    # Verifica se o país está na lista.
    pertence = False
    while pertence == False:
        for i in range(len(matriz_pib)-1):
            if matriz_pib[i+1][0].lower() == pais.lower():
                pertence = True
                # Ponteiro linha.
                linha = i+1
                
        if pertence == False:
            pais = str(input("Atenção, Digite um país dentre os países acima: "))
    
    # Pede para entrar com o ano.
    try:
        ano = int(input("Digite o ano (Entre 2013 e 2020): "))
    except ValueError:
        ano = 0
    # Verifica se o ano é válido.
    while ano < 2013 or ano > 2020:
        try:
            ano = int(input("Atenção, Digite o ano (Entre 2013 e 2020): "))
        except ValueError:
            ano = 0
    
    # Percorre a primeira linha para achar a coluna do respectivo ano
    for j in range(len(matriz_pib[0])-1):
        if int(matriz_pib[0][j+1]) == ano:
            # Ponteiro coluna.
            coluna = j+1
    # Agora mostra o PIB do país com os ponteiros linha e coluna.
    pib = float(matriz_pib[linha][coluna])*10**12 # 10**11 é 10 elevado a 12
    print(f"O PIB do ",pais," é de US$ ", formatar_moeda(pib), ".")
    print("-------------------------------------------------------------------------------------------------------------------")
    print("---------------------------------------- FIM PRODUTO INTERNO BRUTO DE UM PAÍS -------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------------")
    input("TECLE ENTER PARA CONTINUAR")
    print("\n" * 130)
    
def pib_lista_estimativa():
    print("\n" * 130)
    print("-------------------------------------------------------------------------------------------------------------------")
    print("--------------------------------------------- ESTIMATIVA DE PIB POR PAÍS ------------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------------")
    # Gera a matriz
    matriz_pib = gera_matriz()
    # Imprime o nome dos países para escolha.
    paises = "Países: "
    # Imprime o nome dos países para escolha.
    for i in range(len(matriz_pib)-1):
        paises = paises + matriz_pib[i+1][0] + " | "

    print("")
    print("Estimativa de PIB dos países abaixo, em percentual, entre 2013 e 2020:")
    print(paises)
    print("")
    input("TECLE ENTER PARA CONTINUAR")
    print("")
    print("------ PAÍS ------#####------ VARIAÇÃO ------")
    print("---------------------------------------------")
    print("")
    # Percorrer a matriz para calcular variação e imprimir    
    for i in range(len(matriz_pib)-1):
        # Comneça a partir da segunda linha
        linha = matriz_pib[i+1]
        # Pega ano 2013
        pib_2013 = round(float(linha[1]),2)
        # Pega ano 2020
        pib_2020 = round(float(linha[len(linha)-1]),2)
        # Calcula a variação
        variacao = round((((pib_2020/pib_2013)-1)*100),2)
        # Imprime
        print(" -- ",linha[0]," -----#####----- ",variacao,"%")
        print("---------------------------------------------")
    
    print("")
    print("-------------------------------------------------------------------------------------------------------------------")
    print("------------------------------------------- FIM ESTIMATIVA DE PIB POR PAÍS ----------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------------")
    input("TECLE ENTER PARA CONTINUAR")
    print("\n" * 130)
    
    
def pib_grafico_evolucao():
    print("\n" * 130)
    print("-------------------------------------------------------------------------------------------------------------------")
    print("--------------------------------------- GRÁFICO DE ESTIMATIVA DE PIB POR PAÍS -------------------------------------")
    print("-------------------------------------------------------------------------------------------------------------------")
    # Gera a matriz
    matriz_pib = gera_matriz()
    # Imprime o nome dos países para escolha.
    paises = "Países: "
    # Imprime o nome dos países para escolha.
    for i in range(len(matriz_pib)-1):
        paises = paises + matriz_pib[i+1][0] + " | "
    
    print(paises)
    print("")
    # Pede para entrar com o país.
    pais = str(input("Dentre os países acima, escolha um para mostrar o gráfico de estimativa do PIB: "))
    # Verifica se o país está na lista.
    pertence = False
    while pertence == False:
        for i in range(len(matriz_pib)-1):
            if matriz_pib[i+1][0].lower() == pais.lower():
                pertence = True
                # Ponteiro linha.
                linha = i+1
                
        if pertence == False:
            pais = str(input("Atenção, Digite um país dentre os países acima: "))
            
    # Prepara os dados do gráfico.
    ano = matriz_pib[0]
    ano.remove(ano[0])
    # Transformando os dados em números inteiros.
    for i in range(len(ano)):
        ano[i] = int(ano[i])
    # Recebe o PIB do país pelo ponteiro linha.
    pib = matriz_pib[linha]
    # Remove o país da lista
    pib[0] = pib[0].lower()
    pib.remove(pais.lower())
    # Transformando os dados em números reais.
    for j in range(len(pib)):
        pib[j] = round(float(pib[j]),2)
    
    # Gerando o gráfico.
    
    # Tamanho do gráfico
    plt.rcParams['figure.figsize'] = (12,8)
    # Desenha o gráfico
    plt.plot(ano,pib,'b-o',label="Evolução PIB")
    # Nomes dos eixos X e Y
    plt.xlabel('Ano')
    plt.ylabel('PIB em trilhões de US$')
    # Título do gráfico
    plt.title("Evolução do PIB")
    # Posição da legenda
    plt.legend(loc="lower right")
    # Mostra guias no gáfico
    plt.grid()
    # Salva o gráfico
    plt.savefig('grafico_q5.png')
    # Mostra o gráfico
    plt.show()
    
    print("")
    print("-------------------------------------------------------------------------------------------------------------------")
    print("-------------------------------------- FIM GRÁFICO DE ESTIMATIVA DE PIB POR PAÍS ----------------------------------")
    print("-------------------------------------------------------------------------------------------------------------------")
    input("TECLE ENTER PARA CONTINUAR")
    print("\n" * 130)
# :::::::::::::::::::::::::::::::::::::::::::::::::: PROGRAMA PRINCIPAL ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

print("-------------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------- PRODUTO INTERNO BRUTO ------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------")
print("\nSaudações, Considere a seguinte projeção de PIB feita pelo FMI em 2014 para as maiores Economias do Mundo")

# variavel opção definida antes para entrar no While
opcao = 0

while opcao != 4:

    print("\nDigite 1 para mostrar o PIB de um país para um determinado ano.")
    print("\nDigite 2 para listar por país a estimativa de variação do PIB, em percentual, entre 2013 e 2020.")
    print("\nDigite 3 para exibir o gráfico de evolução do PIB ao longo dos anos de 2013 a 2020.")
    print("\nDigite 4 para sair do programa.")
    print("")
    # Recebe a opção e valida.
    # Opção: opcao
    try:
        opcao = int(input("\nDigite sua opção: "))
    except ValueError:
        opcao = 0
    
    while opcao <= 0 or opcao >=5:
        try:
            opcao = int(input("\nAtenção, digite uma opção entre 1 e 4: "))
        except ValueError:
            opcao = 0

    # Primeira opção: Mostrar o PIB de um país para um determinado ano.
    if opcao == 1:
        pib_pais_ano()
    # Segunda opção: Mostar uma lista, por país, da estimativa de variação do PIB, em percentual, entre 2013 e 2020.
    if opcao == 2:
        pib_lista_estimativa()
    # Terceira opção: Mostra um gráfico da evolução do PIB ao longo dos anos de um determinado país.
    if opcao == 3:
        pib_grafico_evolucao()
        

print("")
print("")
print("-------------------------------------------------------------------------------------------------------------------")
print("------------------------------------------ FIM PRODUTO INTERNO BRUTO ----------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------")
# :::::::::::::::::::::::::::::::::::::::::::::::::: FIM PROGRAMA PRINCIPAL :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
