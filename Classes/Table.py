import Classes.Player as pl
import Classes.Round as rnd

class Table(object):
    Players = pl.Player
    Rounds = []
    Min = int
    Max = int
    Multiple = int
    def __init__(self, players):
        self.Players = players