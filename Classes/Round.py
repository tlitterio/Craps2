import Classes.Roll as roll
class Round(object):
    def __init__(self,id):
        self.id = id
        self.Rolls = []
        self.Open = 0
        self.Point = [int]
        self.Result = ""