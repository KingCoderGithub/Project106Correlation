import csv
from xml.etree.ElementPath import find
import plotly_express as px
import csv
import numpy as np

def plotFigure(dataPath) :
    with open(dataPath) as csv_files:
        df = csv.DictReader(csv_files)
        fig = px.scatter(df, x="Marks In Percentage", y="Days Present")
        fig.show()
    
def getDataSource(dataPath) :
    data1Sales = []
    data2Sales = []
    with open(dataPath) as csv_files:
        csv_reader = csv.DictReader(csv_files)
        for row in csv_reader:
            data1Sales.append(float(row["Marks In Percentage"]))
            data2Sales.append(float(row["Days Present"]))
            
    return{"x" : data1Sales, "y" : data2Sales}

def findCorrelation(dataSource) :
    
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("This is the Correlation : " , correlation[0, 1])
    
dataPath = "data1.csv"
dataSource = getDataSource(dataPath)
findCorrelation(dataSource)
plotFigure(dataPath)