import numpy as np
import math
import random

""""

TENNIS SIMULATOR

""""


class Tennis:

    def __init__(self, prob1, prob2, server):
        #initialise class varirables
        self.prob1 = prob1
        self.prob2 = prob2
        self.server = server

    def simGam(self):
        """ The simGam function simulates a game of tennis based on initalised probabilities of each player winning.
            
            A game is won when a player scores four (or more) points: 15, 30, 40 and the game-winning point.
            Should both players make it 40, then the score is called "deuce." Following deuce, a player must win two
            consecutive points: the first point, known as "advantage" and the game-winning point. 
            If the opposing player scores the next point, the game once again heads to deuce.
            
            prob1, prob2: are each player probabilties of wining the game. They both must satify the Probability axioms
            i.e. lie in [0,1] and union sums to one.
            
            returns: Binary (True/False) which represents whether player 2 won the game.
        """
        #intialise variables to store the scores of each player and the number of serves.
        player1_score=0
        player2_score=0

        #lets play!
        playing = True

        while playing:
            #switch the probabilities every two points (replicates change of sever in a game)
            current_prob = self.prob2 if self.server % 3 else self.prob1

            # The underlying dynamics of a game is based on whether a uniformly generated random number
            # (in the range (0,1) - representing a probability) is less than the probability of the current server winning 
            # (i.e their initialised probability) if it is player1_score inciments by one, else player 2 score increments by 1
            rand = np.random.uniform(0,1)
            
            if rand < current_prob:
                player1_score +=1
            #if its not player 2 wins the point
            else:
                player2_score += 1
            
            #add one to the sever count
            self.server += 1
            
            # Check to see if anyone has won the game (based on rules of a tennis game, explained above)
            if (max(player1_score, player2_score)>= 4 and abs(player1_score-player2_score)>= 2):
                # if someone has one we stop playing
                playing = False
                # did player2 win? (higher score)
                print(f'Game Final Score: {player1_score}-{player2_score}')
                return player1_score<player2_score
            else:
                # we continue playing
                continue


    def simSet(self):
        
        """The simSet function simulates a set of tennis based on initalised probabilities of each player winning.
        A player must win at least six games to win a set. A player must also win by two games in order to win the
        set. If a set should make it to 6-6, a tiebreak game is played to determine a winner of the set, resulting
        in a 7-6 set score.

        returns: Binary (True/False) which represents whether player 2 won the set.
        """
        #initialise game score and set_counter
        gam1=0
        gam2=0;
        set_counter = 0
        
        #lets play!
        playing = True
        while playing:
            print('')
            print('SET: ', set_counter)
            
            #did player 2 win the current game?
            current_game = self.simGam()
            if current_game:
                gam2 += 1
            else:
                gam1 += 1
            set_counter += 1
            
            #check to see if set over
            if (max(gam1, gam2)>6 and abs(gam1-gam2)>2):
                playing = False
                # did player 2 win the set?
                print(' ')
                print(f'Set Final Score: {gam1}-{gam2}')
                return gam1<gam2
            #tiebreak set
            if (gam1, gam2) == (6,6):
                print(f'Tiebreak Game! {gam1}-{gam2}')
                tie_break = self.simGam()
                if tie_break:
                    gam2 +=1 
                else:
                    gam1 +=1
                print(' ')
                print(f'Set Final Score: {gam1}-{gam2}')
                return gam1<gam2

    def simMat(self): 

        """The simMatch function simulates a match of tennis based on initalised probabilities of each player winning.
        A match is complete when a player reaches three sets.

        returns: Binary (True/False) which represents whether player 2 won the match.
        """ 
        #initilise set
        set1=0
        set2=0
        match_counter=0
        
        playing = True
        while playing:
            print('')
            print('MATCH: ', match_counter)
            print('')
            current_set = self.simSet()
            if current_set:
                set2 += 1
            else:
                set1 += 1
            
            match_counter += 1
            #is the match over?
            if (max(set1, set2)==3):
                playing = False

                #player 2 wins Match
                print(' ')
                print(f'Playing finished! FINAL MATCH SCORE: {set1}-{set2}')
                return set1<set2

# function to compute the possion distribution
def pois(lamb, k):
    if k==1:
        return np.exp(lamb)
    else:
        return ((lamb**k) / np.math.factorial(k) * np.exp(-lamb))



if __name__ == "__main__":

    #caluculate probabilites of each player winning via possion dist
    pFedererWin=0.6
    pNadalWin=0.4
    # initialise the server with a rangom interger - used in SimGam to determine who serves first
    server = math.floor(random.randint(0,9) + 1 / 2)
    

    #LETS PLAY TENNIS 
    game = Tennis(pNadalWin, pFedererWin, server)
    if game.simMat():
        print("Nadal wins!")
    else:
        print("Federer wins!")
