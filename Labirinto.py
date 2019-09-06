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

                if char == ".":
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
                elif char == "v":
                    self.matrix[lineIndex][columnIndex] = 'ROBOT'
                    robot.setLocation(lineIndex, columnIndex)
                    robot.facing = 'SOUTH'
                elif char == ">":
                    self.matrix[lineIndex][columnIndex] = 'ROBOT'
                    robot.setLocation(lineIndex, columnIndex)
                    robot.facing = 'EAST'
                elif char == "x":
                    self.matrix[lineIndex][columnIndex] = 'TARGET'


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

    def printState(self, robot):
        n_cols = 20 #??
        n_rows = 20 #??
        r = 0
        c = 0
        print("    ")
        for i in range(0, n_cols):
            print(str(i))

        print("\n")
        print("    ")
        for i in range(0, n_cols):
            print("+---")
        print("+\n")
        for r in range(0, n_rows):
            print(str(r))
            for c in range(0, n_cols):
                if self.matrix[r][c] == 'WALL':
                    print( "|***" )
                if self.matrix[r][c] == 'TARGET':
                    print( "| X " )
                if self.matrix[r][c] == 'EMPTY':
                    print( "|   " )
                if self.matrix[r][c] == 'ROBOT':
                    if robot.facing == 'NORTH':
                        print("| ^ ")
                    elif robot.facing == 'NORTHEAST':
                        print("| / ")
                    elif robot.facing == 'EAST':
                        print("| > ")
                    elif robot.facing == 'SOUTHEAST':
                        print("| \\ ")
                    elif robot.facing == 'SOUTH':
                        print("| v ")
                    elif robot.facing == 'SOUTHWEST':
                        print("| %% ")
                    elif robot.facing == 'WEST':
                        print("| < ")
                    elif robot.facing == 'NORTHWEST':
                        print("| # ")

            print( "|\n" )
            print("    ")
            for i in range(0, n_cols):
                print("+---")
                print("+\n")

        robot.print_state()

    def moveRobot(self, direction, robot):
        if (direction == 'NORTH') and (robot.facing == 'NORTH') and (robot.matrix[robot.locX - 1][robot.locY] != 'WALL') \
                and (robot.locX > 0) :
            robot.matrix[robot.locX][robot.locY] = 'EMPTY'
            robot.matrix[robot.locX - 1][robot.locY] = 'ROBOT'
            robot.move('NORTH')
        elif (direction == 'NORTHWEST') and (robot.facing == 'NORTHWEST') and (robot.matrix[robot.locX - 1][robot.locY - 1] != 'WALL') \
                and (robot.locX > 0) and (robot.locY > 0):
            robot.matrix[robot.locX][robot.locY] = 'EMPTY'
            robot.matrix[robot.locX-1][robot.locY-1] = 'ROBOT'
            robot.move('NORTHWEST')
        elif (direction == 'NORTHEAST') and (robot.facing == 'NORTHEAST') and (robot.matrix[robot.locX - 1][robot.locY + 1] != 'WALL') \
                and (robot.locX > 0) and (robot.locY < self.nColumns):
            robot.matrix[robot.locX][robot.locY] = 'EMPTY'
            robot.matrix[robot.locX-1][robot.locY+1] = 'ROBOT'
            robot.move('NORTHEAST')

        elif (direction == 'SOUTH') and (robot.facing == 'SOUTH') and (robot.matrix[robot.locX+1][robot.locY] != 'WALL') \
                and (robot.locX < self.nRows):
            robot.matrix[robot.locX][robot.locY] = 'EMPTY'
            robot.matrix[robot.locX+1][robot.locY] = 'ROBOT'
            robot.move('SOUTH')
        elif (direction == 'SOUTHWEST') and (robot.facing == 'SOUTHWEST') and (robot.matrix[robot.locX + 1][robot.locY-1] != 'WALL') \
                and (robot.locX < self.nRows) and (robot.locY > 0):
            robot.matrix[robot.locX][robot.locY] = 'EMPTY'
            robot.matrix[robot.locX+1][robot.locY-1] = 'ROBOT'
            robot.move('SOUTHWEST')
        elif (direction == 'SOUTHEAST') and (robot.facing == 'SOUTHEAST') and (robot.matrix[robot.locX + 1][robot.locY+1] != 'WALL') \
                and (robot.locX < self.nRows) and (robot.locY < self.nColumns):
            robot.matrix[robot.locX][robot.locY] = 'EMPTY'
            robot.matrix[robot.locX+1][robot.locY+1] = 'ROBOT'
            robot.move('SOUTHEAST')

        elif (direction == 'EAST') and (robot.facing == 'EAST') and (robot.matrix[robot.locX][robot.locY+1] != 'WALL') \
                and (robot.locY < self.nColumns):
            robot.matrix[robot.locX][robot.locY] = 'EMPTY'
            robot.matrix[robot.locX][robot.locY+1] = 'ROBOT'
            robot.move('EAST')
        elif (direction == 'WEST') and (robot.facing == 'WEST') and (robot.matrix[robot.locX][robot.locY-1] != 'WALL') \
                and (robot.locY > 0):
            robot.matrix[robot.locX][robot.locY] = 'EMPTY'
            robot.matrix[robot.locX][robot.locY-1] = 'ROBOT'
            robot.move('WEST')

'''
    Instancia todas as possíveis configurações - 0 em todas as posições da matriz e todas as permutações
    Adiciona todas essas instâncias como nós
    Adiciona aresta entre as entidades que possuem o 0 em posições i+1, j-1,j+1 ou i-1 com relação ao nó atual
    Recolhe o estado inicial e localiza no grafo
    Recolhe o estado final e localiza no grafo
    Percorre o grafo com busca em aprofundamento (largura + profundidade)
    Tcharam
'''


