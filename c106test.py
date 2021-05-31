import pandas as pd
import plotly_express as px
import csv
import numpy as np 

#df = pd.read_csv("Size of TV,_Average time spent watching TV in a week (hours).csv")
with open("Size of TV,_Average time spent watching TV in a week (hours).csv") as csv_file :
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x = "Size of TV", y = "Average time spent watching TV in a week (hours)")  
    fig.show()  