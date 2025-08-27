import argparse
def WGC():
    print("running WGC")
def IDS(domain):
    print(f"running IDS on {domain.__name__}")
def BFS(domain):
    print(f"running BFS on {domain.__name__}")
DOMAINS = {
    'wgc' : WGC
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