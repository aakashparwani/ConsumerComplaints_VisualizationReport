
# coding: utf-8

# In[1]:

import pandas as pd
import os
import plotly.plotly as py
import plotly.graph_objs as go

py.sign_in("aakashparwani", "3OQPNkJMHXeqwpjH1aYj")
complaintFile = "D:\Aakash_Documents\MS_Collections\AcceptanceFromSaintPeters\ClassStuff\DataVisualization\consumer_complaints\consumer_complaints.csv"

pwd = os.getcwd()
os.chdir(os.path.dirname(complaintFile))
complaintData = pd.read_csv(os.path.basename(complaintFile))
os.chdir(pwd)


# In[2]:

disputedata = complaintData[['consumer_disputed?','product']]


# In[3]:

disputedata= pd.DataFrame({'count' : disputedata.groupby( [ "consumer_disputed?", "product"] ).size()}).reset_index()


# In[4]:

disputedata = disputedata[(disputedata['consumer_disputed?'] == 'Yes')]


# In[5]:

x1 = disputedata['product']
y1 = disputedata['count']


# In[8]:

# Create a trace
trace = go.Scatter(
x = x1,
y = y1
)
data1 = [trace]
layout = dict(title = 'Complaints with financial products where consumers were marked disputed',
xaxis = dict(title = 'Financial Product'),
yaxis = dict(title = 'Number of Consumer Disputes'),
)
fig = dict(data=data1, layout=layout)

py.iplot(fig, filename='linechart')


# In[ ]:

py.plot(fig, filename='linechart')

