# Tableau de Bord Thérapeutique 📊

## Description

Le **Tableau de Bord Thérapeutique** est une application interactive développée avec **Streamlit** pour visualiser et analyser les données relatives aux séances de thérapie. L'application permet aux utilisateurs de filtrer les données par thérapeute et type de thérapie, et fournit des visualisations claires et animées des coûts totaux, des durées moyennes et du nombre moyen de participants.

## Fonctionnalités ✨

- **Filtrage des Données** 🔍: Sélectionnez les thérapeutes et les types de thérapie pour personnaliser les visualisations.
- **Visualisations Animées** 📈: Graphiques interactifs pour analyser le coût total par type de thérapie et la durée des séances par thérapeute.
- **KPI Principaux** 📊: Affichage des coûts totaux, des durées moyennes et du nombre moyen de participants avec des animations.
- **Design Moderne** 🎨: Utilisation de CSS pour un design interactif et attrayant, avec des animations pour une meilleure expérience utilisateur.

## Prérequis 🛠️

- Python 3.7 ou supérieur
- Les bibliothèques Python suivantes :
  - `pandas`
  - `plotly`
  - `streamlit`
  - `openpyxl` (pour lire les fichiers Excel)

## Installation 🚀

1. **Clonez le dépôt** :
   ```bash
   git clone https://github.com/NicoNoti/visualisation-donnees-therapie.git
   cd visualisation-donnees-therapie

2. **Créez un environnement virtuel et activez-le** :
   ```bash
    python -m venv env
    source env/bin/activate  # Sur Windows utilisez `env\Scripts\activate`

3. **Installez les dépendances** :
   ```bash
    pip install pandas plotly streamlit openpyxl

## Utilisation 🚀

1. **Lancez l'application Streamlit** :
   ```bash
   streamlit run app.py

2. **Ouvrez votre navigateur et accédez à l'adresse fournie par Streamlit pour interagir avec l'application.** :


## Structure du Projet 📂

- app.py : 
    - Le fichier principal contenant le code de l'application Streamlit.
- DonnerEx.xlsx : 
    - Fichier Excel contenant les données de thérapie (doit être présent dans le répertoire du projet).  

## Remarques ⚠️

- Assurez-vous que le fichier Excel est bien formaté et que les noms des colonnes correspondent aux attentes de l'application.

- Les animations et le design interactif peuvent nécessiter une connexion internet pour charger les bibliothèques CSS externes.

## Contact 📬
Pour toute question ou information supplémentaire, veuillez contacter :

- **Nom** : RARIVOLALA Notiavaina Nicolas
- **GitHub** : [NicoNoti](https://github.com/NicoNoti)

**----**

- 📫 **Email** : nrarivolala@gmail.com
- 📘 **facebook** : [Notiavina Rarivo](https://www.facebook.com/profile.php?id=100008875758531)
- 📱 **WhatsApp** : [+261 33 71 244 38](https://wa.me/261337124438) 
- 📞 **Téléphone** : +261 34 93 071 39

## Licence 📜

- Ce projet est sous licence MIT.