from perceptron import Perceptron
from database import Database,IRIS_VIRGINICA
from random import sample
from algoritmogenetico import algoritmoGenetico

# Customize Project

trainRate = 0.5 # Proporção da base de dados destinada a treino
numberCromossomos = 20 # Número de cromossomos gerados
numInteracoes = 100 # Número de execuções do Algoritmo Genetico
taxaMutacao = 0.2 # Taxa que os cromossomos vão sofrer mutação

# Load database
database = Database()

# Remover classes não utilizadas
database.cleanDatabase(IRIS_VIRGINICA)

databaseTrain,databaseTest = database.separateDatabase(trainRate=trainRate)

# Criar pesos com Algoritmo Genetico 
MelhorCromosso = algoritmoGenetico(
    numPesos=database.inputSize,
    basedados=databaseTrain,
    maxTamanhoGrupo=numberCromossomos,
    numeroInteracoes=numInteracoes,
    taxaMutacao=taxaMutacao
)

print("Melhor Cromossomo: ",MelhorCromosso.pesos,MelhorCromosso.aptidao)

# Create Perceptron
perceptron = Perceptron(
    weights=MelhorCromosso.pesos # Pesos gerados pelo Algoritmo Genetico
)

# Test Perceptron
acertos = 0
erros = 0
newDatabaseTest = sample(databaseTest,k=len(databaseTest)) # Embaralhar base de teste Evitar dados todos em sequência

for test in newDatabaseTest:

    inputTest = test[0:-1]
    classReal = test[-1]
    prevision = perceptron.prever(inputTest)
    
    if(prevision == classReal):
        acertos += 1
    else:
        erros += 1

print(f"Acertos: {acertos}")
print(f"Erros: {erros}")
