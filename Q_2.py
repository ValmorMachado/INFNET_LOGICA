# Desenvolva uma função que recebe a idade de uma pessoa e informe se essa pessoa é:
# Eleitor obrigatório (18 anos completos e menos de 70 anos de idade)
# Eleitor facultativo (16 anos completos e menos de 18 anos ou 70 anos de idade ou mais).
# Não tem direito a voto (menor de 16 anos).

# Fluxo de exceção: 
# O programa deve verificar se a idade da pessoa é maior do que zero.
# Exemplos de saída do programa:
# Informe a idade: 25 
# Tem obrigação de votar.
# Informe a idade: 75
# Não tem obrigação de votar.
# Informe a idade: 12
# Não tem direito a voto.

#-------------------------------------------------------------------------
#------------------------ TP3 QUESTÃO 2 ----------------------------------
#-------------------------------------------------------------------------

def idade_eleitoral(idade):
    # Verifica o voto facultativo.
    if (idade >= 16 and idade < 18) or (idade >= 70):
        print(" ")
        print (f"\n O seu direito de votar é facultativo!")
        print (f"\n Caso queira votar vá a junta eleitoral mais próxima para retirar seu título de eleitor ou verificar a situação do seu título!")
    # Verifica o voto obrigatório.
    elif idade >=18 and idade < 70:
        print(" ")
        print (f"\n O seu voto é obrigatório!")
        print (f"\n Gentileza verificar na junta eleitoral a situação do seu título de eleitor!")
    # senão não tem direito a voto (menor de 16 anos!)    
    else:
        print(" ")
        print (f"\n Não tem direito a voto!")
        print (f"\n Compareça a junta eleitoral a partir dos 16 anos caso queira votar!")    

print("----------------------------------------------------------------------------------------------------")
print("-------------------------------------- TENHO DIREITO A VOTO? ---------------------------------------")
print("----------------------------------------------------------------------------------------------------")
# A pessoa digita a idade.
idade = int(input(f"Por favor, digite a sua idade: "))

# Verifica a idade.
if idade > 0:
   idade_eleitoral(idade) 
# Caso valor digitado estiver errado finaliza o programa conforme a condição.
else:
    print("----------------------------------------- IDADE INVÁLIDA! ------------------------------------------")
    print("----------------------------------------------------------------------------------------------------")
    print("----------------------------------------- FIM DO PROGRAMA ------------------------------------------")
    print("----------------------------------------------------------------------------------------------------")
