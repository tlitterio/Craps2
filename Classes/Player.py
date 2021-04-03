class Player(object):
    Name = str
    Purse = float
    Bets = []    

    def __init__(self,name,purse):
        self.Name = name
        self.Purse = purse
