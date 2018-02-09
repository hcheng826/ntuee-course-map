
# coding: utf-8

# In[129]:

import numpy as np
import pandas as pd


# In[130]:

data = pd.read_csv("../dat/elective.csv",sep=',', header=None)


# In[131]:

data.sort_values(1)
data = data.fillna(0)


# In[132]:


# In[133]:

category = data.get(0) # no use
domain = data.get(1) # by hand, no program
course_name = data.get(2)
prof = data.get(3)
recom = data.get(4)
pre_study = data.get(5)
content1 = data.get(6)
content2 = data.get(7)
content3 = data.get(8)


# In[134]:

f = open('../result/elective.md', 'w')


# In[135]:

for i in range(len(data)):
    f.write("> " + course_name[i] + "\n\n")
    f.write("* 開課教授：" + str(prof[i]) + "\n")
    if recom[i] != 0:
        f.write("* 推薦同時修習的課程：" + str(recom[i]) + "\n")
    if pre_study[i] != 0:
        f.write("* 推薦預先修習的課程：" + str(pre_study[i]) + "\n")
    f.write("* 課程小卦：\n")
    if content1[i] != 0:
        tmp = content1[i].replace('\n', '')
        f.write("  1. " + tmp + "\n")
    if content2[i] != 0:
        tmp = content2[i].replace('\n', '')
        f.write("  2. " + str(content2[i]) + "\n")
    if content3[i] != 0:
        tmp = content3[i].replace('\n', '')
        f.write("  3. " + str(content3[i]) + "\n")
    f.write("\n")

