import pandas as pd
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics

df = pd.read_csv("newdata.csv") 
data = df["temp"].tolist() 
# If we take 100 random data points is called "sample data" 
# # Raw temperature data is called "population data" 
# # code to show the plot of raw data--------------------point 1---------------------------------
fig = ff.create_distplot([data], ["temp"], show_hist=False)
fig.show()
population_mean = statistics.mean(data) 
std_deviation = statistics.stdev(data) 
#Code to find the mean/std-dev of the raw data 
 
print("population mean:- ", population_mean)
print("std_deviation of population:- ",std_deviation)

#This is a function to get a mean of random samples
def random_set_of_mean(counter):
    dataset =[]
    for i in range(0,counter):
        randomindex = random.randint(0,len(data)-1)
        value = data[randomindex]
        dataset.append(value)
    mean = statistics.mean(dataset)

#function for a graph

def show_fig(mean_list): 
    df = mean_list 
    mean = statistics.mean(df) 
    fig = ff.create_distplot([df], ["temp"], show_hist=False) 
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))

    fig.show()

def setup():
    meanlist = []
    for i in range(0,1000):
        setofmeans = random_set_of_mean(100)
        meanlist.append(setofmeans)

    show_fig(meanlist)
    mean = statistics.mean(meanlist)
    print("meanofsamplingdistribution",mean)

setup()
def stddeviation(counter):
    dataset =[]
    for i in range(0,counter):
        randomindex = random.randint(0,len(data)-1)
        value = data[randomindex]
        dataset.append(value)
    stdev = statistics.stddeviation(dataset)
    print("stdofsamplingdistribution",stdev)

stddeviation(1000)

