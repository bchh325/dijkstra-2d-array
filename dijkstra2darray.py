import copy
#START = [[4, 8, 2, 8, 8, 1, 8, 7], [1, 1, 7, 2, 4, 7, 9, 4], [9, 5, 9, 8, 1, 1, 6, 7], [9, 2, 6, 7, 3, 7, 8, 7], [8, 2, 4, 5, 3, 7, 5, 7], [8, 1, 1, 5, 5, 6, 7, 4]]
#START = [[3, 4, 1, 2, 8, 6], [6, 1, 8, 2, 7, 4], [5, 4, 3, 9, 9, 5], [5, 9, 8, 3, 2, 6], [8, 7, 2, 9, 6, 4]]
START = [[1, 1, 4, 8, 8, 6, 2, 2, 8, 2, 1, 5], [2, 8, 1, 8, 2, 2, 2, 4, 5, 9, 9, 1], [8, 3, 2, 5, 2, 2, 5, 8, 9, 8, 4, 4], [1, 4, 1, 9, 8, 9, 5, 6, 1, 6, 4, 7], [7, 2, 6, 8, 4, 1, 1, 7, 1, 2, 5, 3], [6, 2, 2, 6, 1, 6, 2, 2, 7, 8, 7, 7], [8, 5, 5, 8, 9, 8, 7, 8, 8, 3, 2, 5]]

def solve(grid):
    instructions = []
    emptyGrid = []
    fillGrid(emptyGrid, grid)

    moves = len(grid[0]) - 1
    displayGrid(grid)
    print("------------------------")
    return (dijkstra(emptyGrid, grid))

def fillGrid(emptyGrid, grid):
    for i in range(len(grid)):
        emptyGrid.append([])

    for row in emptyGrid:
        for i in range(len(grid[0])):
            row.append('x')

def displayGrid(grid):
    for i in range(len(grid)):
        for num in grid[i]:
            print(f"{num}", end = " ")
        print()

def UpRight(points, grid):
    if points[0] == 0:
        points[0] = len(grid) - 1
    else:
        points[0] -= 1

    if points[1] == len(grid[0]) - 1:
        points[1] = 0
    else:
        points[1] += 1

    return points

def UpLeft(points, grid):
    if points[0] == 0:
        points[0] = len(grid) - 1
    else:
        points[0] -= 1

    if points[1] == 0:
        points[1] = len(grid[0]) - 1
    else:
        points[1] -= 1

    return points

def Right(points, grid):
    if points[1] == len(grid[0]) - 1:
        points[1] = 0
    else:
        points[1] += 1

    return points

def Left(points, grid):
    if points[1] == 0:
        points[1] = len(grid[0]) - 1
    else:
        points[1] -= 1

    return points

def DownRight(points, grid):
    if points[0] == len(grid) - 1:
        points[0] = 0
    else:
        points[0] += 1

    if points[1] == len(grid[0]) - 1:
        points[1] = 0
    else:
        points[1] += 1

    return points

def DownLeft(points, grid):
    if points[0] == len(grid) - 1:
        points[0] = 0
    else:
        points[0] += 1

    if points[1] == 0:
        points[1] = len(grid[0]) - 1
    else:
        points[1] -= 1

    return points

def dijkstra(e, grid):


    START_VALUE = []

    STARTING_POINTS = []
    indexOfMax = []

    findStartingPoints(STARTING_POINTS, grid)
    #print("STARTINGS", STARTING_POINTS)
    for p in STARTING_POINTS:
        eCopy = copy.deepcopy(e)
        point = p
        finished = []
        unfinished = []
        SOURCE_Y = point[1]
        eCopy[point[0]][point[1]] = grid[point[0]][point[1]]
        markAllUnfinished(eCopy, unfinished)
        try:
            while len(unfinished) != 0:

                #find biggest unfinished score, mark as finished
                point = markFinished(finished, unfinished, eCopy)
                #displayFinished(finished, copy.deepcopy(e))

                #relax all edges of just finished point
                relaxEdges(eCopy, point, grid, SOURCE_Y)
            #displayFinished(finished, eCopy)
            #displayGrid(eCopy)
            #displayGrid(grid)
        except Exception:
            appendMax(eCopy, indexOfMax, p)
            START_VALUE = copy.deepcopy(p)

    #print(indexOfMax)
    #print(indexOfMax.index(max(indexOfMax)))

    return getDirections(STARTING_POINTS[indexOfMax.index(max(indexOfMax))], copy.deepcopy(e), grid, max(indexOfMax), STARTING_POINTS[indexOfMax.index(max(indexOfMax))])

