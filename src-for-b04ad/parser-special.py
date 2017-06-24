
# coding: utf-8

# In[3]:

import numpy as np
import pandas as pd


# In[4]:

data = pd.read_csv("./dat/1.csv",sep=',', header=None) #專題


# In[5]:

data.sort_values(1)
data = data.fillna(0)


# In[6]:

data


# In[7]:

prof = data.get(0)
domain = data.get(1)
content1 = data.get(2)


# In[8]:

f = open('./result/1.md', 'w')


# In[9]:

for i in range(len(data)):
    f.write("> " + prof[i] + "\n\n")
    f.write("* 相關領域：" + str(domain[i]) + "\n")
    f.write("* 專題小卦：\n")
    if content1[i] != 0:
        tmp = content1[i].replace('\n', '')
        f.write("  1. " + tmp + "\n")
    f.write("\n")


# In[ ]:



