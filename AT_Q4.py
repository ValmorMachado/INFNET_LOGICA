#--------------------------------------------------------------------------
#------------------------------ AT QUESTÃO 4 ------------------------------
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

def hipotese_einstein(valor_inicial,rendimento,aporte,periodo):
    print("")
    print("")
    print("------------------------------------------------------------------------------------------------------------------")
    print("")
    print(f" Valor inicial informado: R$ ",formatar_moeda(valor_inicial))
    print(f" Rendimento por periodo informado: ",rendimento,"%")
    print(f" Aporte a cada periodo: R$ ",formatar_moeda(aporte))
    print(f" Total de periodos: ",periodo)
    print("")
    # Lista meses
    meses = []
    # Lista valores de rendimento mensal
    valor_mensal = []
    # Calculo do rendimento mensal
    montante = valor_inicial
    # Repete até o fim do periodo
    for i in range(periodo):
        montante = (montante + (montante*(rendimento/100))) + aporte
        print(f"Após ",i+1,"º mês, o montante será de R$ ",formatar_moeda(montante),".")
        meses.append(i+1)
        valor_mensal.append(round(montante,2))
            
    # Tamanho do gráfico
    plt.rcParams['figure.figsize'] = (15,7)
    # Desenha o gráfico
    plt.plot(meses,valor_mensal,'g-o',label="Evolução do montante")
    # Nomes dos eixos X e Y
    plt.xlabel('Meses')
    plt.ylabel('Faturamento em R$')
    # Título do gráfico
    plt.title("HIPOTESE DE EINSTEIN")
    # Posição da legenda
    plt.legend(loc="lower right")
    # Mostra guias no gáfico
    plt.grid()
    # Salva o gráfico
    plt.savefig('grafico_q4.png')
    # Mostra o gráfico
    plt.show()
    
# :::::::::::::::::::::::::::::::::::::::::::::::::: PROGRAMA PRINCIPAL ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

print("------------------------------------------------------------------------------------------------------------------")
print("-------------------------------------------- HIPOTESE DE EINSTEIN ------------------------------------------------")
print("------------------------------------------------------------------------------------------------------------------")
print("")
print("")
print("")
# Pede o valor inicial e valida.
# Valor inicial: valor_inicial.
try:
    valor_inicial = round(float(input(f"Por favor, digite o valor do montante: (exemplo: 3540,25): R$ ").replace(",",".")),2)    
except ValueError:
    valor_inicial = 'a'

while valor_inicial == 'a' or valor_inicial < 0:
    try:
        valor_inicial = round(float(input(f"Atenção, digite um valor do montante válido (exemplo: 3540,25): R$ ").replace(",",".")),2)
    except ValueError:
        valor_inicial = 'a'
        
       
print("")
print("")
# Pede o valor do rendimento mensal e valida.
# Rendimento: rendimento
try:
    rendimento = round(float(input(f"Agora digite o valor da porcentagem do rendimento: (exemplo: 0,54): ").replace(",",".")),2)    
except ValueError:
    rendimento = 'b'

while rendimento == 'b' or (rendimento <= 0 and rendimento >= 100):
    try:
        rendimento = round(float(input(f"Atenção, digite um valor da porcentagem do rendimento válido (exemplo: 0,54): ").replace(",",".")),2)
    except ValueError:
        rendimento = 'b'
        

print("")
print("")
# Pede o valor do aporte mensal e valida.
# Aporte: aporte
try:
    aporte = round(float(input(f" Digite o valor do aporte mensal: (exemplo: 3000,00): R$ ").replace(",",".")),2)    
except ValueError:
    aporte = 'c'

while aporte == 'c':
    try:
        aporte = round(float(input(f"Atenção, digite um valor do aporte mensal válido (exemplo: 3000,00): R$ ").replace(",",".")),2)
    except ValueError:
        aporte = 'c'        
        
print("")
print("")
# Pede o valor do periodo e valida.
# Período: periodo
try:
    periodo = int(input(f"Para finalizar, digite o período, em meses, de rendimento: (exemplo: 42): "))
except ValueError:
    periodo = 'd'

while aporte == 'd' or periodo <= 0:
    try:
        periodo = int(input(f"Atenção, digite um valor válido de meses (exemplo: 42): "))
    except ValueError:
        periodo = 'd'

# Chamando a função
hipotese_einstein(valor_inicial,rendimento,aporte,periodo)

print("")
print("")
print("------------------------------------------------------------------------------------------------------------------")
print("------------------------------------------ FIM HIPOTESE DE EINSTEIN ----------------------------------------------")
print("------------------------------------------------------------------------------------------------------------------")
# :::::::::::::::::::::::::::::::::::::::::::::::::: FIM PROGRAMA PRINCIPAL :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::