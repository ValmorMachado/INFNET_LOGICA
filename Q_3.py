
# Questão 3 que o Pivotto fez na sala.

def julgar_fantasia(participantes): # Função de julgar as notas
    for i in range(participantes):
        nome = input(f"\nNome do participante: ")
        nota = float(input("Nota do participante: "))
        while nota < 0 or nota > 10:
            nota = float(input("Nota inválida - deve estar entre 0 e 10.\nNota do participante: "))
            
        if i==0:
            nome_vencedor = nome
            nota_vencedor = nota
        elif nota > nota_vencedor:
            nome_vencedor = nome
            nota_vencedor = nota
    
    print(f"O(A) vencedor(a) foi: {nome_vencedor}, com a nota {nota_vencedor}.")

# Chama a função
julgar_fantasia(5)