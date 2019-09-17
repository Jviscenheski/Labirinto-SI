# -*- coding: utf-8 -*-

import best_first
import a_star

class Robot:

    def __init__(self):
        self.locX = "null"
        self.locY = "null"
        self.facing = "null"
        self.facingEnd = "null"

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
        print("Robot position: X =", self.locX,"Y =", self.locY, "\nFacing:", end = "")
        if self.facing == 'NORTH':
            print(" NORTH")
        if self.facing == 'EAST':
            print(" EAST")
        if self.facing == 'SOUTH':
            print(" SOUTH")
        if self.facing == 'WEST':
            print(" WEST")
        if self.facing == 'NORTHEAST':
            print(" NORTHEAST")
        if self.facing == 'NORTHWEST':
            print(" NORTHWEST")
        if self.facing == 'SOUTHEAST':
            print(" SOUTHEAST")
        if self.facing == 'SOUTHWEST':
            print(" SOUTHWEST")

    def printFinalState(self):
        print("Robot position: X =", self.locX,"Y =", self.locY, "\nFacing at the start:", end = "")
        if self.facing == 'NORTH':
            print(" NORTH")
        if self.facing == 'EAST':
            print(" EAST")
        if self.facing == 'SOUTH':
            print(" SOUTH")
        if self.facing == 'WEST':
            print(" WEST")
        if self.facing == 'NORTHEAST':
            print(" NORTHEAST")
        if self.facing == 'NORTHWEST':
            print(" NORTHWEST")
        if self.facing == 'SOUTHEAST':
            print(" SOUTHEAST")
        if self.facing == 'SOUTHWEST':
            print(" SOUTHWEST")
        print('Facing at the end:', self.facingEnd)


