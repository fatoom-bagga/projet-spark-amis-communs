#  Mini Projet Spark - Amis communs

##  Objectif

Ce projet a pour but de découvrir les **amis communs entre deux utilisateurs** d'un réseau social représenté sous forme d’un graphe, en utilisant **Apache Spark** avec **PySpark**.

---

##  Données

Le fichier d'entrée est un fichier texte où chaque ligne représente un utilisateur et ses amis :

```
<user_id> <Nom> <friend_id1>,<friend_id2>,...
```



##  Étapes techniques

1. Charger les données avec PySpark
2. Générer les couples d’amis triés `(min, max)`
3. Grouper les paires et calculer les amis communs
4. Filtrer la paire spécifique `(1, 2)`
5. Afficher les amis communs

---

## ⚙️ Lancer le projet

### Prérequis

- Python 3
- PySpark
- Java installé
- Apache Spark installé et configuré

### Étapes :

```bash

# 1. Installer PySpark
pip install pyspark

# 2. Lancer le script
spark-submit common_friends.py
```

---

## Résultat attendu

```bash
1<Mohamed>2<Sidi>['Aicha']
```

Cela signifie que **Mohamed** (ID 1) et **Sidi** (ID 2) ont l’utilisateur **Aicha** en commun comme ami.

---

##Arborescence du projet

```
projet_spark/
├── common_friends.py    
├── friends_common.txt       
├── resultats_test.txt
└── README.md              
```

---

## 🧑‍💻 Auteurs

- Étudiant :Fatimetou Mohamed Abderrahmane Bagga
