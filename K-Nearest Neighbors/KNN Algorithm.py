import pandas as pd

import math
import operator 
class KNN:
    k = 0
    trainX = []
    trainY = []
    testX = []
    testY = []
    predikimetY = []
    
    def __init__(self,k):
        self.k = k
        
    def distancaEuklidit(instanca1,instanca2,gjatesia):
        distanca = 0
        for i in range(gjatesia):
            distanca += pow((instanca1[i]-instanca2[i]),2)
        return math.sqrt(distanca)

    def merrFqinjet(_teDhenatTrajnueseX,_teDhenatTrajnueseY,_teDhenatPredikueseX,_k):
        distancat = []
        gjatesia = len(_teDhenatPredikueseX)-1
        for i in range(len(_teDhenatTrajnueseX)):
            dist = distancaEuklidit(_teDhenatPredikueseX, _teDhenatTrajnueseX[i],gjatesia)
            distancat.append((_teDhenatTrajnueseY[i],dist))
        distancat.sort(key=operator.itemgetter(1))
        fqinjet = []
        for i in range(_k):
            fqinjet.append(distancat[i][0])
        return fqinjet

    def vleratUnike(lista):
        vleratUnike = []
        for i in range(len(lista)):
            if lista[i] not in vleratUnike:
                vleratUnike.append(lista[i])
        return vleratUnike

    def gjejKlasen(fqinjet):
        vUnike = vleratUnike(fqinjet)
        frekuentimi = []
        for i in range(len(vUnike)):
            count = 0
            for j in range(len(fqinjet)):
                if vUnike[i]==fqinjet[j]:
                    count = count + 1
            frekuentimi.append((vUnike[i],count))
        max = frekuentimi[0][1]
        klasa = frekuentimi[0][0]
        for i in range(len(frekuentimi)):
            if max<frekuentimi[i][1]:
                max = frekuentimi[i][1]
                klasa = frekuentimi[i][0]
        return klasa
    def trajnoAlgoritmin(self,X,Y):
        self.trainX = X.as_matrix()
        self.trainY = Y.as_matrix()
        
    def prediko(self,_teDhenatPredikueseX):
        self.testX = _teDhenatPredikueseX.as_matrix()
        teDhenatPredikueseY = []
        for i in range(len(self.testX)):
            fqinjet = merrFqinjet(self.trainX,self.trainY,self.testX[i],self.k)
            predikimiKlases = gjejKlasen(fqinjet)
            teDhenatPredikueseY.append(predikimiKlases)
        self.predikimetY = teDhenatPredikueseY
   
   def predikimet(self):
        return self.predikimetY
    
    def saktesiaAlgoritmit(self,testY):
        self.testY = testY
        saktesia = 0
        for i in range(len(self.testY)):
            if self.testY[i] == self.predikimetY[i]:
                saktesia +=1
        return round((saktesia/float(len(self.predikimetY)))*100,2)


train = pd.read_csv("TrainDataTest.csv")
test = pd.read_csv("TestDataTest.csv")

trainY = train['Klasa']
trainX = train.drop('Klasa',1)

testY = test['Klasa']
testX = test.drop('Klasa',1)

objKNN = KNN(3)
objKNN.trajnoAlgoritmin(trainX,trainY)
objKNN.prediko(testX)
objKNN.saktesiaAlgoritmit(testY)
objKNN.predikimet()