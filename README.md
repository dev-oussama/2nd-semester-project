# 2nd-semester-project
Compte rendue 

1. Introduction 
L'objectif de ce travail pratique est d'analyser les charges fixes quotidiennes de 242 ménages d'une cité, en considérant leur type de logement (appartement ou villa), leur consommation énergétique et le nombre de personnes par foyer. Ce TP vise à mettre en pratique les concepts de statistiques descriptives univariées et bivariées vus en cours, en utilisant Python comme outil principal d'analyse.

À travers cette étude, nous allons :
1. Examiner les caractéristiques des différentes variables (quantitatives et qualitatives)
2. Réaliser des analyses descriptives complètes (moyennes, médianes, écarts-types)
3. Construire des représentations graphiques appropriées (histogrammes, boîtes à moustaches, diagrammes circulaires)
4. Explorer les relations entre les variables
5. Interpréter les résultats obtenus

Ce travail nous permettra de mieux comprendre la répartition des charges ménagères dans cette population et d'identifier d'éventuels liens entre les différents facteurs étudiés. L'utilisation de Python offre l'avantage d'automatiser les analyses et de produire des visualisations claires et personnalisables.
Outils utilisés:  
- IDO Visual Studio Code
- Python avec les librairies :  
 - pandas : pour structure de données et feuilles de calcul
 - mathplotlib : pour les graphs
 - seaborn : pour la visualisation des donnes
 - scipy : pour integrer les principaux algorithme numerique



2. PartieTheorique
Variables etudiees :
1.	Charge_fixe : Quantitative continue (depense quotidiennes )
2.	Charge_energie : Quantitative continue (consommation energetique)
3.	Type : Quantitative nominale (Appartement/Villa)
4.	Voiture : Quantitative binaire( Oui/Non)
5.	NB_personne : Quantitative discrete (nombre d’habitants)
3. Partie Pratique
A. Collecte des Donnes 
 
Dans cette partie j’ai oublier la de mentionner la séparation mais comme même j’ai réussi a résoudre le problème en ajoutant dataset.info() :
 
Donc j’ai pu identifier l’erreur et le modifier :
 

B. Analyse statistique des résultats
  
