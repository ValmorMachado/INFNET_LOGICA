# QUESTÃO 1 TP3
#Desenvolva uma função que calcule a divisão de uma conta de consumo (conta de restaurante ou bar), em reais,
#considerando o número de pessoas que estavam consumindo e a taxa de serviço que será paga ao garçom.

#Ao usuário do programa serão solicitados o 'valor total do consumo', em reais, 'o número total de pessoas' e o
#'percentual do serviço prestado', entre 0 e 100.

#Fluxo de exceção: 

#O programa deve verificar se o número total de pessoas é maior do que zero.
#O programa deve verificar se o percentual do serviço está dentro do intervalo válido, de 0 a 100. 
#Caso valores inválidos sejam digitados, deve ser exibida a mensagem de erro “Valor inválido” e o programa deve ser interrompido.
# Dica: Em Python, o valor monetário calculado ao final pode ser informado, na função print(), usando vírgula como separador de
#casa decimal, em vez de pontos.

#Para isso, converta o valor final da conta em uma string, usando a função str() e, em seguida, substitua os pontos por vírgulas
#com replace('.',',').
#Exemplo:

#valor = 1.99 # Valor numérico 
#valor = str(valor) # Converte o valor para uma string
#valor.replace('.', ',') # Substitui pontos por vírgulas
#print(valor) # Imprimirá 1,99

#Exemplo de saída do programa:
#Informe o valor total do consumo: R$ 100.00
#Informe o total de pessoas: 2
#Informe o percentual do serviço, entre 0 e 100: 10
#O valor total da conta, com a taxa de serviço, será de R$ 110,00.
#Dividindo a conta por 2 pessoa(s), cada pessoa deverá pagar R$ 55,00.

#-------------------------------------------------------------------------
#------------------------------TP3 QUESTÃO 1------------------------------
#-------------------------------------------------------------------------

# Função retirada do site "https://pt.stackoverflow.com/questions/66183/como-retornar-um-valor-no-formato-moeda-brasileiro-na-view-do-django"
# Função que recebe um valor
# Formata no valor americano (variavel a)
# Formata no valor brasileiro (variavel b, c e d)
# Independente do tamanho do número, troca as virgulas, quando existirem, por "v".
# Em seguida troca o ponto pela virgula.
# E caso exista a troca de de virgula por "v", troca todos os "v" por ponto.

def Formatar_moeda(valor):
    a = '{:,.2f}'.format(float(valor))
    b = a.replace(',','v')
    c = b.replace('.',',')
    d = c.replace('v','.')
    return d

def calcular_conta(q_pessoas,consumo,percentual):
    # Divide o consumo pela quantidade de pessoas.
    conta_pessoa = consumo / q_pessoas
    # Calcula a taxa de serviço.
    tx_servico = round(consumo * (percentual/100),2)
    # Calcula o valor final por pessoa.
    valor_final = round((consumo/q_pessoas) + (tx_servico/q_pessoas),2)
    # Calcula a divisão da taxa de serviço por cada pessoa.
    tx_pessoa = round((tx_servico / q_pessoas),2)
    
    if q_pessoas == 1:
        print(f"\nO valor da sua conta é R$ ",Formatar_moeda(consumo),".")
        print(f"\nVocê informou que pagará ",percentual,"% pela taxa de serviço, totalizando R$",Formatar_moeda(tx_servico),".")
        print(f"\nO valor da sua conta ficou R$",Formatar_moeda(valor_final),".")
    else:
        print(f"\nO valor da conta é R$",Formatar_moeda(consumo)," e você solicitou parcelamento para ",q_pessoas," pessoas.")
        print(f"\nVocê informou que pagará ",percentual,"% pela taxa de serviço, totalizando R$",Formatar_moeda(tx_servico),".")
        print(f"\nO valor da taxa de serviço para cada pessoa foi de R$ ",Formatar_moeda(tx_pessoa),".")
        print(f"\nO valor da conta para cada pessoa foi de R$ ",Formatar_moeda(conta_pessoa),".")
        print(f"\nO valor total para cada pessoa foi de R$ ",Formatar_moeda(valor_final),".")
    print("----------------------------------------------------------------------------------------------------")
    print("---------------------------------- OBRIGADO PELA PREFERÊNCIA ---------------------------------------")
    print("----------------------------------------------------------------------------------------------------")


print("----------------------------------------------------------------------------------------------------")
print("-------------------------------------- DIVIDINDO A CONTA -------------------------------------------")
print("----------------------------------------------------------------------------------------------------")
# Pede a quantidade de pessoas e valida.
try:
    q_pessoas = int(input(f"Saudações, por favor, digite o número de pessoas em que será dividido a conta: "))
except ValueError:
    q_pessoas = 0

# Para esse programa a primeira condição será o número de pessoas
if q_pessoas > 0:
    # Pede o consumo e valida.
    try:
        consumo = round(float(input(f"Gentileza, digite o valor da conta (exemplo: 850,12): ").replace(",",".")),2)
    except ValueError:
        consumo = 0
    
    # A segunda condição será o consumo.
    if consumo > 0:
        # Pede o percentual e valida.
        try:
            percentual = int(input(f"Entre 0% e 100%, quanto deseja pagar pela taxa de seviço? "))
        except ValueError:
            percentual = 101
            
        # A terceira condição será o consumo.
        if percentual >= 0 and percentual <= 100:
            # Chama a função para calcular
            calcular_conta(q_pessoas,consumo,percentual)
            
        # Caso valor digitado na segunda opção estiver errado finaliza o programa conforme a condição.
        else:
            print("----------------------------------------- VALOR INVÁLIDO! ------------------------------------------")
            print("----------------------------------------------------------------------------------------------------")
            print("----------------------------------------- FIM DO PROGRAMA ------------------------------------------")
            print("----------------------------------------------------------------------------------------------------")
            
    # Caso valor digitado na segunda opção estiver errado finaliza o programa conforme a condição.
    else:
        print("----------------------------------------- VALOR INVÁLIDO! ------------------------------------------")
        print("----------------------------------------------------------------------------------------------------")
        print("----------------------------------------- FIM DO PROGRAMA ------------------------------------------")
        print("----------------------------------------------------------------------------------------------------")
    
# Caso valor digitado na primeira opção estiver errado finaliza o programa conforme a condição.
else:
    print("----------------------------------------- VALOR INVÁLIDO! ------------------------------------------")
    print("----------------------------------------------------------------------------------------------------")
    print("----------------------------------------- FIM DO PROGRAMA ------------------------------------------")
    print("----------------------------------------------------------------------------------------------------")
