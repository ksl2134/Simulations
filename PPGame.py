from numpy.random import random
import matplotlib.pyplot as plt

"""
    This script uses numpy and matplotlib modules. numpy is used for 
    generating uniformly distributed random numbers. matplotlib is used 
    for data visualization.
    
    This is basically a Monte Carlo simulation.
    Based on the probabilities of each player's winning
    a service, each ping pong game is simulated 'n' times. The player who
    reaches 15 pts first wins the game. 
    
    For a given 'n' number of simulated games, the number of winning games
    of each player is plotted and visualized in a graph and pie chart.
    
"""
    
# Asks for inputs.
def Input ():
    ProbA = input('Enter the probability of A = ')
    ProbB = input('Enter the probability of B = ')
    n = input('Enter the number of games to simulate = ')
    return n, ProbA, ProbB
    
def Intro():
    print ("Hello, this is Kaung's first Monte Carlo Simulation program"
           " in python.")
            
"""
    Player B serves first. Game point is 15. 
    A random number between 0 and 1 is generated
    and compared to ProbA or ProbB. Depending on ProbA and ProbB you entered,
    winning of each service by a player is determined. A point is counted
    and whoever reaches 15 points first wins. The winner must serve next,
    but for this game, the first servicer is player B.
"""

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
    
# Player A serves first here.   
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
    
""" 
    Each player serves first in equal number of games. For example,
    out of 1000 games, 500 will be served by player A,
    whereas the other 500 by B.
    This function counts number of wins for player A and B,
"""
    
    
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

    GameCount = [GameCountA, GameCountB]
    plt.figure()
    plt.subplot(221)
    plt.xticks((1,2), ('Games Won by A', 'Games Won by B'))
    plt.bar([1,2], GameCount, width = 0.8, color = ['lightblue','yellowgreen'], align = 'center')
    plt.subplot(223)
    sizes = [float(GameCountA), float(GameCountB)]
    colors = ['lightblue', 'yellowgreen']
    labels = ['Games Won by A', 'Games Won by B']
    plt.pie(sizes, labels = labels, colors = colors, startangle = 0 )
    plt.show()
        

def main():
    Intro()
    n, ProbA, ProbB = Input()
    GameCountA, GameCountB = SimulateNGames(n, ProbA, ProbB)
    PrintResults(n, GameCountA, GameCountB, ProbA, ProbB)
    
if __name__ == '__main__':
   main()
    
    
