from perceptron import Perceptron
from trainer import Trainer
from ui import UI

# perceptron1 = Perceptron()
# perceptron2 = Perceptron()
# perceptron3 = Perceptron()

trainer = Trainer(Perceptron())

ui = UI(trainer)
# trainer.printAccuracy()
print("=================================")
howManyTrainings = 1
# for i in range(howManyTrainings):
#     trainer.train()

trainingsCount = 0
maxTrainings = 3000
succeeded = False
perceptronsNeeded = 1

while not succeeded:
    newPerceptron = Perceptron()
    trainer.perceptron = newPerceptron
    trainingsCount = 0
    while trainer.test() <= 0.9:
        if trainingsCount >= maxTrainings:
            print(perceptronsNeeded, ". Max trainings reached")
            perceptronsNeeded += 1
            break
        trainer.train()
        # print(newPerceptron.weights)
        trainingsCount += 1
    else:
        succeeded = True


print("Perceptron needed to be trained " + str(trainingsCount) + " times.")
trainer.printAccuracy()

# ui.userInput()
