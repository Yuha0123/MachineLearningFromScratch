#!/usr/bin/env python
# coding: utf-8

# In[39]:


####################################################################################
# File Name : hw#1                                                                 #  
# Date  : 2020/07/19                                                               #  
# OS : Windows 10                                                                  #  
# Author : 권지윤                                                                  #
# -------------------------------------------------------------------------------  #  
# requirements : python 3                                                          #
#                                                                                  #
####################################################################################   

import random                      
import numpy as np                 
import pandas as pd                 
import matplotlib.pyplot as plt    
import warnings                     

try:
    from sklearn.cluster import KMeans  # check installation of sklearn
except:
    print("Not installed scikit-learn.") 
    pass



if __name__ == '__main__': # Start from main
    data = pd.read_csv("./data.csv")


    Sepal_Width = data['Sepal width'].to_numpy()
    Sepal_Length = data['Sepal length'].to_numpy()

    plt.scatter(Sepal_Width, Sepal_Length, cmap = plt.cm.Blues,  marker="o", alpha = 0.5)
    plt.title("from scikit-learn library")
    plt.xlabel("sepal length (cm)")
    plt.ylabel("sepal width (cm)")
    plt.show() # show plot
    
    
    


# In[20]:


data['Sepal width']


# In[11]:





# In[ ]:




