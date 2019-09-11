class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, x=None, y=None):
        self.parent = parent
        self.x = x
        self.y = y

        self.g = 0
        self.h = 0
        self.f = 0

        self.facing = 'null'

def calculag(node, x, y, pos):
    turn = 1
    g = 0
    if (abs(x - node.x) == 1) and (abs(y - node.y) == 1):  # diagonal
        g += 1.5
    else:
        g += 1

    if (x, y) == (node.x + 1, node.y):
        direction = 'SOUTH'
    elif (x, y) == (node.x, node.y + 1):
        direction = 'EAST'
    elif (x, y) == (node.x - 1, node.y):
        direction = 'NORTH'
    elif (x, y) == (node.x, node.y - 1):
        direction = 'WEST'
    elif (x, y) == (node.x + 1, node.y + 1):
        direction = 'SOUTHEAST'
    elif (x, y) == (node.x - 1, node.y - 1):
        direction = 'NORTHWEST'
    elif (x, y) == (node.x + 1, node.y - 1):
        direction = 'SOUTHWEST'
    elif (x, y) == (node.x - 1, node.y + 1):
        direction = 'NORTHEAST'

    if direction != node.facing:
        if direction == 'NORTH':
            if node.facing == 'NORTHEAST' or node.facing == 'NORTHWEST':
                g += turn
            elif node.facing == 'EAST' or node.facing == 'WEST':
                g += 2 * turn
            elif node.facing == 'SOUTHEAST' or node.facing == 'SOUTHWEST':
                g += 3 * turn
            elif node.facing == 'SOUTH':
                g += 4 * turn
        elif direction == 'NORTHEAST':
            if node.facing == 'NORTH' or node.facing == 'EAST':
                g += turn
            elif node.facing == 'SOUTHEAST' or node.facing == 'NORTHWEST':
                g += 2 * turn
            elif node.facing == 'SOUTH' or node.facing == 'WEST':
                g += 3 * turn
            elif node.facing == 'SOUTHWEST':
                g += 4 * turn
        elif direction == 'EAST':
            if node.facing == 'NORTHEAST' or node.facing == 'SOUTHEAST':
                g += turn
            elif node.facing == 'SOUTH' or node.facing == 'NORTH':
                g += 2 * turn
            elif node.facing == 'SOUTHWEST' or node.facing == 'NORTHWEST':
                g += 3 * turn
            elif node.facing == 'WEST':
                g += 4 * turn
        elif direction == 'SOUTHEAST':
            if node.facing == 'EAST' or node.facing == 'SOUTH':
                g += turn
            elif node.facing == 'SOUTHWEST' or node.facing == 'NORTHEAST':
                g += 2 * turn
            elif node.facing == 'WEST' or node.facing == 'NORTH':
                g += 3 * turn
            elif node.facing == 'NORTHWEST':
                g += 4 * turn
        elif direction == 'SOUTH':
            if node.facing == 'SOUTHWEST' or node.facing == 'SOUTHEAST':
                g += turn
            elif node.facing == 'WEST' or node.facing == 'EAST':
                g += 2 * turn
            elif node.facing == 'NORTHWEST' or node.facing == 'NORTHEAST':
                g += 3 * turn
            elif node.facing == 'NORTH':
                g += 4 * turn
        elif direction == 'SOUTHWEST':
            if node.facing == 'WEST' or node.facing == 'SOUTH':
                g += turn
            elif node.facing == 'SOUTHEAST' or node.facing == 'NORTHWEST':
                g += 2 * turn
            elif node.facing == 'EAST' or node.facing == 'NORTH':
                g += 3 * turn
            elif node.facing == 'NORTHEAST':
                g += 4 * turn
        elif direction == 'WEST':
            if node.facing == 'SOUTHWEST' or node.facing == 'NORTHWEST':
                g += turn
            elif node.facing == 'SOUTH' or node.facing == 'NORTH':
                g += 2 * turn
            elif node.facing == 'SOUTHEAST' or node.facing == 'NORTHEAST':
                g += 3 * turn
            elif node.facing == 'EAST':
                g += 4 * turn
        elif direction == 'NORTHWEST':
            if node.facing == 'NORTH' or node.facing == 'WEST':
                g += turn
            elif node.facing == 'SOUTHWEST' or node.facing == 'NORTHEAST':
                g += 2 * turn
            elif node.facing == 'SOUTH' or node.facing == 'EAST':
                g += 3 * turn
            elif node.facing == 'SOUTHEAST':
                g += 4 * turn

    pos.facing = direction
    return g

def astar(maze, robot):
    sx = maze.start[0]
    sy = maze.start[1]
    ex = maze.end[0]
    ey = maze.end[1]
    start = Node(None, sx, sy)
    start.f = 0
    start.g = 0
    start.facing = robot.facing
    end = Node(None, ex, ey)
    end.f = 0

    current = start
    moves = 0
    cust = 0
    iterations = 0
    path = []

    while current.x < maze.nRows and current.y < maze.nColumns:
        positions = []
        # verificando cada posição alcançável pela minha posição atual
        for coordinate in [(current.x, current.y+1), (current.x, current.y-1), (current.x+1, current.y), (current.x-1, current.y),
            (current.x+1, current.y+1), (current.x+1, current.y-1), (current.x-1, current.y+1), (current.x-1, current.y-1)]:
            iterations += 1
            x = coordinate[0]
            y = coordinate[1]
            stuff = scanMaze(maze, x, y)
            if stuff != 'WALL':
                pos = Node(current, x, y)
                pos.g = calculag(current, x, y, pos)
                pos.h = end.x-x + end.y-y # calculando custo apenas com base na distância
                pos.f = pos.g + pos.h 
                positions.append(pos)

        positions.sort(key=lambda x: x.f)  # ordenei pelo menor custo

        #indexes = []
        #for node1 in path:
        #    for index, node2 in enumerate(positions):
        #        if node1 == node2:
        #            indexes.append(index)
        #for index in indexes:
        #    positions.pop(index)

        choice = positions[0]
        new_position = Node(current, choice.x, choice.y)  # definindo meu próximo movimento
        moves += 1
        path.append(new_position)

        cust += choice.g

        current = new_position



        if current.x == end.x and current.y == end.y:
            break

    print('Numero de movimentos: ', moves, ' | Custo: ', cust, ' | Operações: ', iterations)
    print('Coordenadas: ')
    for decision in path:
        print(decision.x, decision.y)
    print('ACHOU :D')


def scanMaze(maze, x, y):
    for row in range(maze.nRows):
        if x < 0 or x >= maze.nRows:
            # print('Fora do mapa rows')
            return 'WALL'
        elif row == x:
            for column in range(maze.nColumns):
                if y < 0 or y >= maze.nColumns:
                    # print('Fora do mapa columns')
                    return 'WALL'
                elif column == y:
                    # print(maze.matrix[row][column])
                    break
            break
    return maze.matrix[row][column]