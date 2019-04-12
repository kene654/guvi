class leapyr:
    def __init__(self):
        self.year= int(input())
    def find(self):
        if((self.year)%4==0 and (self.year)%100!=0):
            print("yes")
        else:
            print("no")

lp= leapyr()
lp.find()