def getDirections(p, e, grid, mVal, START_VALUE):
    maxPoint = []
    optimalGrid = []
    fillGrid(optimalGrid, grid)
    eCopy = copy.deepcopy(e)
    point = p
    finished = []
    unfinished = []
    SOURCE_Y = point[1]
    eCopy[point[0]][point[1]] = grid[point[0]][point[1]]
    markAllUnfinished(eCopy, unfinished)
    try:
        while len(unfinished) != 0:
            # find biggest unfinished score, mark as finished
            point = markFinished(finished, unfinished, eCopy)
            # displayFinished(finished, copy.deepcopy(e))

            # relax all edges of just finished point
            relaxEdges(eCopy, point, grid, SOURCE_Y)
        # displayFinished(finished, eCopy)
        # displayGrid(grid)
    except Exception:
        pass
        #displayGrid(grid)

    if max(eCopy[0]) == mVal:
        maxPoint.append(0)
    else:
        maxPoint.append(len(eCopy) - 1)
    maxPoint.append(p[1] - 1)

    optimalGrid[maxPoint[0]][maxPoint[1]] = 0

    return createPath(maxPoint, optimalGrid, grid, eCopy, START_VALUE)

def createPath(p, opt, grid, e, START_VALUE):
    mPoint = copy.deepcopy(p)
    entrance = START_VALUE
    #print(entrance)
    directions = []

    #print(e[mPoint[0]][mPoint[1]])
    for i in range(len(e[0]) - 1):
        #print(e[mPoint[0]][mPoint[1]] - grid[mPoint[0]][mPoint[1]])
        prev = e[mPoint[0]][mPoint[1]] - grid[mPoint[0]][mPoint[1]]
        p1 = UpLeft(copy.deepcopy(mPoint), e)
        p2 = Left(copy.deepcopy(mPoint), e)
        p3 = DownLeft(copy.deepcopy(mPoint), e)

        values = [e[p1[0]][p1[1]], e[p2[0]][p2[1]], e[p3[0]][p3[1]]]

        if values[0] == prev:
            prev = e[p1[0]][p1[1]]
            mPoint = p1
            directions.insert(0, -1)
        elif values[1] == prev:
            prev = e[p2[0]][p2[1]]
            mPoint = p2
            directions.insert(0, 0)
        else:
            prev = e[p3[0]][p3[1]]
            mPoint = p3
            directions.insert(0, 1)


    if entrance[0] == 0:
        directions.insert(0, entrance[1])
        directions.insert(0, 1)
    else:
        directions.insert(0, entrance[1])
        directions.insert(0, 0)

    #print(startingPoint)

    displayGrid(e)
    print("------------------------")
    print(directions)
    return directions

def addDirections(l, e, p):
    if p[0] == 0:
        l.append(1)
    else:
        l.append(0)
    l.append(p[1])

    for i in range(len(e[0]) - 1):
        p1 = UpRight(copy.deepcopy(p), e)
        p2 = Right(copy.deepcopy(p), e)
        p3 = DownRight(copy.deepcopy(p), e)
        if e[p1[0]][p1[1]] == 0:
            l.append(1)
            p = p1
        elif e[p2[0]][p2[1]] == 0:
            l.append(0)
            p = p2
        elif e[p3[0]][p3[1]] == 0:
            l.append(-1)
            p = p3

    return l

def relaxEdges(e, p, grid, SOURCE_Y):
    p1 = UpRight(copy.deepcopy(p), grid)
    p2 = Right(copy.deepcopy(p), grid)
    p3 = DownRight(copy.deepcopy(p), grid)

    if e[p1[0]][p1[1]] == 'x' and p1[1] != SOURCE_Y:
        e[p1[0]][p1[1]] = e[p[0]][p[1]] + grid[p1[0]][p1[1]]
        ##print("HELLO1", e[p1[0]][p1[1]])

    if e[p2[0]][p2[1]] == 'x' and p2[1] != SOURCE_Y:
        e[p2[0]][p2[1]] = e[p[0]][p[1]] + grid[p2[0]][p2[1]]
        ##print("HELLO2", e[p2[0]][p2[1]])

    if e[p3[0]][p3[1]] == 'x' and p3[1] != SOURCE_Y:
        e[p3[0]][p3[1]] = e[p[0]][p[1]] + grid[p3[0]][p3[1]]
        ##print("HELLO3", e[p3[0]][p3[1]])

    return p1, p2, p3

def appendMax(e, list, p):
    a = e[p[0]][p[1] - 1]
    b = None
    if p[0] == 0:
        b = e[-1][p[1] - 1]
    else:
        b = e[0][p[1] - 1]

    list.append(max(a,b))


def markFinished(finished, unfinished, e):
    temp = 0
    transferPoint = [0, 0]
    for p in unfinished:
        if isinstance(e[p[0]][p[1]], int):
            if e[p[0]][p[1]] > temp:
                temp = e[p[0]][p[1]]
                transferPoint = p


    unfinished.remove(transferPoint)
    finished.append(transferPoint)

    return transferPoint


def markAllUnfinished(e, unfinished):
    for i in range(len(e)):
        for j in range(len(e[0])):
            unfinished.append([i, j])

def displayFinished(finished, e):
    for p in finished:
        e[p[0]][p[1]] = 'T'

    displayGrid(e)

def findStartingPoints(list, grid):

    for i in range(len(grid[0])):
        list.append([0, i])

    for i in range(len(grid[0])):
        list.append([len(grid) - 1, i])

solve(START)