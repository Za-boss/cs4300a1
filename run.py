import argparse
from domains import wgc
from core import *
DOMAINS = {
    'wgc' : wgc.WGC(cost=0)
}
CONFIGURATIONS = {
    'conf1' : {'left': {'Farmer' : True,
                      'Wolf' : True,
                      'Goat' : True,
                      'Cabbage' : True
                      },
               'right' : {'Farmer' : False,
                      'Wolf' : False,
                      'Goat' : False,
                      'Cabbage' : False
                      }
                },
    'conf2' : {
            'left' : {'Farmer' : True,
                      'Wolf' : True,
                      'Goat' : False,
                      'Cabbage' : True
                      },
            'right' : {'Farmer' : False,
                      'Wolf' : False,
                      'Goat' : True,
                      'Cabbage' : False
                      }
                }
}
ALGORITHMS = {
    'bfsopt': BFSopt,
    'bfs': BFS,
    'ids': IDS
}
def main():
    parser = argparse.ArgumentParser(description="Agent runner")
    parser.add_argument('--domain', type=str, required=True, choices=DOMAINS.keys(), help="domain to run the algorithm in")
    parser.add_argument('--algo', type=str, required=True, choices=ALGORITHMS.keys())
    parser.add_argument('--conf', type=str, required=False, choices=CONFIGURATIONS.keys())

    args = parser.parse_args()
    domain = DOMAINS[args.domain]
    search = ALGORITHMS[args.algo]
    if (args.conf):
        domain.leftBank = CONFIGURATIONS[args.conf]['left']
        domain.rightBank = CONFIGURATIONS[args.conf]['right']
    result = search(domain)
    if result is None:
        print("no valid path found")
    else:
        print("Path:")
        for i in range(len(result[0]) - 1):
            print(f'{i+1}) {result[0][i]} --> {result[0][i+1]}')
        print(f'Domain: WGC')
if __name__ == "__main__":
    main()