import sys
import random
import math
import collections

CONSTANT_S = 2000  # Fixed value for s
DEBUG = True  # False when you submit to kattis
# function which queries the next set of neighbors from kattis
if DEBUG:
    # Generate a forest containing the multiple identical graphs.

    N = 700
    graph = [None]*N
    for i in range(0, N, 7):
        graph[i] = f"3 {i+1} {3} {i+2} {1} {i+3} {2} {i+6} {1}"
        graph[i+1] = f"3 {i} {3} {i+4} {4} {i+5} {1}"
        graph[i+2] = f"3 {i} {2} {i+6} {2} {i+2} {4}"
        graph[i+3] = f"3 {i} {2} {i+6} {2} {i+2} {4}"
        graph[i+4] = f"1 {i+1} {4}"
        graph[i+5] = f"2 {i+1} {1} {i+2} {2}"
        graph[i+6] = f"2 {i} {1} {i+3} {2}"

    def getNeighbours(node):
        line = graph[node].split()
        return [(int(line[i]), int(line[i+1])) for i in
                range(1, len(line), 2)]
    """
    N = 4
    graph = [None]*N
    graph[0] = [[1, 2]]
    graph[1] = [[0, 2]]
    graph[2] = []
    graph[3] = []
    def getNeighbours(nodeId):
        return graph[nodeId]
    """

else:
    N = int(sys.stdin.readline())  # read number of nodes from the input

    def getNeighbours(node):
        # ask kattis for the next node
        print(node)
        sys.stdout.flush()
        # read the answer we get from kattis
        line = sys.stdin.readline().split()
        # the answer has the form 'numNeighbors neighbor1 weight1 neighbor2 weight2 ...
        # we want to have a list of the form:
        #[ (neighbor1, weight1), (neighbor2, weight2) , ...]
        return [(int(line[i]), int(line[i+1])) for i in
                range(1, len(line), 2)]


if N == 0 or N == 1:
    print('end ' + str(0))
    sys.stdout.flush()
    sys.exit()


def getX():
    x = math.floor(1.0/random.random())
    # print("x "+str(x))
    if x > 100:
        x = 100
    return x


def bfs(w, X, node):
    b = 0

    explored_vertices = 0
    visited = set()
    queue = collections.deque([node])
    visited.add(node)
    while queue and X > explored_vertices:
        vertex = queue.popleft()
        explored_vertices += 1

        neighbours = getNeighbours(vertex)  # get the list of neighbors and the corresponding weights
        for neighbour in neighbours:
            # if the whole component containing the node is traversed the queue will become empty
            # and the while loop will stop before the limit is reached.
            neighbour_id, neighbour_weight = neighbour[0], neighbour[1]
            if neighbour_id not in visited and neighbour_weight <= w:
                visited.add(neighbour_id)
                queue.append(neighbour_id)

    if len(queue) == 0:
        b = 1

    return b


def approxConnectedComps(s, w):
    b = 0

    for i in range(0, s):
        node = random.randint(0, N - 1)
        X = getX()
        b += bfs(w, X, node)

    return ((1.0 * N)/s) * b


def approxMSFWeight(W, s):

    estimate_c = 0
    for w in range(1, W):
        c = approxConnectedComps(s, w)
        estimate_c += c

    # Since we want to approximate MSF, we want to find the value of
    # connected components for the max weight W, and not just for the weights
    # 1 to W-1
    NUM_T = approxConnectedComps(s, W)
    # NUM_T variable represents the amount of trees in the graph, in the original
    # algorithm it's assumed that the graph is connected. Therefor it just subtracts
    # W. Since we assume there exists a forest we subtract number of trees * W,
    # instead of just W.
    return N - (NUM_T * W) + estimate_c


def main():
    s = CONSTANT_S
    W = 4

    res = approxMSFWeight(W, s)

    print('end ' + str(res))
    sys.stdout.flush()


if __name__ == "__main__":
    main()
