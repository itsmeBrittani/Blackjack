# flesh out functions
# fully create classes
# ace check after get functions working
# be sure to use input
class Player:
    def __init__(self, hand, score=0):
        self.hand = hand
        self.score = score

class CPU(Player):
    pass


# cpu_hand = []
# player_hand = []
# cpu_score = 0
# player_score = 0

deck = {AH: 11, AS: 11, AD: 11, AC: 11, H1: 1, H2: 2, H3: 3, H4: 4, H5: 5, H6: 6, H7: 7, H8: 8, H9: 9, HJ: 10, HQ: 10, HK: 10, S1: 1, S2: 2, S3: 3, S4: 4, S5: 5, S6: 6, S7: 7, S8: 8, S9: 9, SJ: 10, SQ: 10, SK: 10, D1: 1, D2: 2, D3: 3, D4: 4, D5: 5, D6: 6, D7: 7, D8: 8, D9: 9, DJ: 10, DQ: 10, DK: 10, C1: 1, C2: 2, C3: 3, C4: 4, C5: 5, C6: 6, C7: 7, C8: 8, C9: 9, CJ: 10, CQ: 10, CK: 10}

def draw():
    pass
#pick two random cards from the deck for both hands

def ace_check():
#check if there is already an 11 in hand
#if yes, new 11 equals 1
    pass


def check_score():
    #if player score higher than 21 - Game Over you lose
    #if CPU score higher than 21 - Game Over you win
    #if CPU score 16 or lower - draw
    #if CPU score 17 - 21 - check for winner
    pass

def winner_check():
    #
    pass

def hit_me():
    pass

def lets_stay():
    pass

