import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Titre de l'application
st.title("TP sur la base de donnée IRIS !")

st.subheader(":blue[Créer par Abdoul Rachid BISSARE, 01 63 61 49 80]")

# Charger les données
st.header("1. Charger la base de données")
uploaded_file = st.file_uploader("Téléversez le fichier iris.csv", type=["csv"])

if uploaded_file is not None:
    # Charger la base de données
    data = pd.read_csv(uploaded_file)
    st.success("Fichier chargé avec succès !")

    # Afficher un aperçu des données
    st.subheader("Aperçu des données")
    st.dataframe(data.head())

    # Statistiques descriptives
    st.subheader("Statistiques descriptives")
    st.write(data.describe())

    # Sélectionner des colonnes pour la manipulation
    st.subheader("2. Manipulez les données")
    selected_columns = st.multiselect(
        "Sélectionnez les colonnes à afficher",
        data.columns.tolist(),
        default=data.columns.tolist()
    )
    st.write("Données sélectionnées :")
    st.dataframe(data[selected_columns])

    # Graphiques interactifs
    st.subheader("3. Visualisez les données avec des graphes")
    graph_type = st.radio("Choisissez un type de graphique", ["Histogramme", "Nuage de points", "Pairplot"])
    
    if graph_type == "Histogramme":
        column = st.selectbox("Sélectionnez une colonne pour l'histogramme", data.columns[:-1])
        plt.figure(figsize=(8, 4))
        sns.histplot(data[column], kde=True, bins=20, color="blue")
        st.pyplot(plt)

    elif graph_type == "Nuage de points":
        x_axis = st.selectbox("Axe X", data.columns[:-1])
        y_axis = st.selectbox("Axe Y", data.columns[:-1])
        species = st.selectbox("Coloration par espèce", data.columns[-1])
        plt.figure(figsize=(8, 4))
        sns.scatterplot(data=data, x=x_axis, y=y_axis, hue=species, palette="viridis")
        st.pyplot(plt)

    elif graph_type == "Pairplot":
        plt.figure(figsize=(8, 6))
        sns.pairplot(data, hue=data.columns[-1], palette="husl")
        st.pyplot(plt)
else:
    st.warning("Veuillez téléverser un fichier CSV pour continuer.")

# Titre de l'application
st.header("Copyright 2024")
