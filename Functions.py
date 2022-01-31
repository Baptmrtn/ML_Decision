from tkinter import filedialog

#####################
#### Import data ####
#####################

def OpenCSV():
	#pour que l'utilisateur puisse choisir son fichier CSV
	file = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select a CSV file",filetypes = (("csv files",".csv"),("all files",".*")))

	if file.endswith(".csv"):
		data = np.array(pd.read_csv(file, error_bad_lines=False,encoding = "ISO-8859-1",sep=";"))
	elif UnboundLocalError :
		print("Le Fichier sélectionner n'est pas un fichier de type CSV")
	else:
		pass

	return data


def OpenExcel():
	#pour que l'utilisateur puisse choisir son fichier excel
	file = filedialog.askopenfilename(initialdir = os.getcwd(),title = "Select a CSV file",filetypes = (("Excel files",".xlsx"),("all files",".*")))

	if file.endswith(".xlsx"):
		data = np.array(pd.read_excel(file, error_bad_lines=False,encoding = "ISO-8859-1",sep=";"))
	elif UnboundLocalError :
		print("Le Fichier sélectionner n'est pas un fichier de type XLSX (Excel)")
	else:
		pass
	return data

#####################
#### Data choice ####
#####################

#PROBLEM MACHINE LEARNING
def Types_of_learning():
	VarCheck = False
	while VarCheck != True:
		print("Sélectionner : \n- Supervised Machine Learning : 1 \n- Unsupervised Machine Learning : 2 \n(Entrez QUIT si vous souhaitez quitter le programme)\nVotre Choix :")
		TypeML = input()
		if int(TypeML) == 1 or int(TypeML) == 2:
			print("Validate")
			VarCheck = True
		elif TypeML == "QUIT":
			exit()
		else:
			print("Erreur, tu n'a pas sélectionner 1 ou 2")
	return TypeML