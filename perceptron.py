from comuns import activeFunction

class Perceptron:
    def __init__(self,weights = []) -> None:
        self.weights = weights
        
    def train(self,data,learnRate,epoch):
        
        for _ in range(epoch):
            for line in data:
                inputData = line[0:-1]
                classData = line[-1]
                
                # Produto Escalar
                prod = 0
                for i in range(len(self.weights)):
                    prod += float(inputData[i]) * self.weights[i]
                
                # Função ativação
                prevClass = activeFunction(prod)
                
                # Atualizar pesos
                erro = classData - prevClass
                for i in range(len(self.weights)):
                    self.weights[i] = self.weights[i] + learnRate * erro * inputData[i]
                    prod += inputData[i] * self.weights[i]
        
    def prever(self,input):
        
        # Produto Escalar
        prod = 0
        for i in range(len(self.weights)):
            prod += input[i] * self.weights[i]
        
        # Função ativação
        return activeFunction(prod)
       