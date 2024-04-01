from perceptron import Perceptron
class Trainer:
    def __init__(self, perceptron: Perceptron):
        self.perceptron = perceptron

    def calculateNetValue(self, inputVector):
        netValue = 0
        for i in range(len(inputVector)):
            netValue += float(inputVector[i]) * self.perceptron.weights[i]
        netValue -= self.perceptron.bias
        # print("Vector")
        # print("Net Value: ",netValue)
        return netValue

    def activate(self, inputVector):
        if self.calculateNetValue(inputVector) > self.perceptron.threshold:
            self.perceptron.y = 1
        else:
            self.perceptron.y = 0

    def assignClass(self, inputVector):
        self.activate(inputVector)
        # print("Output: ",self.perceptron.y)
        if self.perceptron.y == 0:
            self.perceptron.assignedClass = self.perceptron.classes[0]
        else:
            self.perceptron.assignedClass = self.perceptron.classes[1]
        # print("Assigned Class: ", self.perceptron.assignedClass)

    def deltaFunction(self, inputVector, vectorRealClass):
        self.assignClass(inputVector)
        learningRate = 0.00001 # 0.00001
        if self.perceptron.assignedClass == vectorRealClass:
            decision = 1
        else:
            decision = -1

        inputMultipliedByLR = []
        for val in inputVector:
            newVal = float(val) * learningRate * decision
            inputMultipliedByLR.append(newVal)

        # print(inputMultipliedByLR)
        # print("+++++++++++++++++++++++")
        # print("Weights before delta: ", self.perceptron.weights)


        for i in range(len(inputMultipliedByLR)):
            self.perceptron.weights[i] += inputMultipliedByLR[i]
        self.perceptron.bias += -1 * learningRate * decision
        # print(self.perceptron.bias)

        # print("Threshold: ", self.perceptron.threshold, " + ", learningRate * decision, end="")
        # print(" = ", self.perceptron.threshold)
        #
        # print("Weights after delta: ", self.perceptron.weights)

    def train(self):
        for realClass in self.perceptron.trainGroupsDict.keys():
            for inputVec in self.perceptron.trainGroupsDict[realClass]:
                formattedInputVec = inputVec.split(";")
                self.deltaFunction(formattedInputVec, realClass)
                # print(self.perceptron.bias)
                # print(self.perceptron.weights)
                # print("Real class: ", realClass)

    def test(self):
        countCorrectPredictions = 0
        countAllPredictions = 0
        # print(self.perceptron.testGroupsDict)
        for realClass in self.perceptron.testGroupsDict.keys():
            for inputVec in self.perceptron.testGroupsDict[realClass]:
                # print(self.perceptron.weights)
                formattedInputVec = inputVec.split(";")
                countAllPredictions += 1
                self.assignClass(formattedInputVec)
                # print(self.perceptron.assignedClass)
                # print(countAllPredictions)
                # print(self.calculateNetValue(formattedInputVec))
                # print(self.perceptron.bias)
                # print(self.perceptron.weights)
                if self.perceptron.assignedClass == realClass:
                    # print("+++++++++++++++++++++++++++++")
                    # print(self.perceptron.assignedClass)
                    # print(countAllPredictions)
                    # print(self.calculateNetValue(formattedInputVec))
                    # print(self.perceptron.weights)
                    # print(realClass)
                    # print("+++++++++++++++++++++++++++++")
                    countCorrectPredictions += 1
        return countCorrectPredictions / countAllPredictions

    def testUserInput(self, inputVector):
        self.assignClass(inputVector)
        print("This vector belongs to group: ", self.perceptron.assignedClass)

    def printAccuracy(self):
        print("Accuracy: ", self.test())
