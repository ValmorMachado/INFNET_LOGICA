#--------------------------------------------------------------------------
#------------------------------ AT QUESTÃO 3 ------------------------------
#--------------------------------------------------------------------------

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

# Função que faz o disgnostico financeiro
def diagnosticar(renda_MT,aluguel,educacao,transporte):
    print(" ")
    print(f" DIAGNOSTICO:")
    print(f"---------------------------------------------------------------------------------------------------------------")
    # Cálculo do percentual gasto com moradia.
    p_aluguel = (aluguel/renda_MT)*100
    # Cálculo do valor máximo gasto com moradia.
    m_aluguel = (renda_MT*0.3)
    # Cria a condição para verificar os gastos com moradia.
    if p_aluguel <= 30:
        print(f" MORADIA:")
        print(" ")
        print(f" Seus gastos totais com moradia comprometem {p_aluguel:.2f}% de sua renda total. O máximo recomendado é de 30%.")
        print(f" Portanto, seu gasto com moradia no valor de R$ ",formatar_moeda(aluguel)," está dentro do valor sugerido.")
        print(f"---------------------------------------------------------------------------------------------------------------")
        print(" ")
    else:
        print(f" MORADIA:")
        print(" ")
        print(f" Seus gastos totais com moradia comprometem {p_aluguel:.2f}% de sua renda total. O máximo recomendado é de 30%.")
        print(f" Portanto, idealmente, o máximo da sua renda comprometida com moradia deveria ser de R$ ",formatar_moeda(m_aluguel),".")
        print(f"---------------------------------------------------------------------------------------------------------------")
        print(" ")
        
    # Cálculo do percentual gasto com educação.
    p_educacao = (educacao/renda_MT)*100
    # Cálculo do valor máximo gasto com educação.
    m_educacao = (renda_MT*0.2)
    # Cria a condição para verificar os gastos com educação.
    if p_educacao <= 20:
        print(f" EDUCAÇÃO:")
        print(" ")
        print(f" Seus gastos totais com educação comprometem {p_educacao:.2f}% de sua renda total. O máximo recomendado é de 20%.")
        print(f" Portanto, seu gasto com educação no valor de R$ ",formatar_moeda(educacao)," está dentro do valor sugerido.")
        print(f"---------------------------------------------------------------------------------------------------------------")
        print(" ")
    else:
        print(f" EDUCAÇÃO:")
        print(" ")
        print(f" Seus gastos totais com educação comprometem {p_educacao:.2f}% de sua renda total. O máximo recomendado é de 30%.")
        print(f" Portanto, idealmente, o máximo da sua renda comprometida com educação deveria ser de R$ ",formatar_moeda(m_educacao),".")
        print(f"---------------------------------------------------------------------------------------------------------------")
        print(" ")
        
    # Cálculo do percentual gasto com transporte.
    p_transporte = (transporte/renda_MT)*100
    # Cálculo do valor máximo gasto com transporte.
    m_transporte = (renda_MT*0.15)
    # Cria a condição para verificar os gastos com transporte.
    if p_transporte <= 15:
        print(f" TRANSPORTE:")
        print(" ")
        print(f" Seus gastos totais com transporte comprometem {p_transporte:.2f}% de sua renda total. O máximo recomendado é de 15%.")
        print(f" Portanto, seu gasto com transporte no valor de R$ ",formatar_moeda(transporte)," está dentro do valor sugerido.")
        print(f"---------------------------------------------------------------------------------------------------------------")
        print(" ")
    else:
        print(f" TRANSPORTE:")
        print(" ")
        print(f" Seus gastos totais com transporte comprometem {p_transporte:.2f}% de sua renda total. O máximo recomendado é de 15%.")
        print(f" Portanto, idealmente, o máximo da sua renda comprometida com transporte deveria ser de R$ ",formatar_moeda(m_transporte),".")
        print(f"---------------------------------------------------------------------------------------------------------------")
        print(" ")
    
# :::::::::::::::::::::::::::::::::::::::::::::::::: PROGRAMA PRINCIPAL ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

print("------------------------------------------------------------------------------------------------------------------")
print("------------------------------------------- DIAGNOSTICO FINANCEIRO -----------------------------------------------")
print("------------------------------------------------------------------------------------------------------------------")
print("")
print(" Vamos iniciar um diagnostico financeiro! Presisamos que você entre com alguns dados para avalição: ")
print("")
# Pede o valor da renda mensal total e valida.
# Renda mesnal total: renda_MT
try:
    renda_MT = round(float(input(f"Por gentileza, digite o valor da renda mensal da familia (exemplo: 850,32): R$ ").replace(",",".")),2)    
except ValueError:
    renda_MT = 'a'

while renda_MT == 'a' or renda_MT <= 0:
    try:
        renda_MT = round(float(input(f"Atenção, digite um valor da renda mensal da familia válido (exemplo: 850,32): R$ ").replace(",",".")),2)
    except ValueError:
        renda_MT = 'a'

# Pede o valor gasto com moradia e valida.
# Gasto com moradia: aluguel
try:
    aluguel = round(float(input(f"Agora digite o valor do aluguel do imóvel (exemplo: 1850,12): R$ ").replace(",",".")),2)    
except ValueError:
    aluguel = 'b'

while aluguel == 'b' or aluguel <= 0:
    try:
        aluguel = round(float(input(f"Atenção, digite um valor do aluguel do imóvel válido (exemplo: 1850,12): R$ ").replace(",",".")),2)
    except ValueError:
        aluguel = 'b'

# Pede o valor de gastos totais com educação e valida.
# Gastos totais com educação: educacao
try:
    educacao = round(float(input(f"Digite o valor do gasto com educação (exemplo: 353,10): R$ ").replace(",",".")),2)    
except ValueError:
    educacao = 'c'

while educacao == 'c' or educacao <= 0:
    try:
        educacao = round(float(input(f"Atenção, digite o valor do gasto com educação válido (exemplo: 353,10): R$ ").replace(",",".")),2)
    except ValueError:
        educacao = 'c'

# Pede o valor de gastos com transporte e valida.
# Gastos com transporte: transporte
try:
    transporte = round(float(input(f"Digite o valor do gasto com transporte (exemplo: 157,88): R$ ").replace(",",".")),2)    
except ValueError:
    transporte = 'd'

while transporte == 'd' or transporte <= 0:
    try:
        transporte = round(float(input(f"Atenção, digite o valor do gasto com transporte válido (exemplo: 157,88): R$ ").replace(",",".")),2)
    except ValueError:
        transporte = 'd'

# Chamando a função
diagnosticar(renda_MT,aluguel,educacao,transporte)

print("------------------------------------------------------------------------------------------------------------------")
print("----------------------------------------- FIM DIAGNOSTICO FINANCEIRO ---------------------------------------------")
print("------------------------------------------------------------------------------------------------------------------")
# :::::::::::::::::::::::::::::::::::::::::::::::::: FIM PROGRAMA PRINCIPAL :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::