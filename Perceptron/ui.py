from trainer import Trainer
from perceptron import Perceptron
class UI:

    def __init__(self, trainer: Trainer):
        self.trainer = trainer
    def userInput(self):
        inputVec = input("Please enter " + str(Perceptron.vectorSize()) + " numbers separeted by spaces.\n\n")
        formattedInputVec = inputVec.split(" ")
        while len(formattedInputVec) != Perceptron.vectorSize():
            print("Invalid input!")
            inputVec = input("Please enter " + str(Perceptron.vectorSize()) + " numbers separeted by spaces.\n\n")
            formattedInputVec = inputVec.split(" ")
        for val in formattedInputVec:
            val = float(val)
        self.trainer.testUserInput(formattedInputVec)
