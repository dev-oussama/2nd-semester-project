# declaration des modules necessaire
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress


# importation des donnes necaissanre
dataset=pd.read_csv ("project s2\data.csv",sep=";")

# verification des informations de la dataset
print (dataset.info())

# Pour les caractères quantitatifs

# 3. affichage des caracthere quantitatifs
def calcul (serie, nom):
    '''
    calcule des caracthere quantitatifs
    '''
    print("les statisitques  pour ",nom)
    print("Moyenne= ",serie.mean())
    print("Variance= ",serie.var())
    print("l'ecart-type= ",serie.std())
    print("le maximum= ",serie.max())
    print("le minimum= ",serie.min())
    print("les quantiles: ")
    print(serie.quantile([0.25,0.5,0.75]),"\n")

calcul(dataset['Charge_fixe'],"les charges fixes")
calcul(dataset['Charge_energie'],"la charge d'energies")
calcul(dataset['NB_personne'],'le nombre de personne')

# 4. affichage du calcule globale
print("calcule globale de charge fixe :",dataset['Charge_fixe'].describe())
print("\ncalcule globale de charge d'energie :",dataset['Charge_energie'].describe())
print("\ncalcule globale de nombre de personne :",dataset['NB_personne'].describe())


# 5.describtion de l'histogramme et la boite moustache pour chaque caractere
def affichage_graphique(serie, nom):
    '''
    cette fonction nous permet d'afficher les histogrammes 
    et les boites moustaches pour chaque caractere
    '''
    #histogramme
    plt.figure(figsize=(8, 5))
    plt.hist(serie ,bins = 25, color = 'skyblue',edgecolor = 'black')
    #plt.title('histogramme de ',nom) renvois un error donc:
    plt.title (str("histogramme de ")+str(nom))
    plt.xlabel(nom)
    plt.ylabel('frequence')
    plt.grid(True)
    plt.show()

    #boite a moustache (boxplot)
    plt.figure(figsize = (6,4))
    sns.boxplot(x=serie , color ='lightgreen')
    #plt.title("Boite a moustache de ", nom)
    plt.title(str ("Boite a moustache de ")+str(nom))
    plt.xlabel(nom)
    plt.grid(True)
    plt.show()

affichage_graphique(dataset['Charge_fixe'], "Charge fixe")
affichage_graphique(dataset['Charge_energie'],"Charge energie")
affichage_graphique(dataset ['NB_personne'], "Nombre de personnes")

# 6. affichage du graphique en violon
def affichage_violinplot (serie,nom):
    '''
    cette fonction nous permet de cree les graphiques en violon
    '''
    plt.figure(figsize = (6,4))
    sns.violinplot (x=serie , color = 'lightblue')
    plt.title(str("violon plot de ")+str(nom))
    plt.xlabel(nom)
    plt.grid(True)
    plt.show()

affichage_violinplot(dataset['Charge_fixe'], "Charge fixe")
affichage_violinplot(dataset['Charge_energie'], "Charge energie")
affichage_violinplot(dataset['NB_personne'], "Nombre de personnes")


# 7. histogramme et boite a moustache pour l'analyse globale
def affichage_global(serie, nom):
    '''
    cette fonction nous permet d'afficher l'hitogramme et 
    la boite a moustache pour l'analyse globale
    '''
    ### Histogramme
    plt.figure (figsize=(8,4))
    plt.hist(x=serie,bins= 25, color = "pink",edgecolor ="black")
    plt.title(str("histogramme globale ")+str(nom))
    plt.xlabel(nom)
    plt.ylabel("Frequence")
    plt.grid(True)
    plt.show()

    ### Boite a moustaches
    plt.figure (figsize= (6,3))
    sns.boxplot(x = serie , color = "red")
    plt.title(str("boite a moustache globale de ")+str(nom))
    plt.xlabel(nom)
    plt.grid(True)
    plt.show()

affichage_global(dataset['Charge_fixe'],"Charge fixe")
affichage_global(dataset['Charge_energie'],"Charge d'energie")
affichage_global(dataset['NB_personne'],"Nombre de personnes")

# Pour les caractères qualitatifs

# 8. tableau pour les effectifs et les frequences pour les caracteres qualitatifs
## creation des colognes du tableau
def tableau(serie):
    '''
    cette fonction nous permet de cree un tableau statistique pour
    les caracteres qualitatifs
    '''
    eff=serie.value_counts().sort_index() #effectif
    effcum= eff.cumsum()                  #effectif cumule 
    freq = eff/sum(eff)                   #frequence
    freqcum = freq.cumsum()               #frequence cumuler

    ### la representation de la dataframe
    df = pd.DataFrame({
        'effectif' :eff,
        'effectif cumuler' :effcum,
        'frequence' :freq,
        'frequence cumuler' :freqcum
    })
    return df

print ("le tableau consernant les voitures :\n",tableau (dataset["Voiture"]),"\n")
print ("le tableau consernant l'hebergement :\n", tableau(dataset["Type"]))

