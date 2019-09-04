import networkx as nx
import numpy as np


lineList = []
with open("mapa.txt") as file:
    for line in file:
        lineList.append(line.strip())

size_x = int(lineList[0])
size_y = int(lineList[1])

del lineList[0]
del lineList[0]

lineIndex = 0
columnIndex = 0

# 1 - obstáculo
# 0 - vazio
# 2 - origem
# 3 - destino

mapMatrix = [[0 for x in range(size_x)] for y in range(size_y)]

for line in lineList:
    for char in line:
        if char == ">":
            mapMatrix[lineIndex][columnIndex] = 2
        elif char == ".":
            mapMatrix[lineIndex][columnIndex] = 0
        elif char == "*":
            mapMatrix[lineIndex][columnIndex] = 1
        else:
            mapMatrix[lineIndex][columnIndex] = 3
        columnIndex = columnIndex + 1
    columnIndex = 0
    lineIndex = lineIndex + 1

print(mapMatrix)

grafo = nx.Graph()
grafo.add_node(0, position=[0, 0])
# penso que cada nó pode representar um estado

for line in range(size_x):
    for column in range(size_y):
        index = 0
        if column == 0:                         # vazio
            grafo.add_edge(index, index+1, custo=1)
        elif column == 1:
            print("blablabla")

'''
    Instancia todas as possíveis configurações - 0 em todas as posições da matriz e todas as permutações
    Adiciona todas essas instâncias como nós
    Adiciona aresta entre as entidades que possuem o 0 em posições i+1, j-1,j+1 ou i-1 com relação ao nó atual
    Recolhe o estado inicial e localiza no grafo
    Recolhe o estado final e localiza no grafo
    Percorre o grafo com busca em aprofundamento (largura + profundidade)
    Tcharam
'''


