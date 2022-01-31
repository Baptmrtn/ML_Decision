import pandas as pd
import numpy as np
import scipy as scp
import os
from time import time
import matplotlib.pyplot as plt 
import seaborn as sns
from itertools import combinations

from Functions import *
from Classes import *


#TypeML = Types_of_learning()

##############
#Unsupervised#
##############

from sklearn.datasets import load_iris 

print("Il existe plusieurs méthodes de clustering :\
		\n 1) K-means\n")

data = load_iris()
df = data.data
features_name = data.feature_names
Sample_size = df.shape[0]*df.shape[1]

choice = 1


if choice == 1 :
	print("# Vous venez de choisir L'algorithme K-Means #")
	cluster_known = input("Savez-vous le nombre de cluster souhaitez ? Y/N\n# ")
	if cluster_known == "Y":
		k = int(input("Nombre cluster :\n# "))
		kmean = KMeans_algo(Sample_size,k)
		end = "N"
		while end != "Y":
			diff = kmean.Fit_data(df)
			kmean.Evaluation_graph(df,combinations(Select_feature_graph(features_name),2))
			plt.show()
			end = input("Avez-vous terminé ? ")


	elif cluster_known == "N":

		#Methode du coude
		pass
	elif cluster_known == "QUIT":
		exit()
	else:
		print("Error, choix des réponses possible : Y/N/QUIT")




"""
kmean = KMeans_algo(Sample_size,3)
kmean.Fit_data(df)
print(features_name[0],features_name[1])
kmean.Evaluation_graph(df,features_name[0],features_name[1])
#kmean.Evaluation_metrics()
plt.show()
"""