# Analyse statistique descriptives bivarié:
def graph (serie,nom):
    '''
    cette fonction nous permet d'afficher les diagramme en barres
    et les diagramme circulaire(pie) des caracthere qualitifs
    '''
    # comptage des modalites
    counts = serie.value_counts()
    labels = counts.index
    valeurs = counts.values

    colors = sns.color_palette('pastel', len (labels))  # couleurs personnalisees

    ## diagramme en barres 
    sns.barplot(x=labels,y=valeurs, palette= colors)
    plt.title ("Diagramme en barres de "+str(nom))
    plt.xlabel(nom)
    plt.ylabel("effectif")
    plt.grid(True,axis='y')
    plt.show()

    ## diagramme circulaire
    explode = [0.05,0.05] 
    plt.figure (figsize =(6,6))
    plt.pie(valeurs , 
            labels = labels , 
            autopct ='%1.1f%%', 
            startangle=90, 
            explode = explode, 
            colors = colors, 
            shadow= True)
    plt.title ('diagramme circulaire de '+ str(nom))
    plt.axis ('equal')
    plt.legend()
    plt.tight_layout()
    plt.show()

graph(dataset['Voiture'], "l'existance de voiture")
graph(dataset['Type'], "type d'hebergement")
plt.show()

# 10. creation graphique pour les nuages de points
plt.figure(figsize=(8,6))
plt.scatter(x=dataset['Charge_fixe']
            ,y=dataset['Charge_energie'],
            s=100, 
            alpha=0.5)
plt.title("Nuage de points : charge fixe vs charge energie")
plt.xlabel("Charge fixe")
plt.ylabel("Charge energie")
plt.grid(True)
plt.show()

# 11. calcule de covariance
covariance = dataset['Charge_energie'].cov(dataset['Charge_fixe'])
print("la valeur de covariance = ",covariance)

# 12. le coefficient de corrélation
correlation = dataset['Charge_fixe'].corr(dataset['Charge_energie'])
print("Coefficient de correlation :", correlation)

#13. Le coefficient de détermination
R_carre = correlation**2
print("Coefficient de determination :", R_carre)

# 14. les coefficients de la droite de regression
result = linregress(dataset['Charge_fixe'],dataset['Charge_energie'])
a = result.slope
b = result.intercept

print("coefficient a : ",a)
print("coefficient b : ",b)

#15. graph a nuage de point + la droite de regression 
plt.figure (figsize=(8,6))
sns.regplot(x='Charge_fixe', 
            y='Charge_energie', 
            data=dataset,
            scatter_kws={'color':'blue'}, 
            line_kws={'color':'red'})
plt.xlabel("Charge fixe")
plt.ylabel("charge energie")
plt.title ("graph a nuage accompagner de la droite de regression")
plt.grid(True)
plt.show

# 16. tableau de contingence
contingence = pd.crosstab(dataset['Type'],dataset['Voiture'])
print("Tableau de contingence :\n",contingence)

# 17. comparaison de deux caracteres
contingence.plot(kind="bar",figsize= (6,8))  
plt.title("Diagramme a bar Type vs Voiture")
plt.xlabel('type')
plt.ylabel('Voiture')
plt.legend(title='Voiture')
plt.grid(True)
plt.show()

# 18. diagramme circulaire cote a cote
fig, axes = plt.subplots(1, 2, figsize=(14,6))

dataset['Type'].value_counts().plot.pie(autopct='%1.1f%%', 
                                        ax=axes[0], 
                                        title="Repartition des Types", 
                                        colors=sns.color_palette('pastel'),
                                        startangle=90,
                                        shadow=True,
                                        explode= [0.1, 0.1]) 
dataset['Voiture'].value_counts().plot.pie(autopct='%1.1f%%', 
                                           ax=axes[1], 
                                           title="Repartition des Voitures", 
                                           colors=sns.color_palette('pastel'),
                                           startangle=90,
                                           shadow=True,
                                           explode = [0.1, 0.1])
plt.tight_layout()
plt.show()

# analyse conjointe des caracteres quantitatif

# 19.le tableau d’analyse descriptive détaillée de Charge_fixe en fonction des modalités de Type
description = dataset.groupby('Type')['Charge_fixe'].describe()
print(description)

# 20. histogramme de charge fixe pour chaque type
g = sns.FacetGrid(dataset, col='Type', height=5)
g.map(plt.hist, 'Charge_fixe', bins=20, color='skyblue', edgecolor='black')
plt.show()

# 21. comparaison graphique des médianes
# boxplot
sns.boxplot(x='Type', y='Charge_fixe', data=dataset, palette='pastel')
plt.title("Boxplot Charge_fixe par Type")
plt.grid(True)
plt.show()

#violinplot
sns.violinplot(x='Type', y='Charge_fixe', data=dataset, palette='muted')
plt.title("Violin plot Charge_fixe par Type")
plt.grid(True)
plt.show()