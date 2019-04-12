class checkvalidity:
    def __init__(self):
        self.num=int(input())
    def checking(self):
        if(self.num<0):
           print("invalid")
        elif(self.num%2==0):
              print("Even")
        else:
               print("Odd")
               
c1=checkvalidity()
c1.checking()
