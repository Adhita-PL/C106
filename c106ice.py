import pandas as pd
import plotly_express as px
import csv
import numpy as np 

#df = pd.read_csv("Ice Cream Sale vs Temperature data.csv")
#with open("Ice Cream Sale vs Temperature data.csv") as csv_file :
    #df = csv.DictReader(csv_file)
    #fig = px.scatter(df, x = "Temperature", y = "Ice-cream Sales( â‚¹ )") 
    #fig.show()  

def getDataSource(data_path) :
    ice_cream_sales = []
    temperature = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader :
            temperature.append(float(row["Temperature"]))
            ice_cream_sales.append(float(row["Ice-cream Sales( â‚¹ )"])) 
    return{"x": temperature, "y" : ice_cream_sales}

def findCorrelation(data_source) :
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correation between the temperature and icecream sales is ", correlation[0,1]) 

def main() :
    data_path = "Ice Cream Sale vs Temperature data.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)

main() 