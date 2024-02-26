class bcolors:
    def __init__(self):
        self.b = '\033[94m' #blue
        self.g = '\033[92m' #green
        self.y = '\033[93m' #yellow
        self.E = '\033[0m' #endstyle
        self.B = '\033[1m' # Bold
        self.U = '\033[4m' #underline
    def testPrint(self):
        for i in self.__dict__:
            print(f"  {self.__dict__[i]}  {i} will display this way. {bc_.E}")

        
        
bc = bcolors()

