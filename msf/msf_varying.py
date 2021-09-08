import sys
import random
import math
import collections

DEBUG = True  # False when you submit to kattis
# function which queries the next set of neighbors from kattis
if DEBUG:
    W = 4
    aprox = 1.2
    # Generate a forest containing the multiple identical graphs.
    # """
    N = 7000
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
    aprox = float(sys.stdin.readline())
    W = int(sys.stdin.readline())
    queried_nodes = {}

    def getNeighbours(node):
        if node in queried_nodes:
            neighbours = queried_nodes[node]
        else:
            # ask kattis for the next node
            print(node)
            sys.stdout.flush()
            # read the answer we get from kattis
            line = sys.stdin.readline().split()
            # the answer has the form 'numNeighbors neighbor1 weight1 neighbor2 weight2 ...
            # we want to have a list of the form:
            #[ (neighbor1, weight1), (neighbor2, weight2) , ...]
            neighbours = [(int(line[i]), int(line[i+1])) for i in range(1, len(line), 2)]
            queried_nodes[node] = neighbours

        return neighbours


def bfs(w, X, node):
    b = 0
    visited = set()
    explored_vertices = 0

    visited.add(node)
    queue = collections.deque([node])
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
        X = math.floor(1.0/random.random())
        b += bfs(w, X, node)

    return ((1.0 * N)/s) * b


def approxMSFWeight(W, s):

    estimate_c = 0
    for w in range(1, W):
        c = approxConnectedComps(s, w)
        estimate_c += c
        # print(f"{w}: {c}")

    # print(f"Sum of c: {estC}")
    # Since we want to approximate MSF, we want to find the value of
    # connected components for the max weight W, and not just for the weights
    # 1 to W-1
    NUM_T = approxConnectedComps(s, W)
    # print(f"NUM_T: {NUM_T}")
    # NUM_T variable represents the amount of trees in the graph, in the original
    # algorithm it's assumed that the graph is connected. Therefor it just subtracts
    # W. Since we assume there exists a forest we subtract number of trees * W,
    # instead of just W.
    return N - (NUM_T * W) + estimate_c


def main():
    epsilon = aprox - 1
    s = math.ceil(W**2 / (epsilon ** 2))

    res = approxMSFWeight(W, s)

    print('end ' + str(res))
    sys.stdout.flush()


if __name__ == "__main__":
    main()
