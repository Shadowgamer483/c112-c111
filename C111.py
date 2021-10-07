from os import name
import plotly.figure_factory as ff
import pandas as pd
import plotly.graph_objects as go
import statistics as st
import random 
import csv 

df=pd.read_csv("D:/Daksh/WhiteHatJr/C98/C111/studentMarks.csv")
data=df["Marks"].tolist()
fig=ff.create_distplot([data],["Marks for math(you all failed)"],show_hist=False)
fig.show()





mean=st.mean(data)
standarddeviation=st.stdev(data)
print("Mean is of these marks where alot failed alot passed is ....   ",mean)
print("The standard deviation of marks where alot failed alot passed is ....   ",standarddeviation)


def Rmean(counter):
    dataset=[]
    for i in range (0,counter):
        randomindex=random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)
    mean=st.mean(dataset)
    return mean
meanlist=[]
for i in range (0,1000):
    som=Rmean(100)
    meanlist.append(som)
standarddeviation1=st.stdev(meanlist)
mean=st.mean(meanlist)
print("this is the mean of sampling distribution",mean)
print("standarddeviation of sampling distribution",standarddeviation1)



one_st_start,one_st_end=mean-standarddeviation,mean+standarddeviation
two_st_start,two_st_end=mean-(2*standarddeviation),mean+(2*standarddeviation)
three_st_start,three_st_end=mean-(3*standarddeviation),mean+(3*standarddeviation)
print("standarddeviation1",one_st_start,one_st_end)

print("standarddeviation2",two_st_start,two_st_end)

print("standarddeviation3",three_st_start,three_st_end)

fig=ff.create_distplot([meanlist],["Marks for math(you all failed)"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[one_st_start,one_st_start],y=[0,0.17],mode="lines",name="standarddeviation 1 start"))
fig.add_trace(go.Scatter(x=[one_st_end,one_st_end],y=[0,0.17],mode="lines",name="standarddeviation 1 end"))
fig.add_trace(go.Scatter(x=[two_st_start,two_st_start],y=[0,0.17],mode="lines",name="standarddeviation 2 start"))
fig.add_trace(go.Scatter(x=[two_st_end,two_st_end],y=[0,0.17],mode="lines",name="standarddeviation 2 end"))
fig.add_trace(go.Scatter(x=[three_st_start,three_st_start],y=[0,0.17],mode="lines",name="standarddeviation 3 start"))
fig.add_trace(go.Scatter(x=[three_st_end,three_st_end],y=[0,0.17],mode="lines",name="standarddeviation 3 end"))

fig.show()


df=pd.read_csv("D:\Daksh\WhiteHatJr\C98\C111\d1.csv")
data=df["Math_score"].tolist()
mo1=st.mean(data)
print("this is the mean of sample one :O",mo1)

fig=ff.create_distplot([meanlist],["Student Marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[mo1,mo1],y=[0,0.17],mode="lines",name="mo1"))

fig.add_trace(go.Scatter(x=[one_st_end,one_st_end],y=[0,0.17],mode="lines",name="one_st_end"))
fig.show()
zscore1=(mean-mo1)/standarddeviation
print("ur ZSCORE1 is -_-....",zscore1)




df=pd.read_csv("D:\Daksh\WhiteHatJr\C98\C111\d2.csv")
data=df["Math_score"].tolist()
mo2=st.mean(data)
print("this is the mean of sample one :O",mo2)

fig=ff.create_distplot([meanlist],["Student Marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[mo2,mo2],y=[0,0.17],mode="lines",name="mo2"))

fig.add_trace(go.Scatter(x=[one_st_end,one_st_end],y=[0,0.17],mode="lines",name="one_st_end"))
fig.add_trace(go.Scatter(x=[two_st_end,two_st_end],y=[0,0.17],mode="lines",name="two_st_end"))

fig.show()
zscore2=(mean-mo2)/standarddeviation
print("ur ZSCORE is2 -_-....",zscore2)



df=pd.read_csv("D:\Daksh\WhiteHatJr\C98\C111\d3.csv")
data=df["Math_score"].tolist()
mo3=st.mean(data)
print("this is the mean of sample one :O",mo3)

fig=ff.create_distplot([meanlist],["Student Marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[mo3,mo3],y=[0,0.17],mode="lines",name="mo3"))

fig.add_trace(go.Scatter(x=[two_st_end,two_st_end],y=[0,0.17],mode="lines",name="two_st_end"))

fig.add_trace(go.Scatter(x=[three_st_end,three_st_end],y=[0,0.17],mode="lines",name="three_st_end"))
fig.show()
zscore3=(mean-mo3)/standarddeviation
print("ur ZSCORE3 is -_-....",zscore3)




