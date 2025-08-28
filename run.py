import argparse
from domains import wgc
from core import *
DOMAINS = {
    'wgc' : wgc.WGC()
}
ALGORITHMS = {
    'bfs': BFS,
    'ids': IDS
}
def main():
    parser = argparse.ArgumentParser(description="Agent runner")
    parser.add_argument('--domain', type=str, required=True, choices=DOMAINS.keys(), help="domain to run the algorithm in")
    parser.add_argument('--algo', type=str, required=True, choices=ALGORITHMS.keys())

    args = parser.parse_args()
    domain = DOMAINS[args.domain]
    search = ALGORITHMS[args.algo]
    search(domain)
if __name__ == "__main__":
    main()