import Classes.Round as rnd
import random as rand
import Classes.Roll as roll

def Craps(_Table,Rounds):
    counter = 0 
    while counter < Rounds:
        i = 0
        _Round = NewRound(counter)
        _Round = PlayRound(_Round)
        _Table.Rounds.append(_Round)
        counter+=1
        Rounds-=1
    return _Table

def PlayRound(_Round):
    del _Round.Point
    _Round.Point = []
    while _Round.Open == 0:
        _roll = RollDice()
        _Round.Rolls.append(_roll)
        if (int(_roll.Dice) in range(4,7) or int(_roll.Dice) in range(8,11)): 
            _Round.Point.append(_roll.Dice)
            if _roll.Dice == _Round.Point[0]:
                _Round.Point = [0]
                _roll.Result = "Point Wins"
            elif _Round.Point[0] != 0:
                if _Round.Point.count(_roll.Dice) % 2 == 0: 
                    _roll.Result = "Come Win"
                else:
                    _roll.Result = "Come"
            else:
                _Round.Point[0] = _roll.Dice
                _roll.Result = "Point"
        elif (_Round.Point[0]) == 0 and (_roll.Dice == 2 or _roll.Dice == 3 or _roll.Dice == 12):
            _roll.Result = "Craps"
        elif (_Round.Point[0]) == 0 and _roll.Dice == 7 or _roll.Dice == 11:
            _roll.Result = "Natural"
        elif (_Round.Point[0]) > 3 and _roll.Dice == 7:
            _Round.Open = 1
            _Round.Point = [0]
            _roll.Result = "Out"

        else: _roll.Result = "End"
        print(_Round.Point.count(_roll.Dice))

    return _Round

def RollDice():
    Die1 = rand.randint(1,6)
    Die2 = rand.randint(1,6)
    Dice = Die1+Die2
    Point = 0
    Result = ""
    if (Die1==Die2): Hard = 1
    else: Hard = 0
    _roll = roll.Roll(Die1,Die2,Dice,Hard,Point,Result)
    return _roll


def NewRound(id):
    _round = rnd.Round(id)
    return _round
