class Alphab:
    def __init__(self):
        self.alphabets="abcdefghijklmnopqrstuvwxyz"
        self.inp=input()
    def checkalpha(self):
        if(self.inp in self.alphabets):
            print("Alphabet")
        else:
            print("No")

a1= Alphab()
a1.checkalpha()
