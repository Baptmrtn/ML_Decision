import pandas as pd
import numpy as np
import scipy as scp
import os
from time import time
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.cluster import KMeans,MiniBatchKMeans

class KMeans_algo:

	def __init__(self,n_sample):
		self.k = int(input("Combien de cluster souhaitez-vous obtenir ?\n"))
		self.init = 10
		self.max_iter = 300
		self.type_algo = "elkan"
		self.fig = 0
		if n_sample > 10000:
			self.algo = MiniBatchKMeans(n_clusters =self.k,n_init=self.init,max_iter=self.max_iter,algorithm=self.type_algo)
		else:
			self.algo = KMeans(n_clusters =self.k,n_init=self.init,max_iter=self.max_iter,algorithm=self.type_algo)
		

	def Set_Parameters(self):
	### Parameters initialization
		k = int(input("Combien de cluster souhaitez-vous obtenir ?\n"))
		n_init = int(input("Combien de fois voulez-vous que l'algorithme soit exécuté ? \n\
		~ note : Il selectionnera automatiquement le résultat le plus perfomant \n\
		~ valeur par défaut : 10\n"))
		max_iter = int(input("Quel sera le nombre maximal d'itérations par exécution ? \n\
		~ valeur par défaut : 300\n"))
		type_algo = input("Algorithme à utiliser : full ou elkan ? \n\
		~ note : full : EM classique / elkan : efficace sur données avec clusters bien définis. \n\
		~ valeur par défaut : elkan\n")
		#Apply new parameters
		self.algo.set_params(n_clusters =k,n_init=n_init,max_iter=max_iter,algorithm=type_algo)

	def Fit_data(self,dataset):
		start = time()
		self.algo.fit(dataset)
		end = time()
		print("Time to fit data : ",end-start)

	def Evaluation_graph(self,dataset,feature1,feature2):
		self.fig += 1
		plt.figure(self.fig,figsize=(25, 8))
		plt.scatter(x=dataset[:,0],y=dataset[:,1],c=self.algo.labels_)
		plt.scatter(x=self.algo.cluster_centers_[:,0],y=self.algo.cluster_centers_[:,1],c='r')
	def Evaluation_metrics(self):
		print(self.algo.inertia_)
		print(self.algo.n_iter_)
		print(self.algo.cluster_centers_)

	def Prediction(self):	
		results = self.algo.predict(dataset)
		print(results)

	#Méthodes 
	#.fit()
	#.predict() #renvoi l'index du cluster ou chaque individu appartient 
	#print(kmean.get_params())
	#start = time()
	#end = time()
	#print("Time is : ",end-start)
	#Evaluation 
		#graphique 
			#kmean.labels.
		#Measure
			#kmean.inertia_
			#kmean.n_iter