import random
class Perceptron:
    def __init__(self):
        self.trainGroupsDict = {}
        self.testGroupsDict = {}
        self.makeGroups("train-set.csv", self.trainGroupsDict)
        self.makeGroups("test-set.csv", self.testGroupsDict)
        self.y = 0
        self.weights = []
        self.generateRandomWeights()
        self.threshold = 0
        self.bias = self.calculateBias()
        self.classes = self.getClasses()
        self.assignedClass = ""
        self.realClass = ""

    def calculateBias(self):
        sum = 0
        count = 0
        for group in self.trainGroupsDict.keys():
            for vector in self.trainGroupsDict[group]:
                formattedVec = vector.split(";")
                for val in formattedVec:
                    sum += float(val)
                    count += 1
        # print(sum)
        # print(count)
        # print((sum/count)*2)
        return (sum/count) * 2
    def getClasses(self):
        classes = []
        for group in self.trainGroupsDict.keys():
            classes.append(group)
        return classes
    def makeGroups(self, path, groupsDict):
        file = open(path)
        while True:
            line = file.readline()
            if not line:
                break
            strSplit = line.strip().split(";")
            conc = ";".join(strSplit[:-1])
            if strSplit[-1] not in groupsDict:
                groupsDict[strSplit[-1]] = []
            groupsDict[strSplit[-1]].append(conc)

    @staticmethod
    def vectorSize():
        file = open("train-set.csv")
        return len(file.readline().split(";")) - 1

    def generateRandomWeights(self):
        for i in range(Perceptron.vectorSize()):
            self.weights.append(random.random())

