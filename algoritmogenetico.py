# Algoritmo genético adaptado para gerar pesos do perceptron
from comuns import generateWeights,activeFunction
import random

class Cromossomo:
    def __init__(self,pesos) -> None:
        self.pesos = pesos
        self.aptidao = 0 # Numero de acertos
    
    def avalia(self, database) -> None:
        
        numAcertos = 0
        for data in database:
            
            inputData = data[0:-1]
            classData = data[-1]
            
            # Produto Escalar
            prod = 0
            for i in range(len(self.pesos)):
                prod += inputData[i] * self.pesos[i]
            
            # Função ativação
            prevClass = activeFunction(prod)
            if(prevClass == classData):
                numAcertos+=1
                
        # Salvar valores no cromossomo, evitar recalcular
        self.aptidao = numAcertos

    def mutacao(self,taxaMutacao = 0.2):
        for i,_ in enumerate(self.pesos):
            probabilidade = random.random()
            if(probabilidade <= taxaMutacao):
                # Gerar número aleatorio que pode aumentar ou diminuir o valor do peso
                self.pesos[i] += random.randint(-1,1) * (random.random() * taxaMutacao)

def ordenarGrupo(grupoCromossomos) -> None:
    grupoCromossomos.sort(key= lambda item: item.aptidao, reverse=True)
    
def criarGrupoCromossomos(numCromossomos,numPesos,baseTreino):
    novoGrupo = [
        Cromossomo(generateWeights(numPesos)) for _ in range(numCromossomos)
    ]

    for cromossomo in novoGrupo:
        cromossomo.avalia(baseTreino)
    
    ordenarGrupo(novoGrupo)
    return novoGrupo

def realizaTorneio(grupoCromossomos,k = 2) -> Cromossomo:

    # Selecionar no grupo k elementos para fazer o torneio
    cromossomosSelecionados = random.choices(grupoCromossomos,k=k)

    # Seleciona o melhor
    ordenarGrupo(cromossomosSelecionados)

    return cromossomosSelecionados[0]

def cruzar(cromossomo1,cromossomo2):
    
    pontoCorte = random.randint(1,len(cromossomo1.pesos)-1)
    head1,tail1 = cromossomo1.pesos[0:pontoCorte],cromossomo1.pesos[pontoCorte:]
    head2,tail2 = cromossomo2.pesos[0:pontoCorte],cromossomo2.pesos[pontoCorte:]

    head1.extend(tail2)
    head2.extend(tail1)

    filho1 = Cromossomo(head1)
    filho2 = Cromossomo(head2)

    return filho1,filho2

def algoritmoGenetico(
        numPesos,
        basedados,
        maxTamanhoGrupo = 10,
        numeroInteracoes = 100,  
        taxaMutacao = 0.2,
    ) -> Cromossomo:
    
    # gerar grupo Inicial de soluções aleatórias, Ordenado
    grupo = criarGrupoCromossomos(
        numCromossomos=maxTamanhoGrupo,
        numPesos=numPesos,
        baseTreino=basedados
    )
    #print("Melhor cromossomo inicial: ",grupo[0].pesos,grupo[0].aptidao)
    
    # Algoritmo genetico

    # Definir número de pais que vão reproduzir
    numeroPais = 2

    for _ in range(numeroInteracoes):
        
    # Cross over

        # Selecionar os pais
        populacaoIntermediaria = []

        # Elitismo: Escolher o melhor cromossomo
        populacaoIntermediaria.append(grupo[0])

        # Realizar torneio
        while len(populacaoIntermediaria) < numeroPais:
            escolhido = realizaTorneio(grupo,2)
            populacaoIntermediaria.append(escolhido)
        
        # Cruzamento
        filhos = []
        for i in range(0,numeroPais,2):
            filhos.extend(list(cruzar(populacaoIntermediaria[i],populacaoIntermediaria[i+1])))

        # Mutação dos filhos e avaliação
        for filho in filhos:
            filho.mutacao(taxaMutacao = taxaMutacao)
            filho.avalia(basedados)

    # Reformular grupo
    
        # Substituir os piores pelos novos filhos
        pontoSeparacaoGrupo = (len(filhos)+1)*-1
        del grupo[pontoSeparacaoGrupo:-1]
        grupo.extend(filhos)
        ordenarGrupo(grupo)
        
    # endLoop Interações
    
    #Retornar o melhor cromossomo obtido
    return grupo[0]
