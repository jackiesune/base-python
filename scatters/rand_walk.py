from random import choice 

class RandWalk():
    '''随机漫步的类'''
    def __init__(self,num_points=1000):
        self.xvalues=[0]
        self.yvalues=[0]
        self.num_points=num_points

    def fill_walk(self):
        '''漫步的方法'''
        while len(self.xvalues)<self.num_points:
            dx=choice([1,-1])
            lx=choice([1,2,3,4])
            xvalue=dx*lx

            dy=choice([1,-1])
            ly=choice([1,2,3,4])
            yvalue=dy*ly
            
            if xvalue==0 and yvalue==0:
                continue
            nextx=self.xvalues[-1]+xvalue
            nexty=self.yvalues[-1]+yvalue
            self.yvalues.append(nexty)
            self.xvalues.append(nextx)
            







