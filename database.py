from sklearn.model_selection import train_test_split

IRIS_SETOSA = -1
IRIS_VERSICOLOR = 1
IRIS_VIRGINICA = 2

def normalizeClass(className:str) -> int:
    """Normalize DataBase\n
    Iris-setosa = -1\n
    Iris-versicolor = 1\n
    Iris-virginica = 2\n
    """
    classes = { 
        'Iris-setosa': IRIS_SETOSA,
        'Iris-versicolor': IRIS_VERSICOLOR, 
        'Iris-virginica': IRIS_VIRGINICA,
    }
    return classes[className]

# Read DataBase
def loadDatabase() -> tuple[list,int,int]:  
    database = []
    lines = open("./database/iris.data","r").read().splitlines()
    for line in lines:
        data = line.split(',')
        dataInputs = list(map(float,data[0:-1]))
        dataInputs.append(normalizeClass(data[-1]))
        database.append(dataInputs)
        
    return database,len(database[0])-1,len(database)

class Database:
    
    def __init__(self) -> None:
        self.data,self.inputSize,self.size = loadDatabase()
    
    def separateDatabase(self,trainRate=0.3):
        """
            Return train and test data\n
            trainRate - porcentagem destinada a treino Default: 0.3
        """
        midCut = round(len(self.data)/2)
        database0,database1 = self.data[0:midCut],self.data[midCut:midCut*2]

        train0,test0,train1,test1 = train_test_split(database0,database1,train_size=trainRate)
        
        train0.extend(train1)
        test0.extend(test1)
        
        return train0,test0
    
    def cleanDatabase(self,class2remove):
        self.data = list(filter(lambda item: item[-1] != class2remove,self.data))
        self.size = len(self.data)