import os
import csv
import sys
import glob
import math
import numpy
import numpy as np
import pandas as pd
from pandas import Series
from statsmodels.tsa.arima_model import ARIMA

def fitting_model(trainingSet, p, d, q, index):
    #gets the last point of the trainingSet, which is the n + 1 point, with n being
    #the current window. 
    pointToPredict = float(trainingSet.tail(1)['y'])
    #removing the n + 1 point so that we can train of the data set corresponding to the 
    #window size 
    trainingSet.drop(trainingSet.tail(1).index,inplace=True)
    trivialPoint = float(trainingSet.tail(1)['y'])
    #creating and training the model
    model = ARIMA(trainingSet['y'], order=(p,d,q))
    fitted_model = model.fit(disp=0)

    #forecasted value from the model
    forecastedValue = float(fitted_model.forecast()[0])

    #append return values to list to return to be printed out to the csv files
    results = []
    if not math.isnan(forecastedValue):
        #appending the index, trivial point, the actual index + 1 point, the forecated point
        results.append(int(index))
        results.append(float(str(round(float(trivialPoint), 2))))
        results.append(float(str(round(float(pointToPredict), 2))))
        results.append(float(str(round(float(forecastedValue), 2))))

        #calculating the error of the trivial and forecasted point values
        trivialPercentError = float(abs(pointToPredict - trivialPoint)/pointToPredict) * 100
        forecastPercentError = float(abs(pointToPredict - forecastedValue)/pointToPredict) * 100

        #appending the calculated points above 
        results.append(float(str(round(float(trivialPercentError), 2))))
        results.append(float(str(round(float(forecastPercentError), 2))))
        return results
        



    


    
