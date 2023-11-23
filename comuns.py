# Funções comuns aos algoritmos
from random import seed,uniform
from database import IRIS_SETOSA,IRIS_VIRGINICA,IRIS_VERSICOLOR
#seed(123)

def generateWeights(nInputs:int) -> list:
    randomWeights = []
    for _ in range(nInputs):
        randomWeights.append(uniform(-1,1))
    return randomWeights

def activeFunction(value):
    if(value > 0):
        return IRIS_VERSICOLOR
    else:
        return IRIS_SETOSA