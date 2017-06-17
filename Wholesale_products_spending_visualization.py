
# coding: utf-8

# In[1]:

#import plotly library for line,bar & pie chart design
import plotly.plotly as pl
import plotly.graph_objs as gr


# In[2]:

#import pandas module to work with csv file
import pandas as pd


# In[3]:

#read csv file
wcd = pd.read_csv('Wholesale customers data.csv',delimiter=',')


# In[4]:

#fetch list of regions & channels
regions = list(wcd['Region'])
channels = list(wcd['Channel'])


# In[5]:

#DESIGN BAR CHART
# get annual spending on different products
fresh = list(wcd['Fresh'].values)
milk = list(wcd['Milk'].values)
grocery = list(wcd['Grocery'].values)
frozen = list(wcd['Frozen'].values)
paper = list(wcd['Detergents_Paper'].values)
delicassen = list(wcd['Delicassen'].values)


# In[6]:

#create traces
trace_fr = gr.Bar(
x = regions,
y = fresh,
name = 'Fresh'
)
trace_mi = gr.Bar(
x = regions,
y = milk,
name = 'Milk'
)
trace_gr = gr.Bar(
x = regions,
y = grocery,
name = 'Grocery'
)
trace_fro = gr.Bar(
x = regions,
y = frozen,
name = 'Frozen'
)
trace_pa = gr.Bar(
x = regions,
y = paper,
name = 'Detergent Papers'
)
trace_de = gr.Bar(
x = regions,
y = delicassen,
name = 'Delicassen'
)


# In[7]:

data = [trace_fr, trace_mi, trace_gr, trace_fro, trace_pa,trace_de]


# In[10]:

# Edit the layout
layout = dict(title = 'Annual Spending on Different Products in Different Regions',
xaxis = dict(title = 'Regions'),
yaxis = dict(title = 'Spending On Different Products'),
)


# In[11]:

#plot & embed in ipython notebook
fig = dict(data=data, layout=layout)
pl.iplot(fig, filename='barchart')


# Bar chart designed above explains annual spending on different types of wholesale products (Fresh, Milk, Grocery, Frozen, Detergent Papers, Delicassen) by clients of different regions.
# 
# Conclusion:-
# 1. Wholesale distributer is generating highest revenue from clients of "Region 3". As we can see that Region 3 clients has high    spending in each category products.
# 2. Region 1 & 3 has highest annual spending in fresh products category. On the other hand Region 2 has highest spending in          grocery products category.

# In[26]:

# generate bar chart in plotly
pl.plot(fig, filename='barchart')


# In[18]:

#create traces
trace_fr_ch = gr.Bar(
x = channels,
y = fresh,
name = 'Fresh'
)
trace_mi_ch = gr.Bar(
x = channels,
y = milk,
name = 'Milk'
)
trace_gr_ch = gr.Bar(
x = channels,
y = grocery,
name = 'Grocery'
)
trace_fro_ch = gr.Bar(
x = channels,
y = frozen,
name = 'Frozen'
)
trace_pa_ch = gr.Bar(
x = channels,
y = paper,
name = 'Detergent Papers'
)
trace_de_ch = gr.Bar(
x = channels,
y = delicassen,
name = 'Delicassen'
)


# In[19]:

data_channels = [trace_fr_ch, trace_mi_ch, trace_gr_ch, trace_fro_ch, trace_pa_ch,trace_de_ch]


# In[21]:

# Edit the layout
layout = dict(title = 'Annual Spending on Different Products Using Different Channels',
xaxis = dict(title = 'Channels'),
yaxis = dict(title = 'Spending On Different Products'),
)
#plot & embed in ipython notebook
fig = dict(data=data_channels, layout=layout)
pl.iplot(fig, filename='barchart-channels')


# Bar chart designed above explains annual spending on different types of wholesale products (Fresh, Milk, Grocery, Frozen, Detergent Papers, Delicassen) by clients using different channels.
# 
# Conclusion:-
# 1. For Fresh & Frozen products Channel 1 has high reliability factor.
# 2. On the other hand for Grocery & Milk products Channel 2 has high reliability factor.

# In[28]:

#DESIGN PIE CHART
# develop template for pie chart
fig_p = {
"data": [
{
"values": [fresh[-1],milk[-1],grocery[-1],frozen[-1],paper[-1],delicassen[-1]],
"labels": [
"Annual Spending On Fresh Products",
"Annual Spending On Milk Products",
"Annual Spending On Grocery Products",
"Annual Spending On Frozen Products",
"Annual Spending On Detergents and Paper Products",
"Annual Spending On Delicatessen Products"
],
"domain": {"x": [0, .48]},
"name": "Wholesale Distributor Clients",
"hoverinfo":"label+percent+name",
"hole": .4,
"type": "pie"
}],
"layout": {
"title":"Partition Of Annual Spending On Different Products",
"annotations": [
{
"font": {
"size": 20
},
"showarrow": False,
"text": "HDI",
"x": 0.20,
"y": 0.5
}
]
}
}


# In[29]:

#pie chart in ipython
pl.iplot(fig_p,filename='piechart')


# Pie chart above giving a sense of annual spending numbers on different wholesale products
# 
# Conclusion:- 
# 1. Overall highest annual Spending of 36.7% is measured on fresh products. So we can conclude that clients like fresh products of wholesale distributor.
# 2. And Delicatessent products is at the bottom of the list.

# In[30]:

#evaluate which channel and region is mostly in use
channel2 = len(wcd[wcd['Channel']==2])
channel1 = len(wcd[wcd['Channel']==1])

region3 = len(wcd[wcd['Region']==3])
region2 = len(wcd[wcd['Region']==2])
region1 = len(wcd[wcd['Region']==1])


# In[31]:

#DESIGN PIE CHART
# develop template for pie chart
fig_p_n = {
"data": [
{
"values": [channel1,channel2],
"labels": [
"Annual Usage Of Channel 1",
"Annual Usage Of Channel 2"
],
"domain": {"x": [0, .48]},
"name": "Channel Usage",
"hoverinfo":"label+percent+name",
"hole": .4,
"type": "pie"
}],
"layout": {
"title":"Annual Usage Of Channels",
"annotations": [
{
"font": {
"size": 20
},
"showarrow": False,
"text": "HDI",
"x": 0.20,
"y": 0.5
}
]
}
}


# In[37]:

#DESIGN PIE CHART
# develop template for pie chart
fig_p_n1 = {
"data": [
{
"values": [region1,region2,region3],
"labels": [
"Annual Usage Of Region 1",
"Annual Usage Of Region 2",
"Annual Usage Of Region 3"                
],
"domain": {"x": [0, .48]},
"name": "Channel Usage",
"hoverinfo":"label+percent+name",
"hole": .4,
"type": "pie"
}],
"layout": {
"title":"Annual Usage In Different Regions",
"annotations": [
{
"font": {
"size": 20
},
"showarrow": False,
"text": "HDI",
"x": 0.20,
"y": 0.5
}
]
}
}


# In[35]:

#channel usage
pl.iplot(fig_p_n,filename='piechart_channel')


# Pie chart above giving a sense of annual usage of different channels.
# 
# Conclusion:- 
# 1. Channel 1 has highest annual usage of 67.7%. With these statistics we can say that clients consider Channel 1 as more reliable than Channel 2.

# In[38]:

#region usage
pl.iplot(fig_p_n1,filename='piechart_regions')


# Pie chart above giving a sense of annual usage in different regions.
# 
# Conclusion:- 
# 1. Clients from Region 3 has highest annual spending of 71.8%. With these statistics we can say that Region 3 clients are highly satisfied with wholesale distributor.
