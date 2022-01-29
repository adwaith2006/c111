import csv
import pandas as pd 
import plotly.figure_factory as ff 
import statistics as st
import random
import plotly.graph_objects as go

df=pd.read_csv("studentMarks.csv")
data=df["Math_score"].to_list()
fig=ff.create_distplot([data],["Math_score"],show_hist=False)
#fig.show()
population_mean=st.mean(data)
print("mean of population data is:",population_mean)
standard_deviationpop=st.stdev(data)
print("standard deviation of population data is :",standard_deviationpop)

def randomSetOfMean(counter):
    data_set=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        data_set.append(value)

    mean=st.mean(data_set)
    return(mean)
 
mean_list=[]
for i in range(0,1000):
    setOfMean=randomSetOfMean(100)
    mean_list.append(setOfMean)

sample_mean=st.mean(mean_list)
print("mean of sample data is:",sample_mean)
std=st.stdev(mean_list)
print("standard deviation of sample data pyis:",std)
fig1=ff.create_distplot([mean_list],["Maths_Score"],show_hist=False)
fig1.add_trace(go.Scatter(x=[sample_mean,sample_mean],y=[0,0.20],mode="lines",name="mean"))


std1_start,std1_end=sample_mean-std,sample_mean+std
std2_start,std2_end=sample_mean-(2*std),sample_mean+(2*std)
std3_start,std3_end=sample_mean-(3*std),sample_mean+(3*std)

fig1.add_trace(go.Scatter(x=[std1_start,std1_start],y=[0,0.189],mode="lines",name="std1 start"))
fig1.add_trace(go.Scatter(x=[std1_end,std1_end],y=[0,0.189],mode="lines",name="std1 end"))
fig1.add_trace(go.Scatter(x=[std2_start,std2_start],y=[0,0.189],mode="lines",name="std2 start"))
fig1.add_trace(go.Scatter(x=[std2_end,std2_end],y=[0,0.189],mode="lines",name="std2 end"))
fig1.add_trace(go.Scatter(x=[std3_start,std3_start],y=[0,0.189],mode="lines",name="std3 start"))
fig1.add_trace(go.Scatter(x=[std3_end,std3_end],y=[0,0.189],mode="lines",name="std3 end"))
#fig1.show()

df=pd.read_csv("data1.csv")
data=df["Math_score"].to_list()
fig=ff.create_distplot([data],["data1"],show_hist=False)
mean1=st.mean(data)
print("mean of  data 1 is:",mean1)
fig.add_trace(go.Scatter(x=[sample_mean,sample_mean],y=[0,0.20],mode="lines",name="s_mean"))
fig.add_trace(go.Scatter(x=[mean1,mean1],y=[0,0.17],mode="lines",name="mean1"))
fig.add_trace(go.Scatter(x=[std1_end,std1_end],y=[0,0.189],mode="lines",name="std1 end"))

#fig.show()

df=pd.read_csv("data2.csv")
data=df["Math_score"].to_list()
fig=ff.create_distplot([data],["data2"],show_hist=False)
mean2=st.mean(data)
fig.add_trace(go.Scatter(x=[mean2,mean2],y=[0,0.17],mode="lines",name="mean2"))
fig.add_trace(go.Scatter(x=[sample_mean,sample_mean],y=[0,0.20],mode="lines",name="s_mean"))
fig.show()








