# ALIAS (APELIDO) plt para a biblioteca usada
import matplotlib.pyplot as plt

# Função para pegar os dados do arquivo csv para usar dentro do programa ou em outras funções.
def extrair_dados(caminho_arquivo):
    # passo 1: abrir o arquivo encoding='windows1252' #caminho_arquivo = "kobe.csv"
    arquivo = open(caminho_arquivo,encoding='utf8')
    # passo 2: copiar o conteudo do arquivo
    conteudo = arquivo.read()
    # passo 3: fecha o arquivo.
    arquivo.close()
    # passo 4: Copiado o conteudo vamos separa-los em uma lista.
    conteudo = conteudo.splitlines()
    
    # passo 5: separar o cabeçalho da lista na variavel "rotulos" e transforma-la em uma lista.
    rotulos = conteudo[0]
    rotulos = rotulos.split(',')
    
    # passo 6: separar o resto dos dados de conteudo em uma variavel "dados"
    conteudo = conteudo[1:]
    
    # passo 7: criar uma lista de listas (matriz) chamada dados para conseguir manipular melhor.
    dados = []
    for elemento in conteudo:
        elemento = elemento.split(',')
        dados.append(elemento)
        
    # passo 8: retorna rotulos e dados.
    return rotulos, dados

# ITEM A DO EXERCICIO
def calcular_pontos(temporada):
    # chama a função para buscar os dados que serão manipulados.
    rotulos, dados = extrair_dados("kobe.csv")
    # Pega o indice da lista na variavel rotulos para poder usar na variavel "dados". metodo index retorna a posição dentro da lista.
    # rotulos ['TEMPORADA','PARTIDAS','MINUTOS','PONTOS','% CESTAS','% 3 PONTOS','REBOTES','ASSISTÊNCIAS']
    # INDICE      0           1          2         3        4          5          6            7

    indice_pontos = rotulos.index('PONTOS')
    indice_partidas = rotulos.index('PARTIDAS')
    indice_temporada = rotulos.index('TEMPORADA')
    
    # Percorre os dados e procura o ano para entrar no if        
    for elemento in dados:
        if int(elemento[indice_temporada]) == temporada:
            media_pontos = float(elemento[indice_pontos])
            num_partidas = int(elemento[indice_partidas])
            total_pontos = media_pontos * num_partidas
            # ESTOU IMPRIMINDO O VALOR DO TOTAL DE PONTOS APENAS PARA VER NO SHELL DO THONNY OU NO TERMINAL QUE ESTIVEREM USANDO.
            print(int(total_pontos))
            return int(total_pontos)

# função para exibir o gráfico.
def exibir_grafico(x,y):
    plt.plot(x,y)
    plt.show()
    
# ITEM B DO EXERCICIO
def exibir_grafico_percentual_pontos():
    # chama a função para buscar os dados que serão manipulados.
    rotulos, dados = extrair_dados("kobe.csv")
    
    indice_percentual_cestas = rotulos.index('% CESTAS')
    indice_temporada = rotulos.index('TEMPORADA')
    # Cria listas para mandar para a função gerar gráfico
    lista_temporadas = []
    lista_percentuais = []
    # percorre dados e pega todos os dados.
    for elemento in dados:
        lista_temporadas.append(int(elemento[indice_temporada]))
        lista_percentuais.append(float(elemento[indice_percentual_cestas]))
    # Chama a função para exibir o grafico passando o eixo X lista_temporadas e o eixo Y lista_percentuais 
    exibir_grafico(lista_temporadas,lista_percentuais)

################################################################################
# Chama a função pedida no item a
calcular_pontos(2016)

# Chama a função pedida no item b
exibir_grafico_percentual_pontos()

