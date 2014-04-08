from numpy.random import random

def Input ():
    ProbA = input('Enter the probability of A = ')
    ProbB = input('Enter the probability of B = ')
    n = input('Enter the number of games to simulate = ')
    return n, ProbA, ProbB
    
def Intro():
    print "Hello, this is Kaung's first Monte Carlo Simulation program"
    print "in python."
            

def SimulateGameBStarts(ProbA, ProbB):
    PointsA = PointsB = 0
    serving = 'B'
    while not PointsA or PointsB == 15:
        if serving == 'B':
            if random() < ProbB:
                PointsB = PointsB +1
            else:
                serving = 'A'
                #PointsA = PointsA + 1
        else:
            if random() < ProbA:
                PointsA = PointsA + 1
            else:
                serving = 'B'
                #PointsB = PointsB + 1
                
    return PointsA, PointsB

def SimulateGameAStarts(ProbA, ProbB):
    PointsA = PointsB = 0
    serving = 'A'
    while not PointsA or PointsB == 15:
        if serving == 'A':
            if random() < ProbA:
                PointsA = PointsA +1
            else:
                serving = 'B'
                #PointsB = PointsB + 1
        else:
            if random() < ProbB:
                PointsB = PointsB + 1
            else:
                serving = 'A'
                #PointsA = PointsA + 1
                
    return PointsA, PointsB

def SimulateNGames(n, ProbA, ProbB):
    GameCountA1 = GameCountB1 = 0
    GameCountA2 = GameCountB2 = 0
    for i in range(1,n/2):
            
            PointsA, PointsB = SimulateGameAStarts(ProbA, ProbB)
            if PointsA > PointsB:
                GameCountA1 = GameCountA1 +1
            else:
                GameCountB1 = GameCountB1 + 1
    for i in range(n/2,n+1):
            
            PointsA, PointsB = SimulateGameBStarts(ProbA, ProbB)
            if PointsA > PointsB:
                GameCountA2 = GameCountA2 + 1
            else:
                GameCountB2 = GameCountB2 + 1
        
    GameCountA = GameCountA1 + GameCountA2
    GameCountB = GameCountB1 + GameCountB2
            
    return GameCountA, GameCountB

def PrintResults(n, GameCountA, GameCountB, ProbA, ProbB):
    print "Number of Simulated Games: ", n
    print "Number of Games Won by A: ", GameCountA
    print "Number of Games Won by B: ", GameCountB
    print "Probability of A Winning: ", ProbA
    print "Probability of B Winning: ", ProbB

        

def main():
    Intro()
    n, ProbA, ProbB = Input()
    GameCountA, GameCountB = SimulateNGames(n, ProbA, ProbB)
    PrintResults(n, GameCountA, GameCountB, ProbA, ProbB)
    
if __name__ == '__main__':
   main()
    
    
