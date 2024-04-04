import sys
#import util

sys.setrecursionlimit(1000)


class TransportationMDP(object):
    def __init__(self, N):
        # N = No of blocks
        self.N = N

    def startState(self):
        return 1

    def isEnd(self, state):
        return state == self.N
    
    def actions(self, state):
        # Returns a list of valid actions
        result = []
        if state+1 <= self.N:
            result.append('Walk')
        if state*2 <= self.N:
            result.append('Tram')
        else:
            result.append(('Don\'t move'))
        

        return result
    
    def succAndProbReward(self, state, action):
        result = []

        if action == 'Walk' and state+1 <= self.N:
            result.append((state+1, 1., -1.))
        elif action == 'Tram' and state*2 <= self.N:
            result.append((state*2, .5, -2.))
            result.append((state, .5, -2.))
        else:
            result.append(('You can\'t go any further like that'))
        
        return result
    
    def discount(self):
        return 1
    def states(self):
        return range(1, self.N+1)
    
mdp = TransportationMDP(N= 10)
print(mdp.actions(5))
print(mdp.succAndProbReward(5, 'Tram'))
print(mdp.states())