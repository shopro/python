class inputOutString:

    def __init__(self):
        self.s = "Constructor"

    def getString(self):
        self.s = input("Enter String : ")   

    def printString(self):
        print("Upper Char : %s" % self.s.upper())



strObject = inputOutString()
strObject.getString()
strObject.printString()
    
