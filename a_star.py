# -*- coding: utf-8 -*-

from heapq import heappush, heappop # para ordem de prioridade
import math
import time
import random

turn = 10

class Robot:
    def __init__(self):
        self.facing = "null"

    def __get__(self, instance, owner):
        return self.instance

    def __set__(self, instance, value):
        self.instance = value


class node:
    xPos = 0
    yPos = 0
    distance = 0 # Distancia total ja percorrida para chegar ao node
    priority = 0 # prioridade = distancia percorrida + distancia restante estimada
    direction = ''
    def __init__(self, xPos, yPos, distance, priority, direction):
        self.xPos = xPos
        self.yPos = yPos
        self.distance = distance
        self.priority = priority
        self.direction = direction
    def __lt__(self, other): # método de comparação para ordem de prioridade
        return self.priority < other.priority
    def updatePriority(self, xDest, yDest):
        self.priority = self.distance + (self.estimate(xDest, yDest) * 10)
    def nextMove(self, dirs, d): # d é a direção do movimento
        parentFacing = self.direction # Grava a direção do node que gerou o atual.

        if dirs == 8 and d % 2 != 0:
            self.distance += 15 # diagonal
        else:
            self.distance += 10 # linha reta
        # Seta a direção que o robo vai ter que estar para realizar o movimento
        if d == 0:
            self.direction = 'EAST'
        elif d == 1:
            self.direction = 'SOUTHEAST'
        elif d == 2:
            self.direction = 'SOUTH'
        elif d == 3:
            self.direction = 'SOUTHWEST'
        elif d == 4:
            self.direction = 'WEST'
        elif d == 5:
            self.direction = 'NORTHWEST'
        elif d == 6:
            self.direction = 'NORTH'
        elif d == 7:
            self.direction = 'NORTHEAST'

        if self.direction != parentFacing:
            if self.direction == 'NORTH':
                if parentFacing == 'NORTHEAST' or parentFacing == 'NORTHWEST':
                    self.distance += turn
                elif parentFacing == 'EAST' or parentFacing == 'WEST':
                    self.distance += 2 * turn
                elif parentFacing == 'SOUTHEAST' or parentFacing == 'SOUTHWEST':
                    self.distance += 3 * turn
                elif parentFacing == 'SOUTH':
                    self.distance += 4 * turn
            elif self.direction == 'NORTHEAST':
                if parentFacing == 'NORTH' or parentFacing == 'EAST':
                    self.distance += turn
                elif parentFacing == 'SOUTHEAST' or parentFacing == 'NORTHWEST':
                    self.distance += 2 * turn
                elif parentFacing == 'SOUTH' or parentFacing == 'WEST':
                    self.distance += 3 * turn
                elif parentFacing == 'SOUTHWEST':
                    self.distance += 4 * turn
            elif self.direction == 'EAST':
                if parentFacing == 'NORTHEAST' or parentFacing == 'SOUTHEAST':
                    self.distance += turn
                elif parentFacing == 'SOUTH' or parentFacing == 'NORTH':
                    self.distance += 2 * turn
                elif parentFacing == 'SOUTHWEST' or parentFacing == 'NORTHWEST':
                    self.distance += 3 * turn
                elif parentFacing == 'WEST':
                    self.distance += 4 * turn
            elif self.direction == 'SOUTHEAST':
                if parentFacing == 'EAST' or parentFacing == 'SOUTH':
                    self.distance += turn
                elif parentFacing == 'SOUTHWEST' or parentFacing == 'NORTHEAST':
                    self.distance += 2 * turn
                elif parentFacing == 'WEST' or parentFacing == 'NORTH':
                    self.distance += 3 * turn
                elif parentFacing == 'NORTHWEST':
                    self.distance += 4 * turn
            elif self.direction == 'SOUTH':
                if parentFacing == 'SOUTHWEST' or parentFacing == 'SOUTHEAST':
                    self.distance += turn
                elif parentFacing == 'WEST' or parentFacing == 'EAST':
                    self.distance += 2 * turn
                elif parentFacing == 'NORTHWEST' or parentFacing == 'NORTHEAST':
                    self.distance += 3 * turn
                elif parentFacing == 'NORTH':
                    self.distance += 4 * turn
            elif self.direction == 'SOUTHWEST':
                if parentFacing == 'WEST' or parentFacing == 'SOUTH':
                    self.distance += turn
                elif parentFacing == 'SOUTHEAST' or parentFacing == 'NORTHWEST':
                    self.distance += 2 * turn
                elif parentFacing == 'EAST' or parentFacing == 'NORTH':
                    self.distance += 3 * turn
                elif parentFacing == 'NORTHEAST':
                    self.distance += 4 * turn
            elif self.direction == 'WEST':
                if parentFacing == 'SOUTHWEST' or parentFacing == 'NORTHWEST':
                    self.distance += turn
                elif parentFacing == 'SOUTH' or parentFacing == 'NORTH':
                    self.distance += 2 * turn
                elif parentFacing == 'SOUTHEAST' or parentFacing == 'NORTHEAST':
                    self.distance += 3 * turn
                elif parentFacing == 'EAST':
                    self.distance += 4 * turn
            elif self.direction == 'NORTHWEST':
                if parentFacing == 'NORTH' or parentFacing == 'WEST':
                    self.distance += turn
                elif parentFacing == 'SOUTHWEST' or parentFacing == 'NORTHEAST':
                    self.distance += 2 * turn
                elif parentFacing == 'SOUTH' or parentFacing == 'EAST':
                    self.distance += 3 * turn
                elif parentFacing == 'SOUTHEAST':
                    self.distance += 4 * turn

    def estimate(self, xDest, yDest):
        xd = xDest - self.xPos
        yd = yDest - self.yPos
        d = math.sqrt((xd ** 2) + (yd **2))
        return(d)

def pathFind(the_map, robot, n, m, dirs, dx, dy, xA, yA, xB, yB):
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
    n0 = node(xA, yA, 0, 0, robot.facing)
    n0.updatePriority(xB, yB)
    heappush(pq[pqi], n0)
    open_nodes_map[yA][xA] = n0.priority # marca o node na lista de nodes não testados

    while len(pq[pqi]) > 0:
        # pega o node com a prioridade mais alta da lista de nodes não testados
        n1 = pq[pqi][0]
        n0 = node(n1.xPos, n1.yPos, n1.distance, n1.priority, n1.direction)
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
            print('Total cost =', n0.distance / 10)
            robot.facingEnd = n0.direction
            robot.locX = n0.xPos
            robot.locY = n0.yPos

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
                m0 = node(xdx, ydy, n0.distance, n0.priority, n0.direction)
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