1. Nombre de Personnes par Ménage 
L'étude démontre que :
- La taille médiane des ménages est de 2 personnes
- 50% des foyers comptent entre 2 et 3 personnes (Q1-Q3)
- La distribution présente une légère asymétrie droite (moyenne = 2.57 > médiane), due à quelques familles nombreuses (jusqu'à 6 personnes)
- La faible variance (0.91) indique que la plupart des ménages sont de taille similaire

2. Charges Fixes 
L'analyse révèle que :
- 50% des ménages dépensent moins de 17.82 unités quotidiennement (médiane)
- 75% des foyers ont des charges inférieures à 24.22 unités (Q3)
- La distribution présente une forte asymétrie positive (moyenne = 19.84 > médiane), indiquant la présence de quelques ménages avec des charges exceptionnellement élevées (jusqu'à 58.81 unités)
- L'écart-type important (8.92) confirme une grande variabilité entre les ménages






3. Charges Énergétiques Quotidiennes 
- La consommation médiane s'établit à 2.90 unités quotidiennes
- 50% des ménages se situent dans une fourchette relativement restreinte (2.00 à 3.54 unités, Q1-Q3)
- La distribution est quasiment  symétrique (moyenne = 3.00 ≈ médiane)
- Quelques cas extrêmes sont observés (min = 1.0, max = 10.0), mais l'écart-type modéré (1.38) suggère une certaine homogénéité des comportements énergétiques
 



4. Tableau Comparative 
Variable	Moyenne	Médiane	Écart-type	Plage
Nombre de personnes   	2.57        	2.0         	0.95           	[1, 6]          
Charges fixes         	19.84       	17.82       	8.92           	[3.07, 58.81]   
Charges énergétiques  	3.00        	2.90        	1.38           	[1.0, 10.0]     



Interprétation globale :
1. Les charges fixes montrent les plus grandes disparités, avec des écarts importants entre ménages 
2. La consommation énergétique est plus stable, avec des comportements similaires pour la majorité des foyers 

3. La taille des ménages est relativement uniforme, expliquant partiellement les variations observées dans les charges
 

Analyse des Histogrammes
Avant de commencer l’analyse je veut mentionner que lors du coding j’ai galérer a écrire les titres des histogrammes puisque je me suis adapter a la méthode des fonctions et la fonction plt.title() ne prend qu’une celle paramètre donc la solution c’est utiliser «str ()»
Rq : la meme solutions avec les autres graphes
 

1. Histogramme de la Charge Fixe

Caractéristiques principales :
- Distribution: Asymétrie marquée vers la droite
- Pic principal: Entre 10 et 20 unités
- Queue de distribution: S'étend jusqu'à 50 unités
- Classes remarquables:
  - 10-15 unités : Fréquence la plus élevée
  - >30 unités : Fréquences très faibles

Interprétation :
- La majorité des ménages (environ 65%) ont des charges fixes comprises entre 10 et 20 unités
- Quelques ménages (moins de 5%) présentent des charges exceptionnellement élevées (>40 unités)
- La distribution confirme l'asymétrie positive observée dans les statistiques descriptives
2. Histogramme du Nombre de Personnes

Caractéristiques principales:
- Distribution unimodale: Pic à 2 personnes
- Fréquences :
  - 2 personnes : envirant 160 ménages (valeur maximale)
  - 1 personne :  envirant 40 ménages
  - 6 personnes : <20 ménages
- Décroissance rapide au-delà de 3 personnes

Interprétation:
- La distribution confirme la prédominance des petits ménages
- 2 personnes représente le mode (valeur la plus fréquente)
- Les ménages de plus de 4 personnes sont rares (<15% du total)
- Cohérent avec la médiane à 2 personnes
3. Histogramme de la Charge Énergétique
Caractéristiques principales :
- Distribution quasi-normale : Forme en cloche
- Centre de distribution : Autour de 3 unités
- Étendue : De 1 à 10 unités
- Classes remarquables:
  - 2-4 unités : Représente ~70% des ménages
  - <2 ou >6 unités : Fréquences marginales
Interprétation :
- Confirmation de la symétrie observée dans les statistiques (moyenne ≈ médiane)
- La plupart des consommations (90%) se situent entre 1.5 et 5 unités
- Quelques valeurs extrêmes (>8 unités) mais très peu fréquentes

Conclusions:
1. Les charges fixes présentent la plus grande variabilité
2. Le nombre de personnes montre une concentration marquée autour de 2
3. La consommation énergétique est la plus régulière et prévisible

Analyse des Boîtes à Moustaches

1. Boîte à Moustaches de la Charge Fixe

Structure de la boîte :
- Médiane : Environ 18 unités (ligne centrale)
- Boîte (Q1-Q3 : De ~13 à ~24 unités (contient 50% des données)
- Moustaches : S'étendent jusqu'à ~10 (min) et ~35 unités
- Points isolés: Plusieurs valeurs au-delà de 40 unités 

Interprétation:
- 50% des ménages ont des charges entre 13 et 24 unités
- Asymétrie marquée vers les hautes valeurs
- Présence de plusieurs ménages avec charges exceptionnelles (>40 unités)
- Confirme l'histogramme : dispersion importante vers les valeurs hautes


2. Boîte à Moustaches de la Charge Énergétique

Structure de la boîte :
- Médiane: Environ 3 unités
- Boîte (Q1-Q3 : De ~2 à ~3.5 unités
- Moustaches : De ~1 à ~6 unités
- Points isolés : Quelques valeurs >6 unités

Interprétation :
- Distribution plus concentrée que la charge fixe
- Symétrie relative autour de la médiane
- Quelques consommateurs énergétiques extrêmes (>6 unités)
- Cohérent avec l'histogramme : distribution en cloche

3. Boîte à Moustaches du Nombre de Personnes


Structure de la boîte:
- Médiane : À 2 personnes
- Boîte (Q1-Q3 : De 2 à 3 personnes
- Moustaches: De 1 à 4 personnes
- Points isolés : Valeurs à 5 et 6 personnes
Interprétation :
- Concentration très forte autour de 2-3 personnes
- Quelques familles nombreuses (5-6 personnes) considérées comme outliers
- Distribution globalement symétrique mais avec queue droite
- Corrobore l'histogramme : pic à 2 personnes
Conclusions:
1. La charge fixe montre la plus grande variabilité avec de nombreux cas extrêmes
2. La consommation énergétique présente une distribution plus régulière
3. Le nombre de personnes est très concentré, avec peu de variations

Analyse des Graphiques en Violon

1. Graphique en Violon de la Charge Fixe

Caractéristiques principales:
- Forme : Large à la base (10-20 unités) et s'amincissant progressivement
- Densité :
  - Pic de densité autour de 15 unités
  - Queue fine jusqu'à 50 unités
- Médiane : Positionnée vers 18 unités (ligne centrale)

Interprétation:
- Confirmation de la concentration des données entre 10-25 unités
- La forme étirée vers la droite indique des valeurs extrêmes peu fréquentes
- La largeur à différents niveaux illustre la densité variable des observations

2. Graphique en Violon de la Charge Énergétique
Caractéristiques principales:
- Forme symétrique : Distribution en cloche presque parfaite
- Densité maximale : Autour de 3 unités
- Étendue : De 1 à 10 unités avec quelques valeurs extrêmes
- Épaisseur: Uniforme dans la partie centrale (2-4 unités)

Interprétation :
- Distribution quasi-normale confirmée
- Pic de densité très marqué autour de la médiane
- Quelques ménages avec consommations extrêmes (>8 unités) visibles par les extensions fines
- Cohérent avec les résultats précédents mais avec une meilleure visualisation de la densité

3. Graphique en Violon du Nombre de Personnes

Caractéristiques principales :
- Forme particulière : Multi-modale avec pics à 1, 2 et 3 personnes
- Densité :
  - Maximale à 2 personnes
  - Secondaire à 1 et 3 personnes
- Valeurs extrêmes: Quelques points isolés à 5-6 personnes

Interprétation :
- Répartition non uniforme avec préférence marquée pour 2 personnes
- Structure complexe révélant des sous-populations :
  - Célibataires (1)
  - Couples (2)
  - Petites familles (3)
- Les ménages >4 personnes sont rares et forment des "queues" fines




Apports spécifiques des violons :
1. Meilleure visualisation des densités que les boîtes à moustaches
2. Révélation de multi-modalités (surtout pour le nombre de personnes)
3. Représentation plus précise de la répartition des valeurs
4. Combinaison idéale des informations d'histogramme et de boîte à moustaches

Suggestions d'exploitation:
- Pour la charge fixe : Analyser séparément les deux modes (10-15 et 20-25)
- Pour l'énergie : Vérifier l'adéquation à une loi normale
- Pour la taille des ménages : Segmenter l'analyse par type de logement

Pour les caractères qualitatifs


Analyse des Variables Qualitatives

1. Possession d'une Voiture
 

Interprétation:
- Majorité sans voiture: 62.4% des ménages ne possèdent pas de véhicule
- Répartition : Près de 2/3 contre 1/3
- Cumul : La fréquence cumulée atteint 100% pour "Oui", vérifiant l'exhaustivité des données

2. Type d'Hébergement
 

Interprétation:
- Prédominance des appartements : 64.5% des logements
- Équilibre géographique : 1/3 des ménages en villas
- Vérification : Total cumulé cohérent avec l'effectif total (242)

Synthèse Comparative

Variable        	Modalité Majoritaire	Poids (%)	Modalité Minoritaire	Poids (%)	Écart
Voiture	Non                  	62.4%     	Oui   	37.6%     	24.8%
Type Logement	Appartement	64.5%     	Villa  	35.5%     	29.0%


Conclusions :
1. Les appartements sont significativement plus nombreux que les villas
2. La non-possession de voiture est majoritaire dans cette population







Analyse statistique descriptives bivarie :
Analyse des Diagrammes en Barres 

1. Possession d'une Voiture

Lecture du graphique :
- Axe vertical : Effectif des ménages (0-140)
- Axe horizontal: Modalités (Non/Oui)
- Hauteur des barres :
  - "Non" : ~130 ménages
  - "Oui" : ~90 ménages


Interprétation :
- Écart important : 1.4 fois plus de ménages sans voiture
- Visualisation claire de la dominance de la non-possession (62.4% vs 37.6%)
- La différence de hauteur est immédiatement perceptible

2. Type d'Hébergement

Lecture du graphique:
- Axe vertical : Effectif (0-160)
- Axe horizontal : Type (Appartement/Villa)
- Hauteur des barres :
  - Appartement : ~155 ménages
  - Villa : ~85 ménages
Analyse des Diagrammes Circulaires pour les Variables Qualitatives

1. Possession d'une Voiture
 
Lecture du graphique:
- Secteurs:
  - "Non" : 62.4% (bleu)
  - "Oui" : 37.6% (orange)
- Angles :
  - "Non" : ~225°
  - "Oui" : ~135°

Interprétation :
- Proportions immédiatement visibles: La dominance du "Non" est flagrante
- Avantage : Permet de saisir instantanément les proportions relatives
Limite : Difficulté à comparer précisément deux diagrammes circulaires entre eux

2. Type d'Hébergement

Lecture du graphique:
- Secteurs :
  - "Appartement" : 64.5% (bleu)
  - "Villa" : 35.5% (orange)
- Angles :
  - "Appartement" : ~232°
  - "Villa" : ~128
Analyse du Nuage de Points









1. Structure Globale du Graphique
- Axe X (Charge fixe) : 0-60 unités 
- Axe Y (Charge énergie): 0-12 unités
- Densité des points: Concentration entre 10-30 (X) et 2-6 (Y)

2. Interprétation des Tendances
1. Corrélation Positive:
   - Nuage orienté vers le haut à droite
   - Confirme le coefficient de corrélation de 0.75 calculé précédemment
   - Relation quasi-linéaire pour la majorité des points
2. Clusters Naturels:
   - Zone Principale (80% des points) :
     - Charge fixe : 10-25 unités
     - Énergie : 2-5 unités
   - Sous-groupe Énergivore (5%) :
     - Charge fixe > 30 avec énergie > 6 unités

3. Points Aberrants :
   - Haut-Droite : (50,10) - Ménage à très haute consommation
   - Bas-Droite : (40,2) - Charges fixes élevées mais consommation énergétique basse
Analyse des Mesures de Liaison Statistique
 
1. Covariance (8.34)
Interprétation :
- Valeur positive : Relation croissante entre charges fixes et énergétiques
- Amplitude modérée : Indique une covariation sensible mais non extrême
- Limite : Sensible aux unités de mesure (difficile à interpréter seul)
Conclusion : 
Liaison modérément forte (0.68) confirmant la tendance linéaire positive observée dans le nuage de points.

2. Coefficient de Détermination (0.46)
Signification :
- 45.8% de la variation de la charge énergétique s'explique par la charge fixe
- 54.2% dépend d'autres facteurs (surface, isolation, etc.)

Implications :
- Modèle utile mais nécessite l'ajout de variables explicatives
- Puissance prédictive moyenne en l'état actuel

3. Droite de Régression (y = 0.105x + 0.918)
Relation positive : Plus les charges fixes augmentent, plus la consommation d'énergie augmente

Analyse du Nuage de Points avec Droite de Régression

1. Description Visuelle du Graphique
- Nuage de points : Répartition des données brutes entre :
  - Charge fixe (X) : 0 à 50 unités
  - Charge énergie (Y) : 0 à 10 unités
- Droite de régression : Tracée en rouge avec équation y = 0.105x + 0.918

2. Interprétation Clé
1. Tendance Générale :
   - La droite monte légèrement entre charges fixes et énergie.
   - Exemple :  
     - À **20 unités** de charge fixe → ~3 unités d'énergie  
     - À **40 unités** → ~5.1 unités (+2.1 unités seulement).

3. Zones Remarquables
Zone	Charge Fixe	Énergie	Observation
A	10-20	2-4	Comportement moyen (proche de la droite)
B	30-50	6-10	Ménages énergivores (au-dessus de la droite)
C	30-50	1-3	Ménages économes (sous la droite)

Analyse Combinée : Tableau de Contingence et Statistiques Descriptives
  
1. Tableau de Contingence Voiture/Type de Logement
	Non Voiture	Avec Voiture	Total
Appartement	97	59	156
Villa	54	32	86
Total	151	91	242

Interprétation :
- Aucune différence significative dans la possession de voiture entre appartements (37.8%) et villas (37.2%)
- Écart négligeable (0.6%) confirmé par un test du Chi² non significatif (p > 0.05)

2. Statistiques Descriptives des Charges Fixes par Type de Logement

Appartements (n=156)
Métrique	Valeur (unités)	Interprétation
Moyenne	20.81	Charges plus élevées que les villas
Ecart-type	9.24	Grande variabilité
Médiane	18.39	50% des appartements ≤ 18.39 unités
Max	50.81	Valeur extrême 

 


Villas (n=86)
Métrique	Valeur (unités)	Interprétation
Moyenne 	18.08	Charge plus basses 
Ecart-type	8.05	Variabilité légèrement moindre
Médiane	16.42	50% des villas ≤ 16.42 unités
Min 	3.07	Cas très économique

3. Comparaison Appartements/Villas
- Écart moyen : +2.73 unités pour les appartements
- Distribution :
  - Q1 (25%) : Appartements (+1.31 unités)
  - Q3 (75%) : Appartements (+3.02 unités)

Tableau Synthèse
Variable	Appartement	Villa 	Difference
% avec voiture	37.8%	37.2%	+0.6%
Charge fixe moyenne	20.81	18.08	+2.73
Dispersons	9.24	8.05	+1.19











Analyse des Diagrammes Circulaires Côte à Côte
 
1. Répartition des Types de Logement (Graphique de gauche)
- Appartements : 64.5%  
- Villas : 35.5%  
  Écart : 1.8x plus d'appartements que de villas  

Interprétation :  
- Prédominance nette des appartements  
2. Répartition de la Possession de Voiture (Graphique de droite)
- Sans voiture: 62.4%  
- Avec voiture : 37.6%  
Interprétation :  
  - Bon réseau de transports en commun  
3. Comparaison Visuelle
Critère	Type Logement	Possession Voiture	Similarité
Proportion majoritaire	64.5%	| 62.4%	≈60/40     
Écart	29 points     	24.8 points        	Comparable

Analyse Comparative des Charges Fixes par Type de Logement
 
1.	Statistiques Clés
Metrique	Appartement(n=156)	Villa (n=86)	Ecart
Moyenne (mean)	20.82 	18.08 	+2.73
Ecart-type	9.24	8.05	+1.19
Mediane	18.39	16.42	+1.97
Minimum	7.25	3.07	+4.18
Maximum	50.81	44.30	+6.51

2. Interprétation des Résultats
a. Différence de Niveau 
- Les appartements ont des charges fixes systématiquement plus élevées :
  - +15% en moyenne (20.81 vs 18.08)
  - +12% au niveau médian (18.39 vs 16.42)

b. Variabilité 
- Plus grande dispersion dans les appartements (écart-type de 9.24 vs 8.05) :
  - S'explique par la présence de :
    - Appartements haut de gamme (jusqu'à 50.81 unités)
    - Studios économiques (à partir de 7.25 unités)
c. Distribution 
- Quartiles supérieurs (75%) :
  - Appartements : 24.84
  - Villas : 21.82  
  → Écart qui s'accentue pour les logements haut de gamme
Analyse du Diagramme à Barres : Charges Fixes (Appartements vs Villas)
 
1. Description du Graphique
- Type de visualisation : Barres groupées comparant les charges fixes moyennes
- Axe X : 
- Sous-catégories : Fourchettes de charges fixes (10-20, 20-30, etc.)
- Axe Y : Fréquence (nombre de ménages)
Fourchette de Charges	Appartements	Villas	Écart
10-20 	~17.5       	~15.0  	+2.5  
20-30 	~12.5       	~7.5   	+5.0  
30-40	~5.0        	~2.5   	+2.5  
40-50	~2.5        	0.0	+2.5


Tendances :
1. Écart croissant avec le niveau de charges :
   - +16% pour 10-20 unités  
   - +67% pour 20-30 unités  


2. Interprétation
- Segment bas/moyen (10-30 unités) :
  - Différence modérée mais systématique en faveur des appartements
  - Possible explication : Charges communes (ascenseurs, hall...) dans les immeubles

- Segment haut (>30 unités) :
  - Dominance écrasante des appartements
  - Correspond probablement à :
    - Résidences services (gestion intensive)
    - Appartements de luxe avec équipements premium


3. Implications
- Gestion immobilière :
  - Prévoir +15-20% de charges pour les appartements vs villas
  - Seuil critique : 30 unités (où l'écart s'accentue)

- Politique énergétique:
  - Cibler les appartements >30 unités pour des audits
  - Étudier les bonnes pratiques des villas économes






Analyse Comparée des Distributions de Charges Fixes : Violon vs Boîte à Moustaches

1. Graphique en Violon
 
Caractéristiques :
- Forme : 
  - Appartements : Distribution bimodale (pics à ~15 et ~25 unités)
  - Villas : Distribution uni modale (pic à ~15 unités)
- Densité :
  - Zone la plus dense pour les appartements : 12-28 unités
  - Zone la plus dense pour les villas : 10-22 unités
- Extrémités :
  - Appartements : Queue étirée jusqu'à 50+ unités
  - Villas : Maximum autour de 40 unités



Interprétation :
- Double population dans les appartements :
  - Groupe économique (~15 unités)
  - Groupe premium (~25 unités)
- Homogénéité relative des villas





















2. Boîte à Moustaches
 
Statistiques Visuelles :
Metrique	Appartement 	Villa
Mediane	18 unités  	16 unités
Q1-Q3	14-25 unités	13-22 unités
Whiskers	7-50 unités	3-40 unités
Outliers	Plusieurs   	Quelques-uns

Points Clés :
- Écart interquartile plus large pour les appartements (11 vs 9 unités)
- Asymétrie marquée vers le haut dans les deux cas
4. Synthèse des Résultats
1. Appartements :
   - Deux marchés distincts : économique et premium
   - Plus grande variabilité : certains très économes (<10 unités), d'autres très coûteux (>40 unités)

2. Villas :
   - Distribution plus homogène autour de 15-20 unités
   - Absence de surcoût extrême : maximum 40 unités vs 50+ pour les appartements
Analyse du Diagramme en Barres : Répartition Voiture/Type de Logement

1. Description du Graphique
 
- Axe X : Type de logement (Appartement/Villa)
- Axe Y : Nombre de ménages
- Couleurs :
  - Bleu : Sans voiture
  - Orange : Avec voiture
- Hauteur des barres : Effectifs bruts


2. Données Clés
Type	Sans Voiture	Avec Voiture	Total
Appartement	97		59           	156   
Villa       	54           	32	86    

Pourcentages par type :
- Appartements : 62.2% sans voiture vs 37.8% avec
- Villas : 62.8% sans voiture vs 37.2% avec

3. Observations Majeures
1. Proportions quasi identiques :
   - Écart <1% entre appartements et villas
   - Confirme l'absence de lien statistique (test du Chi² non significatif)

2. Dominance des appartements :
   - Représentent 64.5% du total (156/242)
   - Même proportion de motorisation que les villas

3. Structure globale :
   - 62.4% des ménages sans voiture (151/242)
   - 37.6% avec voiture (91/242)

4.Conclusion:
Le projet pratique a été un excellent moyen d’appliquer les concepts de statistiques descriptives à un dataset relatif aux charges énergétiques de 242 foyers. Avec l'aide de Python et de ses bibliothèques (pandas, matplotlib, seaborn), j'ai pu:

1. Analyser les distributions des charges fixes et des coûts énergétiques
2. Visualiser les relations entre les différentes variables
3. Interpréter les comportements en matière de consommation

Principaux enseignements :

- Mise en oeuvre du principe DRY (Don't Repeat Yourself) par la création de fonctions pour les graphiques et les calculs
- Utilisation avancée de Python dans le cadre d’analyses de données.
- Apprendre GitHub dans le cadre de versioning et de partage de code (premier projet
publié !).

Ressources utilisées :

- Cours universitaires de statistique
- Cours W3Schools ainsi que freeCodeCamp
- Documentation de pandas et seaborn
