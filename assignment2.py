import random

class Dice: 
    """
    To handle randomly generating integer values 1-6.
    """
    def __init__(self):
        self._value=0
        self.roll()

    def  roll(self):
        ''' To roll the dice'''
        self._value=random.randint(1,6)

    def get_value(self):
        '''values after rolling the dice'''
        return self._value
        
class DiceCup: 
    """
    To handle five dice of the class Dice. Also banks and release the dice individually and
    can also roll dice which are not banked yet.
    """
    def __init__(self,num):
        self._dices=[]
        self._cup=[False,False,False,False,False]
        for dice in range(num):
            self._dices.append(Dice())

    def roll(self):
        '''roll the objects of Dice class'''
        for lst in range(0,5):
            if self._cup[lst]==False:
                self._dices[lst].roll()

    def value(self,index):
        '''Value method for taking the value of dice based on index'''
        return self._dices[index].get_value()

    def bank(self,index):
        '''
        Holding a paticular dice based on the index
        '''
        self._cup[index]=True

    def is_banked(self,index):
        '''
        For checking weather a paticular index position is banked or not
        '''
        if self._cup[index]==True:
            return True
        else:
            return False

    def release(self,index):
        '''Releasing the banked dice of paticular index'''
        self._cup[index]==False

    def release_all(self):
        '''To release all the banked dice'''
        for lst in range(5):
            self._cup[lst]=False

class PlayerRoom:
    """
    Handles no. of players and the game. Letting each player to play in every round 
    later checks if any player has the winning score.
    """
    def __init__(self):
        self._players=[]

    def set_game(self,p1):
        '''Set the game called ShipOfFoolsGame'''
        self._game=p1

    def add_player(self,p2):
        '''Adding the players'''
        self._players.append(p2)

    def reset_scores(self):
        '''Reset scores of the players'''
        for ply in range(len(self._players)):
            self._players[ply].reset_score()

    def play_round(self):
        '''player_round in Player class'''
        for ply in self._players:
            ply.play_round(self._game)

    def game_finished(self):
        '''To check the score of each player if 21 or not'''
        sample_lst=[]
        for ply in self._players:
            sample_lst.append(ply.current_score())
        if max(sample_lst)>=21:
            return True
        else:
            return False

    def print_scores(self):
        '''Current score of each player'''
        for scr in range(len(self._players)):
            print(self._players[scr]._name ,"score is:", self._players[scr].current_score())

    def print_winner(self):
        '''checks the score of each player and print the winner'''
        for win in range(len(self._players)):
            if win<1:
                if self._players[win].current_score()>=21 and self._players[win+1].current_score()>=21:
                    print("------DRAW------")
                    break
            if self._players[win].current_score()>=21:
                print("------ winner is:",self._players[win]._name,"-------")
                break

class ShipOfFools:
    """
    Maintains the game logic 
    Play a round of game resulting in score. 
    explains how accumulated score results in a winning state, 
    for example 21.
    """
    def __init__(self):
        self.winningscore=21
        self._cup=DiceCup(5)

    def round(self):
        """
        allows each player to play a round
        """
        self._cup.release_all()
        has_ship = False
        has_captain = False
        has_crew = False
        crew = 0
        self._cup.roll()
        for rnd in range(3):
            sample_lstp=[]
            count=0
            while count<5:
                sample_lstp.append(self._cup._dices[count].get_value())
                count=count+1
            print(sample_lstp)
            if not (has_ship) and (6 in sample_lstp):
                for i in range(5):
                    if sample_lstp[i]==6:
                        self._cup.bank(i)
                        break
                has_ship = True
            else:
                if has_ship:
                    pass
                else:
                    self._cup.roll()
            if (has_ship) and not (has_captain) and (5 in sample_lstp):
                for i in range(5):
                    if sample_lstp[i]==5:
                        self._cup.bank(i)
                        break
                has_captain = True
            else:
                if has_captain:
                    pass
                else:
                    self._cup.roll()
            if has_captain and not has_crew and (4 in sample_lstp):
                for i in range(5):
                    if sample_lstp[i]==4:
                        self._cup.bank(i)
                        break
                has_crew = True
            else:
                if has_crew:
                    pass
                else:
                    self._cup.roll()
            if has_ship and has_captain and has_crew:
                if rnd<2:
                        for j in range(5):
                            if self._cup._dices[j].get_value()>3:
                                self._cup.bank(j)
                            else:
                                self._cup.roll()
                elif rnd==2:
                    for j in range(5):
                        if self._cup.is_banked(j):
                            pass
                        else:
                            self._cup.bank(j)
        if has_ship and has_captain and has_crew:
            crew = sum(sample_lstp) - 15
            print("crew:",crew)
            return crew
        else:
            print("crew:",crew)
            return crew

class Player:
    """
    score of the individual player. 
    game logic, play a round of a game. 
    accumulates gained score in attribute score.
    """
    def __init__(self,playername):
        self._name=self.set_name(playername)
        self._score=0

    def set_name(self,namestring):
        '''to set name for the player'''
        return namestring

    def current_score(self):
        '''eventually updates the score of each player and to store'''
        return self._score

    def reset_score(self):
        ''' to reset the score of the player to 0'''
        self._score=0

    def play_round(self, gameround):
        '''allow to play game in rounds'''
        round1 = gameround
        self._score = self._score + round1.round()

if __name__ == "__main__":
    room = PlayerRoom()
    room.set_game(ShipOfFools())
    room.add_player(Player("p1"))
    room.add_player(Player("p2"))
    room.reset_scores()
    while not room.game_finished():
        room.play_round()
        room.print_scores()
    room.print_winner()      
