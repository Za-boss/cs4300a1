class WGC():
    def __init__(self, 
                parent = None,
                leftBank={'Farmer' : True,
                    'Wolf' : True,
                    'Goat' : True,
                    'Cabbage' : True
                    }, 
                rightBank={'Farmer' : False,
                    'Wolf' : False,
                    'Goat' : False,
                    'Cabbage' : False
                    },
                goalBank=None,
                cost=1
                ):
        self.leftBank = leftBank
        self.rightBank = rightBank
        # 1 = right bank goal 0 = left bank goal
        self.goalBank = goalBank if goalBank else (1 if leftBank['Farmer'] else 0)
        self.parent = parent if parent else None
        self.cost = cost
    def presentActions(self):
        bank = self.leftBank if self.leftBank['Farmer'] else self.rightBank
        return [obj for obj in bank if obj != 'Farmer' and bank[obj]]
    def move(self, item):
        left_copy = self.leftBank.copy()
        right_copy = self.rightBank.copy()

        farmerLeft = self.leftBank['Farmer']

        src = left_copy if farmerLeft else right_copy
        dst = right_copy if farmerLeft else left_copy

        src['Farmer'] = False
        dst['Farmer'] = True

        if item and item != 'Farmer':
            if not src[item]:
                return None
            src[item] = False
            dst[item] = True
        return WGC(parent=self, leftBank=left_copy, rightBank=right_copy, goalBank=self.goalBank)
    def testGoalMet(self):
        goalBank = self.rightBank if self.goalBank else self.leftBank
        return all(goalBank[item] for item in ['Farmer', 'Wolf', 'Goat', 'Cabbage'])
    def bankIsDangerous(self, bank):
        farmer = bank['Farmer']
        wolf = bank['Wolf']
        goat = bank['Goat']
        cabbage = bank['Cabbage']
        if not farmer:
            if wolf and goat:
                return True
            if goat and cabbage:
                return True
        return False
    
    def testLoss(self):
        return self.bankIsDangerous(self.leftBank) or self.bankIsDangerous(self.rightBank)
    def __eq__(self, other):
        if not isinstance(other, WGC):
            raise NotImplemented
        return (self.leftBank == other.leftBank and self.rightBank == other.rightBank)
    
    def __hash__(self):
        left_items = frozenset(self.leftBank.items())
        right_items = frozenset(self.rightBank.items())
        return hash((left_items, right_items))
    
    def __str__(self):
        return (f'({'L' if self.leftBank['Farmer'] else 'R'}, {'L' if self.leftBank['Wolf'] else 'R'}, {'L' if self.leftBank['Goat'] else 'R'}, {'L' if self.leftBank['Cabbage'] else 'R'})')
# alr this thing is probably riddled with bugs that I'll have to iron out, but it's a good starting place for now