class create_funscript:
    def __init__(self, Version="1.0", Inverted="false", Range=99):
        self.header = '{"version":'+Version+',"inverted":'+Inverted+',"range":'+str(Range)+',"actions":'
        self.footer = "}"
        self.listOfActions = []
        self.timeStamp = 0
        self.out = Range
        
    def addAction(self, position, timeStamp):
        self.listOfActions.append({"pos":position,"at":timeStamp})
    
    def addPause(self, waitTime):
        self.timeStamp += waitTime
    
    def addBar(self, positionArray, timeGap):
        for position in positionArray:
            self.timeStamp += timeGap
            self.addAction(position, self.timeStamp)
    
    def addOneOne(self, timeGap):
        out = self.out
        self.addBar(['0',out,'0',out,'0',out,'0',out], timeGap)

    def addOneTwoThree(self, timeGap):
        out = self.out
        self.addBar(['0',out,'0',out,'0',out,out,out], timeGap)

    def addSawtooth(self, timeGap):
        out = self.out
        self.addBar(['75',out,'50',out,'25',out,'0',out], timeGap)
        
    def outputFile(self, path, fileName):
        with open(path + fileName + ".funscript", "w") as text_file:
            print(self.header, file=text_file)
            print(self.listOfActions, file=text_file)
            print(self.footer, file=text_file)
