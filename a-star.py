# -*- coding: utf-8 -*-

from heapq import heappush, heappop # para ordem de prioridade
import math
import time
import random

class node:
    xPos = 0
    yPos = 0
    distance = 0 # Distancia total ja percorrida para chegar ao node
    priority = 0 # prioridade = distancia percorrida + distancia restante estimada
    def __init__(self, xPos, yPos, distance, priority):
        self.xPos = xPos
        self.yPos = yPos
        self.distance = distance
        self.priority = priority
    def __lt__(self, other): # método de comparação para ordem de prioridade
        return self.priority < other.priority
    def updatePriority(self, xDest, yDest):
        self.priority = self.distance + self.estimate(xDest, yDest) * 10
    def nextMove(self, dirs, d): # d é a direção do movimento
        if dirs == 8 and d % 2 != 0:
            self.distance += 15 # diagonal
        else:
            self.distance += 10 # linha reta
    def estimate(self, xDest, yDest):
        xd = xDest - self.xPos
        yd = yDest - self.yPos
        d = (xd ** 2) + (yd **2)
        return(d)

def pathFind(the_map, n, m, dirs, dx, dy, xA, yA, xB, yB):
    closed_nodes_map = [] # mapa de nodes que ja foram testados
    open_nodes_map = [] # mapa de nodes que não foram testados
    dir_map = [] # mapa de direções
    row = [0] * n
    for i in range(m):
        closed_nodes_map.append(list(row))
        open_nodes_map.append(list(row))
        dir_map.append(list(row))

    pq = [[], []] # ordem de prioridade de nodes não testados
    pqi = 0 # indice de ordem de prioridade
    # Cria o node inicial e adiciona ele na lista de nodes não testados
    n0 = node(xA, yA, 0, 0)
    n0.updatePriority(xB, yB)
    heappush(pq[pqi], n0)
    open_nodes_map[yA][xA] = n0.priority # marca o node na lista de nodes não testados

    while len(pq[pqi]) > 0:
        # pega o node com a prioridade mais alta da lista de nodes não testados
        n1 = pq[pqi][0]
        n0 = node(n1.xPos, n1.yPos, n1.distance, n1.priority)
        x = n0.xPos
        y = n0.yPos
        heappop(pq[pqi]) # remove o node da lista de não testados
        open_nodes_map[y][x] = 0
        closed_nodes_map[y][x] = 1 # marca o node na lista de testados

        # finaliza a busca quando encontra o alvo
        # # if n0.estimate(xB, yB) == 0:
        if x == xB and y == yB:
            # gera o caminho do fim até o começo seguindo as direções
            path = ''
            while not (x == xA and y == yA):
                j = dir_map[y][x]
                c = str((j + dirs // 2) % dirs)
                path = c + path
                x += dx[j]
                y += dy[j]
            return path


        # gera os movimentos possíveis (nodes filhos) em todas as direções
        for i in range(dirs):
            xdx = x + dx[i]
            ydy = y + dy[i]
            if not (xdx < 0 or xdx > n-1 or ydy < 0 or ydy > m-1 or
                    the_map[ydy][xdx] == 1 or closed_nodes_map[ydy][xdx] == 1):
                # gera node filho
                m0 = node(xdx, ydy, n0.distance, n0.priority)
                m0.nextMove(dirs, i)
                m0.updatePriority(xB, yB)
                # se não estiver na lista de nodes não testados, adiciona
                if open_nodes_map[ydy][xdx] == 0:
                    open_nodes_map[ydy][xdx] = m0.priority
                    heappush(pq[pqi], m0)
                    # marca a posição do node pai
                    dir_map[ydy][xdx] = (i + dirs // 2) % dirs
                elif open_nodes_map[ydy][xdx] > m0.priority:
                    # atualiza a prioridade
                    open_nodes_map[ydy][xdx] = m0.priority
                    # atualiza a posição do node pai
                    dir_map[ydy][xdx] = (i + dirs // 2) % dirs
                    # substitui o node, todos menos o que vai ser substituido serão ignorados
                    # e o novo será inserido no lugar
                    while not (pq[pqi][0].xPos == xdx and pq[pqi][0].yPos == ydy):
                        heappush(pq[1 - pqi], pq[pqi][0])
                        heappop(pq[pqi])
                    heappop(pq[pqi]) # remove o node alvo
                    # esvazia a fila de prioridade maior até a menor
                    if len(pq[pqi]) > len(pq[1 - pqi]):
                        pqi = 1 - pqi
                    while len(pq[pqi]) > 0:
                        heappush(pq[1 - pqi], pq[pqi][0])
                        heappop(pq[pqi])
                    pqi = 1 - pqi
                    heappush(pq[pqi], m0) # adiciona o melhor node
    return '' # se não encontrar o alvo

# MAIN
dirs = 8 # number of possible directions to move on the map
if dirs == 4:
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
elif dirs == 8:
    dx = [1, 1, 0, -1, -1, -1, 0, 1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]

lineList = []
maze = []

with open("mapa.txt") as file:
    if file:
        for line in file:
            lineList.append(line.strip())
        
    
        del lineList[0]
        del lineList[0]
        maze = []            

        for i, line in enumerate(lineList):
            aux = [0] * len(lineList[0])
            for j, char in enumerate(line):
                if char == ".":
                    aux[j] = 0
                if char == "*":
                    aux[j] = 1
                if char == ">":
                    aux[j] = 2
                    xA = i
                    yA = j
                if char == "x":
                    aux[j] = 4
                    xB = i
                    yB = i
            maze.insert(i, aux)
                    
    else:
        print("File source is empty! :(")

n = len(lineList[0]) # horizontal size of the map
m = len(lineList) # vertical size of the map

print('Map size (X,Y): ', n, m)
print('Start: ', xA, yA)
print('Finish: ', xB, yB)
t = time.time()
route = pathFind(maze, n, m, dirs, dx, dy, xA, yA, xB, yB)
print('Time to generate the route (seconds): ', time.time() - t)
print('Route:')
print(route)

# mark the route on the map
if len(route) > 0:
    x = xA
    y = yA
    maze[y][x] = 2
    for i in range(len(route)):
        j = int(route[i])
        x += dx[j]
        y += dy[j]
        maze[y][x] = 3
    maze[y][x] = 4

# display the map with the route added
print('Map:')
for y in range(m):
    for x in range(n):
        xy = maze[y][x]
        if xy == 0:
            print('. ', end = '') # space
        elif xy == 1:
            print('* ', end = '') # obstacle
        elif xy == 2:
            print('> ', end = '') # start
        elif xy == 3:
            print('R ', end = '') # route
        elif xy == 4:
            print('X ', end = '')# finish
    print('')

input('\nPress Enter...')
