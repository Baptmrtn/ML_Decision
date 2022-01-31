import pandas as pd
import numpy as np
import scipy as scp
import os
from time import time
import matplotlib.pyplot as plt 
import seaborn as sns

from Functions import *
from Classes import *


#TypeML = Types_of_learning()

##############
#Unsupervised#
##############

from sklearn.datasets import load_iris 


data = load_iris()
df = data.data
features_name = data.feature_names

print("Il existe plusieurs méthodes de clustering :\
		\n 1) K-means\n")


Sample_size = df.shape[0]*df.shape[1]


kmean = KMeans_algo(Sample_size)
"""
kmean.Fit_data(df)
print(features_name[0],features_name[1])
kmean.Evaluation_graph(df,features_name[0],features_name[1])
kmean.Evaluation_metrics()
plt.show()
"""