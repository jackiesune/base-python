from random import randint

class Dice():
    def __init__(self,num_sides=6):
        self.num_sides=num_sides

    def throw (self):
        '''掷色子'''
        return randint(1,self.num_sides)

