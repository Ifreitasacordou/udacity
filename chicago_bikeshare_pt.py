
# coding: utf-8

# In[ ]:


# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
print("")
for amostra in range(1, 21):
    print(data_list[amostra])

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for genero in range(20):
    print(data_list[genero][6])


# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
# Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista

def column_to_list(data, index):
    """
          Função que transforma uma coluna em uma lista.
          Argumentos:
              data: Lista que contém todas as colunas.
              index: Inteiro contendo o valor do idx da coluna que deseja transformar em lista.
          Retorna:
              Uma lista:
                  column_list - contém os valores da coluna referenciada pelo index.

    """
    column_list = []
    for row in data:
        column_list.append(row[index])
    return column_list

# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
male = 0
female = 0

for genero in data_list:
    if genero[-2] == 'Female':
        female += 1
    elif genero[-2] == 'Male':
        male += 1
        
# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------



input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """
          Função que conta a quantidade de gêneros.
          Argumentos:
              data_list: Lista que contém todas informações.          
          Retorna:
              Uma lista com dois valores:
                  Female - Inteiro contendo a quantidade do gênero feminino.
                  Male - Inteiro contendo a quantidade do gênero masculino.

    """
    male = 0
    female = 0
    for genero in data_list:
        if genero[-2] == 'Female':
            female += 1
        elif genero[-2] == 'Male':
            male += 1
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list):
    """
          Função que mostra o gênero mais popular dentro do data_list.
          Argumentos:
              data_list: Lista que contém todas informações.          
          Retorna:
              Uma string:
                  answer - Contém o gênero mais popular na data_list, "Female", "Male" ou "Igual".

    """
    generos_list = count_gender(data_list)
    if generos_list[0] > generos_list[1]:
        answer = "Male"
    elif generos_list[0] < generos_list[1]:
        answer = "Female"
    else:
        answer = "Igual"
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

def count_user_type(data_list):
    """
          Função que conta a quantidade de tipo de usuário.
          Argumentos:
              data_list: Lista que contém todas informações.          
          Retorna:
              Uma lista com dois valores:
                  customer - Inteiro referente a quantidade de usuários customer.
                  subscriber - Inteiro referente a quantidade de usuários subscriber.               

    """
    customer = 0
    subscriber = 0
    for user_type in data_list:
        if user_type[-3] == 'Customer':
            customer += 1
        elif user_type[-3] == 'Subscriber':
            subscriber += 1
    return [customer, subscriber]

user_list = column_to_list(data_list, 5)
types = ["Customer","Subscriber"]
quantity = count_user_type(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de Usuário')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de Usuário')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque está contando os valores vazios no len(data_list)."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
trip_duration_list = [int(trip_duration_list[trip]) for trip in range(len(trip_duration_list))]


def min_trip_duration(duration_list):
    """
          Função que retorna o valor mínimo da duração de uma viagem na lista duration_list.
          Argumentos:
              duration_list: Lista que contém as durações das viagens.          
          Retorna:
              Um float:
                  min_trip - Menor duração de uma viagem na duration_list.

    """

    min_trip = float(duration_list[0])
    for trip in duration_list:
        if trip < min_trip:
            min_trip = trip
    return min_trip

def max_trip_duration(duration_list):
    """
          Função que retorna o valor máximo da duração de uma viagem na lista duration_list.
          Argumentos:
              duration_list: Lista que contém as durações das viagens.          
          Retorna:
              Um float:
                  max_trip - Maior duração de uma viagem na duration_list.

    """
    max_trip = float(duration_list[0])
    for trip in duration_list:
        if trip > max_trip:
            max_trip = trip
    return max_trip

def mean_trip_duration(duration_list):
    """
          Função que retorna a média da duração das viagens.
          Argumentos:
              duration_trip: Lista que contém as durações das viagens.          
          Retorna:
              Um float:
                  mean - contém a média referente ao parâmetro passado como lista duration_trip.

    """
    soma = 0
    for trip in duration_list:
        soma += trip
    mean = soma / len(duration_list)
    return mean

def median_trip_duration(duration_list):
    """
          Função que retorna a mediana da duração das viagens.
          Argumentos:
              duration_list: Lista que contém as durações das viagens.          
          Retorna:
              Um float:
                  median - contém o valor da mediana.

    """
    position = 0
    duration_list.sort()
    if len(duration_list) % 2 != 0:
        position = int(len(duration_list)/2)  
        median = duration_list[position]
        return median
    
    else:
        position = int(len(duration_list)/2)
        second_position = int(len(duration_list)/2)
        median = (duration_list[position-1]+duration_list[second_position])/2
        return median

min_trip = min_trip_duration(trip_duration_list)
max_trip = max_trip_duration(trip_duration_list)
mean_trip = mean_trip_duration(trip_duration_list)
median_trip = median_trip_duration(trip_duration_list)

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
user_types = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
      Função de exemplo com anotações.
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      Retorna:
          Uma lista de valores x.

"""

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    """
    A função conta os diferentes tipos de dados em uma lista.
        Argumentos:
            column_list: Lista que contém os itens a serem contados.
        Retorna:
            Duas listas:
                item_types - Lista com as categorias dos dados encontradas na column_list
                count_items - Lista com a quantidade de items referente a cada tipo de dado 
    """
    item_types = []
    count_items = []    
    items_set = set(column_list)

    for item in items_set:
        item_types.append(item)
        count_items.append(column_list.count(item))
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------

