import pandas as pd

train = pd.read_csv("TeDhenatTrajnuese.csv")
test = pd.read_csv("TeDhenatTestuese.csv")

trainY = train['Klasa']
trainX = train.drop('Klasa',1)

testY = test['Klasa']
testX = test.drop('Klasa',1)

objKNN = KNN(3)
objKNN.trajnoAlgoritmin(trainX,trainY)
objKNN.prediko(testX)
objKNN.saktesiaAlgoritmit(testY)
objKNN.predikimet()
