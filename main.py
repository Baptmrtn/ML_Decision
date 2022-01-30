import pandas as pd
import numpy as np
import os
#from tkinter import filedialog
from Functions import *



#PROBLEM MACHINE LEARNING
def Types_of_learning():
	VarCheck = False
	while VarCheck != True:
		print("Sélectionner : \n- Supervised Machine Learning : 1 \n- Unsupervised Machine Learning : 2 \n(Entrez QUIT si vous souhaitez quitter le programme)\nVotre Choix :")
		TypeML = input()
		if TypeML == 1 or TypeML == 2:
			print("Validate")
			VarCheck = True
		elif TypeML == "QUIT":
			exit()
		else:
			print("Erreur, tu n'a pas sélectionner 1 ou 2")
