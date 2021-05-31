import pandas as pd
import plotly_express as px
import csv

#with open("cups of coffee vs hours of sleep.csv", newline='') as f :
df = pd.read_csv("cups of coffee vs hours of sleep.csv") 
fig = px.scatter(df, x="Coffee in ml", y="sleep in hours") 
fig.show() 