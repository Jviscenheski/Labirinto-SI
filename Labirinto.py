import networkx as nx
import numpy as np


initialState = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
finalState = np.array([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

graph = nx.Graph()
graph.add_node(initialState)
#graph.add_node(np.array([[1, 2, 3], [4, 5, 6], [7, 0, 8]]))

'''
    Instancia todas as possíveis configurações - 0 em todas as posições da matriz e todas as permutações
    Adiciona todas essas instâncias como nós
    Adiciona aresta entre as entidades que possuem o 0 em posições i+1, j-1,j+1 ou i-1 com relação ao nó atual
    Recolhe o estado inicial e localiza no grafo
    Recolhe o estado final e localiza no grafo
    Percorre o grafo com busca em aprofundamento (largura + profundidade)
    Tcharam

'''

