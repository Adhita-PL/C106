import csv
import numpy as np

def getDataSource(data_path) :
    size_of_tv = []
    average_time = []
    with open(data_path) as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            size_of_tv.append(float(row["Size of TV"]))
            average_time.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
    return{"x" : size_of_tv, "y" : average_time}
    
def findcorrelation(data_source) :
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print("Correlation between the size of tv and Average time spent watching TV in a week (hours) is", correlation[0,1])

def main() :
    data_path = "Size of TV,_Average time spent watching TV in a week (hours).csv"
    data_source = getDataSource(data_path)
    findcorrelation(data_source)

main() 