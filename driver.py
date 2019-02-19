import os
import csv
import sys
import glob
import numpy as numpy
import pandas as pd
from arima_model import fitting_model

modelType = str(input("What Model Type to Use? "))
startingPoint = int(input("What is the Starting Point for the Data Window? "))
windowSize = int(input("What is the Desired Window Size? "))
csvFileName = input("What is the filename? ")

p = 0
d = 0
q = 0

if str(modelType).lower() == "arima":
    p = int(input("P value? "))
    d = int(input("D value? "))
    q = int(input("Q value? "))

filename = "Data/"+csvFileName
dataframe = pd.read_csv(filename)
dataframe['ds'] = pd.to_datetime(dataframe['ds'].astype(str), format='%Y-%m-%d')

dataToCsv = []
dataToCsv.append(["Starting Index","Value @ Index + Window Size","Value @ Index + Window Size + 1","Forecasted Value","Trivial %Error", "Forecast %Error"])

trivialMean = 0.00
forecastMean = 0.00
countOfIndexes = 0

for index in range(startingPoint, len(dataframe.index) - windowSize - 1):
    #trainingSet is the dataframe which contains the points starting
    #from the current starting point to the starting pount + window size
    mask = dataframe.index.to_series().between(index,index+windowSize+1)
    trainingSet = dataframe[mask]

    dataList = fitting_model(trainingSet, p, d, q, index)

    if dataList != None:
        dataToCsv.append(dataList)
        trivialMean += dataList[4]
        forecastMean += dataList[5]
        countOfIndexes += 1
    
trivialMean /= countOfIndexes
forecastMean /= countOfIndexes

meanList = ["Averages", " ", " ", " ", float(str(round(float(trivialMean), 2))), float(str(round(float(forecastMean), 2)))]
dataToCsv.append(meanList)

newCsvFileName = str(csvFileName) + "_" + str(modelType) + "_" + str(windowSize) + "_" + str(p) + str(d) + str(q) + ".csv"
with open(newCsvFileName, "w") as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(dataToCsv)
csvFile.close()


    