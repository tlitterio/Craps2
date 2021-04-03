class Bet(object):
    BetType = str
    Amount = int
    def __init__(self,bettype,amount):
        self.BetType = bettype
        self.Amount = amount