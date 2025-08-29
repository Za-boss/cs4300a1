from domains.wgc import *
def BFSopt(domain):
    path = []
    initialState = domain
    frontier = []
    frontier.append(initialState)
    seen = set()
    seen.add(initialState)
    sol_cost = 0
    nodesGenerated = 0
    nodesExpanded = 0
    maxFrontierSize = 0
    sol_depth = 0
    while frontier:
        node = frontier.pop(0)
        nodesExpanded += 1
        if node.testGoalMet():
            while node:
                path.append(node)
                sol_cost += node.cost
                node = node.parent
            sol_depth = len(path) - 1
            print("=== Optimized BFS Results ===")
            print(f"Solution Depth: {sol_depth}")
            print(f"Solution Cost: {sol_cost}")
            print(f"Nodes Generated: {nodesGenerated}")
            print(f"Nodes Expanded: {nodesExpanded}")
            print(f"Max Frontier Size: {maxFrontierSize}")
            print("===================")
            return (path[::-1], sol_cost)
        for action in node.presentActions():
            newState = node.move(action)
            if newState is None or newState.testLoss():
                continue
            newState.parent = node
            if newState not in frontier and newState not in seen:
                nodesGenerated += 1
                frontier.append(newState)
                seen.add(newState)
                maxFrontierSize = max(maxFrontierSize, len(frontier))
    return None
def BFS(domain):
    path = []
    initialState = domain
    frontier = []
    frontier.append(initialState)
    seen = set()
    seen.add(initialState)
    sol_cost = 0
    nodesGenerated = 0
    nodesExpanded = 0
    maxFrontierSize = 0
    sol_depth = 0
    while frontier:
        node = frontier.pop(0)
        nodesExpanded += 1
        if node.testLoss():
            continue
        if node.testGoalMet():
            while node:
                path.append(node)
                sol_cost += node.cost
                node = node.parent
            sol_depth = len(path) - 1
            print("=== BFS Results ===")
            print(f"Solution Depth: {sol_depth}")
            print(f"Solution Cost: {sol_cost}")
            print(f"Nodes Generated: {nodesGenerated}")
            print(f"Nodes Expanded: {nodesExpanded}")
            print(f"Max Frontier Size: {maxFrontierSize}")
            print("===================")
            return (path[::-1], sol_cost)
        for action in node.presentActions():
            newState = node.move(action)
            nodesGenerated += 1
            if newState is None:
                continue
            newState.parent = node
            if newState not in frontier and newState not in seen:
                frontier.append(newState)
                seen.add(newState)
            maxFrontierSize = max(maxFrontierSize, len(frontier))
    return None
        


def IDS(domain):
    frontier = []
    depth = 1
    sol_cost = 0
    nodesGenerated = 0
    nodesExpanded = 0
    frontierSize = 0
    while frontier != None:
        return None