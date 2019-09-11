class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, x=None, y=None):
        self.parent = parent
        self.x = x
        self.y = y

        self.g = 0  # custo da distancia
        self.h = 0  # custo do movimento
        self.f = 0  # custo total



def best_first(maze):
    sx = maze.start[0]
    sy = maze.start[1]
    ex = maze.end[0]
    ey = maze.end[1]
    start = Node(None, sx, sy)
    start.f = 0
    end = Node(None, ex, ey)
    end.f = 0

    current = start
    moves = 0
    cust = 0
    path = []

    while current.x < maze.nRows and current.y < maze.nColumns:

        positions = []
        # verificando cada posição alcançável pela minha posição atual
        for coordinate in [(current.x, current.y+1), (current.x, current.y-1), (current.x+1, current.y), (current.x-1, current.y),
            (current.x+1, current.y+1), (current.x+1, current.y-1), (current.x-1, current.y+1), (current.x-1, current.y-1)]:

            x = coordinate[0]
            y = coordinate[1]
            stuff = scanMaze(maze, x, y)
            if stuff != 'WALL':
                pos = Node(current, x, y)
                pos.f = end.x-x + end.y-y  # calculando custo apenas com base na distância
                positions.append(pos)

        positions.sort(key=lambda x: x.f)  # ordenei pelo menor custo
        choice = positions[0]
        new_position = Node(current, choice.x, choice.y)  # definindo meu próximo movimento
        moves += 1
        path.append(new_position)

        if abs(new_position.x) - abs(current.x) == 1 and abs(new_position.y) - abs(current.y) == 1:  # diagonal
            cust += 1.5
        else:  # horizontal ou vertical
            cust += 1

        current = new_position



        if current.x == end.x and current.y == end.y:
            break

    print('Numero de movimentos: ', moves, ' | Custo: ', cust)
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



