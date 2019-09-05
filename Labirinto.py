import networkx as nx
import numpy as np


maxRows = 20
maxColumns = 20


class Robot:

    def __init__(self):
        self.locX = "null"
        self.locY = "null"
        self.facing = "null"

    def __get__(self, instance, owner):
        return self.instance

    def __set__(self, instance, value):
        self.instance = value

    def setLocation(self, locX, locY):
        self.locX = locX
        self.locY = locY

    def move(self, direction):
        if direction == 'EAST':
            self.locY = self.locY + 1
        elif direction == 'SOUTHEAST':
            self.locY = self.locY + 1
            self.locX = self.locX + 1
        elif direction == 'WEST':
            self.locY = self.locY - 1
        elif direction == 'SOUTHWEST':
            self.locY = self.locY - 1
            self.locX = self.locX + 1
        elif direction == 'SOUTH':
            self.locX = self.locX + 1
        elif direction == 'NORTHWEST':
            self.locY = self.locY - 1
            self.locX = self.locX - 1
        elif direction == 'NORTH':
            self.locX = self.locX - 1
        elif direction == 'NORTHEAST':
            self.locY = self.locY + 1
            self.locX = self.locX - 1

    def printState(self):
        print("Robot position: X=%d, Y=%d, facing:", self.locX, self.locY)
        if self.facing == 'NORTH':
            print(" NORTH\n")
        if self.facing == 'EAST':
            print(" EAST\n")
        if self.facing == 'SOUTH':
            print(" SOUTH\n")
        if self.facing == 'WEST':
            print(" WEST\n")
        if self.facing == 'NORTHEAST':
            print(" NORTHEAST\n")
        if self.facing == 'NORTHWEST':
            print(" NORTHWEST\n")
        if self.facing == 'SOUTHEAST':
            print(" SOUTHEAST\n")
        if self.facing == 'SOUTHWEST':
            print(" SOUTHWEST\n")


class Environment:

    def __init__(self):
        self.nRows = "null"
        self.nColumns = "null"
        self.matrix = [[0 for x in range(maxRows)] for y in range(maxColumns)]

    def scanStateFromFile(self, robot):
        lineList = []
        with open("mapa.txt") as file:
            if not file:
                for line in file:
                    lineList.append(line.strip())
            else:
                print("File source is empty! :(")

        del lineList[0]
        del lineList[0]

        lineIndex = 0
        columnIndex = 0

        for line in lineList:
            for char in line:
                if char == ">":
                    self.matrix[lineIndex][columnIndex] = 'ROBOT'
                elif char == ".":
                    self.matrix[lineIndex][columnIndex] = 'EMPTY'
                elif char == "*":
                    self.matrix[lineIndex][columnIndex] = 'WALL'
                elif char == "^":
                    self.matrix[lineIndex][columnIndex] = 'ROBOT'
                    robot.setLocation(lineIndex, columnIndex)
                    robot.facing = 'NORTH'
                elif char == "<":
                    self.matrix[lineIndex][columnIndex] = 'ROBOT'
                    robot.setLocation(lineIndex, columnIndex)
                    robot.facing = 'WEST'
                elif char == "x":
                    self.matrix[lineIndex][columnIndex] = 'TARGET'
                elif char == "v":
                    self.matrix[lineIndex][columnIndex] = 'ROBOT'
                    robot.setLocation(lineIndex, columnIndex)
                    robot.facing = 'SOUTH'

                columnIndex = columnIndex + 1
            columnIndex = 0
            lineIndex = lineIndex + 1


    def scanState(self):
        # recolhe número de linhas
        # recolhe número de colunas
        number_rows = 1998
        number_columns = 1998

        for line in range(0, number_rows):
            for column in range(0, number_columns):
                # recolhe o caracter
                char = "null"
                if char == ">":
                    self.matrix[line][column] = 'ROBOT'
                elif char == ".":
                    self.matrix[line][column] = 'EMPTY'
                elif char == "*":
                    self.matrix[line][column] = 'WALL'
                elif char == "^":
                    self.matrix[line][column] = 'ROBOT'
                elif char == "<":
                    self.matrix[line][column] = 'ROBOT'
                elif char == "x":
                    self.matrix[line][column] = 'TARGET'
                elif char == "v":
                    self.matrix[line][column] = 'ROBOT'


    def printState(self):






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