class Environment:

    def __init__(self):
        self.nRows = 0
        self.nColumns = 0
        self.matrix = []
        self.start = (0,0)
        self.end = (0,0)

    def scanStateFromFile(self, robot):
        lineList = []
        with open("mapa.txt") as file:
            if file:
                for line in file:
                    lineList.append(line.strip())
                
                del lineList[0]
                del lineList[0]

                self.nColumns = len(lineList[0])
                self.nRows = len(lineList)
                self.matrix = [[0 for x in range(self.nColumns)] for y in range(self.nRows)]
                lineIndex = 0
                columnIndex = 0

                for line in lineList:
                    for char in line:
                        if char == ".":
                            self.matrix[lineIndex][columnIndex] = 0
                        elif char == "*":
                            self.matrix[lineIndex][columnIndex] = 1
                        elif char == "^":
                            self.matrix[lineIndex][columnIndex] = 2
                            robot.setLocation(lineIndex, columnIndex)
                            robot.facing = 'NORTH'
                            self.start = (lineIndex,columnIndex)
                        elif char == "<":
                            self.matrix[lineIndex][columnIndex] = 2
                            robot.setLocation(lineIndex, columnIndex)
                            robot.facing = 'WEST'
                            self.start = (lineIndex,columnIndex)
                        elif char == "v":
                            self.matrix[lineIndex][columnIndex] = 2
                            robot.setLocation(lineIndex, columnIndex)
                            robot.facing = 'SOUTH'
                            self.start = (lineIndex,columnIndex)
                        elif char == ">":
                            self.matrix[lineIndex][columnIndex] = 2
                            robot.setLocation(lineIndex, columnIndex)
                            robot.facing = 'EAST'
                            self.start = (lineIndex,columnIndex)
                        elif char == "x":
                            self.matrix[lineIndex][columnIndex] = 4
                            self.end = (lineIndex, columnIndex)

                        columnIndex = columnIndex + 1
                    columnIndex = 0
                    lineIndex = lineIndex + 1
    
            
            else:
                print("File source is empty! :(")

    def scanState(self):  # nao entendi pra que isso serve haha
        for line in range(self.nRows):
            for column in range(self.nColumns):
                # recolhe o caracter
                char = "null"
                if char == ">":
                    self.matrix[line][column] = 2
                elif char == ".":
                    self.matrix[line][column] = 0
                elif char == "*":
                    self.matrix[line][column] = 1
                elif char == "^":
                    self.matrix[line][column] = 2
                elif char == "<":
                    self.matrix[line][column] = 2
                elif char == "x":
                    self.matrix[line][column] = 4
                elif char == "v":
                    self.matrix[line][column] = 2

    def printState(self, robot):
        print("    ", end = '')
        for i in range(self.nColumns):
            print(str(i), end = '')
            if i < 10:
                print("   ", end = '')
            else:
                print("  ", end = '')
        print('')
        print('  ', end = '')
        for i in range(self.nColumns):
            print("+---", end = '')
        print("+")
        for r in range(self.nRows):
            if r < 10: 
                print('', str(r), end = '')
            else:
                print(str(r), end = '')
            for c in range(self.nColumns):
                if self.matrix[r][c] == 1:
                    print("|***", end = '')
                if self.matrix[r][c] == 4:
                    print("| X ", end = '')
                if self.matrix[r][c] == 0:
                    print("|   ", end = '')
                if self.matrix[r][c] == 3:
                    print("| @ ", end = '')
                if self.matrix[r][c] == 2:
                    if robot.facing == 'NORTH':
                        print("| ^ ", end = '')
                    elif robot.facing == 'NORTHEAST':
                        print("| / ", end = '')
                    elif robot.facing == 'EAST':
                        print("| > ", end = '')
                    elif robot.facing == 'SOUTHEAST':
                        print("| \\ ", end = '')
                    elif robot.facing == 'SOUTH':
                        print("| v ", end = '')
                    elif robot.facing == 'SOUTHWEST':
                        print("| % ", end = '')
                    elif robot.facing == 'WEST':
                        print("| < ", end = '')
                    elif robot.facing == 'NORTHWEST':
                        print("| # ", end = '')

            print( "|", end = '' )
            print('')
            print("  ", end = '')
            for i in range(self.nColumns):
                print("+---", end = '')
            print("+")

        robot.printState()

    def printFinalState(self, robot):
        print("    ", end = '')
        for i in range(self.nColumns):
            print(str(i), end = '')
            if i < 10:
                print("   ", end = '')
            else:
                print("  ", end = '')
        print('')
        print('  ', end = '')
        for i in range(self.nColumns):
            print("+---", end = '')
        print("+")
        for r in range(self.nRows):
            if r < 10: 
                print('', str(r), end = '')
            else:
                print(str(r), end = '')
            for c in range(self.nColumns):
                if self.matrix[r][c] == 1:
                    print("|***", end = '')
                if self.matrix[r][c] == 4:
                    print("| X ", end = '')
                if self.matrix[r][c] == 0:
                    print("|   ", end = '')
                if self.matrix[r][c] == 3:
                    print("| @ ", end = '')
                if self.matrix[r][c] == 2:
                    if robot.facing == 'NORTH':
                        print("| ^ ", end = '')
                    elif robot.facing == 'NORTHEAST':
                        print("| / ", end = '')
                    elif robot.facing == 'EAST':
                        print("| > ", end = '')
                    elif robot.facing == 'SOUTHEAST':
                        print("| \\ ", end = '')
                    elif robot.facing == 'SOUTH':
                        print("| v ", end = '')
                    elif robot.facing == 'SOUTHWEST':
                        print("| % ", end = '')
                    elif robot.facing == 'WEST':
                        print("| < ", end = '')
                    elif robot.facing == 'NORTHWEST':
                        print("| # ", end = '')

            print( "|", end = '' )
            print('')
            print("  ", end = '')
            for i in range(self.nColumns):
                print("+---", end = '')
            print("+")

        robot.printFinalState()

    def moveRobot(self, direction, robot):
        if (direction == 'NORTH') and (robot.facing == 'NORTH') and (self.matrix[robot.locX - 1][robot.locY] != 1) \
                and (robot.locX > 0):
            self.matrix[robot.locX][robot.locY] = 0
            self.matrix[robot.locX - 1][robot.locY] = 2
            robot.move('NORTH')
        elif (direction == 'NORTHWEST') and (robot.facing == 'NORTHWEST') and (self.matrix[robot.locX - 1][robot.locY - 1] != 1) \
                and (robot.locX > 0) and (robot.locY > 0):
            self.matrix[robot.locX][robot.locY] = 0
            self.matrix[robot.locX-1][robot.locY-1] = 2
            robot.move('NORTHWEST')
        elif (direction == 'NORTHEAST') and (robot.facing == 'NORTHEAST') and (robot.locY < self.nColumns - 1) \
                and (robot.locX > 0) and (self.matrix[robot.locX - 1][robot.locY + 1] != 1):
            self.matrix[robot.locX][robot.locY] = 0
            self.matrix[robot.locX-1][robot.locY+1] = 2
            robot.move('NORTHEAST')

        elif (direction == 'SOUTH') and (robot.facing == 'SOUTH') and (robot.locX < self.nRows - 1) \
                and (self.matrix[robot.locX+1][robot.locY] != 1):
            self.matrix[robot.locX][robot.locY] = 0
            self.matrix[robot.locX+1][robot.locY] = 2
            robot.move('SOUTH')
        elif (direction == 'SOUTHWEST') and (robot.facing == 'SOUTHWEST') and (robot.locX < self.nRows - 1) \
                and (robot.locY > 0) and (self.matrix[robot.locX + 1][robot.locY-1] != 1):
            self.matrix[robot.locX][robot.locY] = 0
            self.matrix[robot.locX+1][robot.locY-1] = 2
            robot.move('SOUTHWEST')
        elif (direction == 'SOUTHEAST') and (robot.facing == 'SOUTHEAST') and (robot.locY < self.nColumns - 1) \
                and (robot.locX < self.nRows - 1) and (self.matrix[robot.locX + 1][robot.locY+1] != 1):
            self.matrix[robot.locX][robot.locY] = 0
            self.matrix[robot.locX+1][robot.locY+1] = 2
            robot.move('SOUTHEAST')

        elif (direction == 'EAST') and (robot.facing == 'EAST') and (robot.locY < self.nColumns - 1) \
                and (self.matrix[robot.locX][robot.locY+1] != 1):
            self.matrix[robot.locX][robot.locY] = 0
            self.matrix[robot.locX][robot.locY+1] = 2
            robot.move('EAST')
        elif (direction == 'WEST') and (robot.facing == 'WEST') and (robot.locY > 0) \
                and (self.matrix[robot.locX][robot.locY-1] != 1):
            self.matrix[robot.locX][robot.locY] = 0
            self.matrix[robot.locX][robot.locY-1] = 2
            robot.move('WEST')

    def rotateRobot(self, rotation, robot):
        if rotation == 'd':
            if robot.facing == 'NORTH':
                robot.facing = 'NORTHEAST'
            elif robot.facing == 'NORTHEAST':
                robot.facing = 'EAST'
            elif robot.facing == 'EAST':
                robot.facing = 'SOUTHEAST'
            elif robot.facing == 'SOUTHEAST':
                robot.facing = 'SOUTH'
            elif robot.facing == 'SOUTH':
                robot.facing = 'SOUTHWEST'
            elif robot.facing == 'SOUTHWEST':
                robot.facing = 'WEST'
            elif robot.facing == 'WEST':
                robot.facing = 'NORTHWEST'
            elif robot.facing == 'NORTHWEST':
                robot.facing = 'NORTH'
        if rotation == 'a':
            if robot.facing == 'NORTH':
                robot.facing = 'NORTHWEST'
            elif robot.facing == 'NORTHWEST':
                robot.facing = 'WEST'
            elif robot.facing == 'WEST':
                robot.facing = 'SOUTHWEST'
            elif robot.facing == 'SOUTHWEST':
                robot.facing = 'SOUTH'
            elif robot.facing == 'SOUTH':
                robot.facing = 'SOUTHEAST'
            elif robot.facing == 'SOUTHEAST':
                robot.facing = 'EAST'
            elif robot.facing == 'EAST':
                robot.facing = 'NORTHEAST'
            elif robot.facing == 'NORTHEAST':
                robot.facing = 'NORTH'

