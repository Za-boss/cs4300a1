To run use this command:
python3 ./run.py --domain wgc --algo bfs --conf conf1
bfs can be replaced with ids and conf1 can be replaced with conf2

conf options: conf1, conf2

conf1: all objects on left side of river
conf2: goat starts on right side of the river

algo options: bfsopt, bfs, ids

bfsopt - optimized version of bfs search, prunes nodes more aggressively
bfs - basic bfs graph search
ids - iterative deepening search

conf2 places the goat on the other side of the river already