import sys
import os

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

        return result
    
    def succAndProbReward(self, state, action):
        result = []

        if action == 'Walk' and state+1 <= self.N:
            result.append((state+1, 1., -1.))
        elif action == 'Tram' and state*2 <= self.N:
            result.append((state*2, .5, -2.))
            result.append((state, .5, -2.))        
        return result
    
    def discount(self):
        return 1
    def states(self):
        return range(1, self.N+1)

def ValueIteration(mdp):
    #Initialize
    V = {} #State -> Vopt[state]
    for state in mdp.states():
        V[state] = 0.
    
    def Q(state, action):
        return sum(prob * (reward + mdp.discount() * V[new_state]) for new_state, prob, reward in mdp.succAndProbReward(state, action))
                   
    while True:
        #Compute the new values (newV) given to the old values
        newV = {}
        for state in mdp.states():
            if mdp.isEnd(state):
                newV[state] = 0
            else:
                newV[state] = max(Q(state, action) for action in mdp.actions(state))
        #Check for convergence
        if max(abs(V[state] - newV[state]) for state in mdp.states()) <1e-10:
            break
        V = newV 

        #Read out policy
        pi = {}
        for state in mdp.states():
            if mdp.isEnd(state):
                pi[state] = 'None'
            else:
                pi[state] = max((Q(state, action), action) for action in mdp.actions(state))[1]

        os.system('cls')
        print('{:15} {:15} {:15}'.format('s', 'v(s)', 'pi(s)'))
        for state in mdp.states():
            print('{:15} {:15} {:15}'.format(state, V[state], pi[state]))




mdp = TransportationMDP(N= 200)
# print(mdp.actions(8))
# print(mdp.succAndProbReward(5, 'Tram'))
# print(mdp.states())
ValueIteration(mdp)