'''
    Instancia todas as possíveis configurações - 0 em todas as posições da matriz e todas as permutações
    Adiciona todas essas instâncias como nós
    Adiciona aresta entre as entidades que possuem o 0 em posições i+1, j-1,j+1 ou i-1 com relação ao nó atual
    Recolhe o estado inicial e localiza no grafo
    Recolhe o estado final e localiza no grafo
    Percorre o grafo com busca em aprofundamento (largura + profundidade)
    Tcharam
'''

def pathfind(env, robot, alg):
    print('\nAlgoritmo', alg, '\n')
    dirs = 8
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    print('Map size (X,Y): ', env.nColumns, env.nRows)
    print('Start: ', env.start[1], env.start[0])
    print('Finish: ', env.end[1], env.end[0])
    if alg == 'astar':
        route = a_star.pathFind(env.matrix, robot, env.nColumns, env.nRows, dirs, dx, dy, env.start[1], env.start[0], env.end[1], env.end[0])
    else:
        route = best_first.pathFind(env.matrix, robot, env.nColumns, env.nRows, dirs, dx, dy, env.start[1], env.start[0], env.end[1], env.end[0])
    
    if len(route) > 0:
        x = env.start[1]
        y = env.start[0]
        env.matrix[y][x] = 2
        for i in range(len(route)):
            j = int(route[i])
            x += dx[j]
            y += dy[j]
            env.matrix[y][x] = 3
        env.matrix[y][x] = 4

    input('\nPress Enter...')


def main():
    algoritmo = ''
    robot = Robot()
    env = Environment()
    env.scanStateFromFile(robot)
    env.printState(robot)

    while True:
        key = input('Envie 1 para executar o A*, 2 para executar o BestFirst, W para ir para frente, A e D para rotacionar e Q para sair. ')
        if key == 'a' or key == 'd':
            env.rotateRobot(key, robot)
            env.printState(robot)
        elif key == 'w':
            env.moveRobot(robot.facing, robot)
            env.printState(robot)
        elif key == '1':
            algoritmo = 'astar'
            env.scanStateFromFile(robot)
            pathfind(env, robot, algoritmo)
            env.printFinalState(robot)
            break
        elif key == '2':
            algoritmo = 'bestFirst'
            env.scanStateFromFile(robot)
            pathfind(env, robot, algoritmo)
            env.printFinalState(robot)
            break
        elif key == 'q':
            break
        else:
            print('Invalid key!')
        key = ''
    
if __name__ == '__main__':
    main()
