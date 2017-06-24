
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd


# In[2]:

data = pd.read_csv("./dat/exp.csv",sep=',', header=None) #10選2


# In[3]:

data.sort_values(1)
data = data.fillna(0)


# In[4]:

data


# In[5]:

# domain = data.get(0) # no use
course = data.get(1)
prof = data.get(2)
recom = data.get(3)
content1 = data.get(4)
content2 = data.get(5)


# In[6]:

f = open('./result/exp.md', 'w')


# In[9]:

for i in range(len(data)):
    f.write("> " + str(course[i]) + "\n\n")
    f.write("* 開課教授：" + str(prof[i]) + "\n")
    f.write("* 相關領域：" + str(recom[i]) + "\n")
    f.write("* 課程小卦：\n")
    if content1[i] != 0:
        tmp = content1[i].replace('\n', '')
        f.write("  1. " + tmp + "\n")
    if content2[i] != 0:
        tmp = content2[i].replace('\n', '')
        f.write("  2. " + tmp + "\n")
    f.write("\n")


# In[ ]:



