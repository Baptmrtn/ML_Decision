import pandas as pd
import numpy as np
import scipy as scp
import os
from time import time
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.cluster import KMeans,MiniBatchKMeans

class KMeans_algo:

	def __init__(self,n_sample,k_cluster):
		# Initialization of parameters 
		self.k = k_cluster
		self.fig = 0
		if n_sample > 10000:
			self.algo = MiniBatchKMeans(n_clusters =self.k)
		else:
			self.algo = KMeans(n_clusters =self.k)
		

	def Set_Parameters(self):
	### Parameters initialization
		self.k = int(input("Combien de cluster souhaitez-vous obtenir ?\n"))
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
		diff = end-start
		print("Time to fit data : ",diff)
		return diff

	def Evaluation_graph(self,dataset,features):

		for x,y in features:
			self.fig += 1
			plt.figure(self.fig,figsize=(25, 8))
			#The_Scatter
			plt.scatter(x=dataset[:,x],y=dataset[:,y],c=self.algo.labels_)
			#Centroïdes
			plt.scatter(x=self.algo.cluster_centers_[:,x],y=self.algo.cluster_centers_[:,y],c = self.algo.cluster_centers_[:,x],label=["cluster " + str(i) for i in range(1,self.k+1)])
			#Add Info_paramets_right_image
			plt.text(x=plt.xlim()[1] + (plt.xlim()[1]-plt.xlim()[0])/40, y=(plt.ylim()[1]+plt.ylim()[0])/2,s=f"Inertie = {self.algo.inertia_}\nNombre Iteration = {self.algo.n_iter_}")
			plt.subplots_adjust(right=0.8)
			plt.legend()

	def Evaluation_metrics(self):
		print(self.algo.inertia_)
		print(self.algo.n_iter_)
		print(self.algo.cluster_centers_)

	def Prediction(self):	
		results = self.algo.predict(dataset)
		print(results)
