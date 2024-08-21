import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit

# Emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Tableau de Bord Thérapeutique", page_icon=":bar_chart:", layout="wide")

# ---- LECTURE DE L'EXCEL ----
@st.cache_data
def get_data_from_excel():
    try:
        df = pd.read_excel(
            io="DonnerEx.xlsx",
            engine="openpyxl",
            sheet_name="DtBaseDate de la séance"
        )
    except Exception as e:
        st.error(f"Erreur lors de la lecture du fichier Excel: {e}")
        return pd.DataFrame()  # Retourner un DataFrame vide en cas d'erreur
    
    # Nettoyer les noms de colonnes
    df.columns = df.columns.str.replace(' ', '_').str.replace('[^A-Za-z0-9_]+', '', regex=True)
    
    return df

def validate_data(df):
    required_columns = ["Nom_du_thrapeute", "Type_de_thrapie", "Cot_total_de_la_sance", "Dure_de_la_sance", "Nombre_de_participants"]
    for column in required_columns:
        if column not in df.columns:
            st.error(f"La colonne {column} est manquante dans les données.")
            return False
    return True

df = get_data_from_excel()
if not validate_data(df):
    st.stop()

# ---- BARRE LATÉRALE ----
st.sidebar.header("Veuillez filtrer ici :")
st.sidebar.markdown("---")
st.sidebar.write("### Aperçu de l'animation")
st.sidebar.image("https://media.giphy.com/media/3ohhwm8EzYZC67Em5S/giphy.gif", use_column_width=True)

therapist = st.sidebar.multiselect(
    "Sélectionnez le thérapeute :",
    options=df["Nom_du_thrapeute"].unique(),
    default=df["Nom_du_thrapeute"].unique()
)

therapy_type = st.sidebar.multiselect(
    "Sélectionnez le type de thérapie :",
    options=df["Type_de_thrapie"].unique(),
    default=df["Type_de_thrapie"].unique()
)

# Appliquer les sélections pour filtrer le dataframe
filtered_df = df.query(
    "Nom_du_thrapeute in @therapist & Type_de_thrapie in @therapy_type"
)

# Vérifier si le dataframe est vide
if filtered_df.empty:
    st.warning("Aucune donnée disponible selon les paramètres de filtre actuels !")
    st.stop()

# ---- PAGE PRINCIPALE ----
st.markdown("""
    <div style='text-align: center; font-size: 48px; color: #0083B8; font-family: Arial, sans-serif;'>
    Tableau de Bord Thérapeutique
    </div>
    <div style='text-align: center; font-size: 20px; color: #555555;'>
    Visualisez les données thérapeutiques avec style et clarté
    </div>
    <hr style='border: 1px solid #0083B8;'/>
    """, unsafe_allow_html=True)

# KPI PRINCIPAUX avec animations
total_cost = int(filtered_df["Cot_total_de_la_sance"].sum())
average_duration = round(filtered_df["Dure_de_la_sance"].mean(), 1)
average_participants = round(filtered_df["Nombre_de_participants"].mean(), 2)

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.markdown(f"""
        <div class='animate__animated animate__fadeInLeft' style='font-size: 24px; color: #28a745;'>
        <i class="fas fa-dollar-sign"></i> Coût Total : Ar {total_cost:,}
        </div>
        """, unsafe_allow_html=True)
with middle_column:
    st.markdown(f"""
        <div class='animate__animated animate__fadeInUp' style='font-size: 24px; color: #007bff;'>
        <i class="fas fa-hourglass-half"></i> Durée Moyenne : {average_duration} heures
        </div>
        """, unsafe_allow_html=True)
with right_column:
    st.markdown(f"""
        <div class='animate__animated animate__fadeInRight' style='font-size: 24px; color: #ffc107;'>
        <i class="fas fa-users"></i> Participants Moyens : {average_participants} participants
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr style='border: 1px solid #0083B8;'/>", unsafe_allow_html=True)

# COÛT PAR TYPE DE THÉRAPIE [GRAPHIQUE EN BARRE] avec animation
cost_by_therapy_type = filtered_df.groupby(by=["Type_de_thrapie"])[["Cot_total_de_la_sance"]].sum().sort_values(by="Cot_total_de_la_sance")
fig_therapy_cost = px.bar(
    cost_by_therapy_type,
    x="Cot_total_de_la_sance",
    y=cost_by_therapy_type.index,
    orientation="h",
    title="<b>Coût par Type de Thérapie</b>",
    color_discrete_sequence=["#0083B8"] * len(cost_by_therapy_type),
    template="plotly_dark",
)
fig_therapy_cost.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=dict(showgrid=False),
    yaxis_title=None,
    xaxis_title=None,
    title_x=0.5,
    title_font=dict(size=24, color='#0083B8', family="Arial, sans-serif"),
    font=dict(color="#ffffff"),
)

# DURÉE PAR THÉRAPEUTE [GRAPHIQUE EN BARRE] avec animation
duration_by_therapist = filtered_df.groupby(by=["Nom_du_thrapeute"])[["Dure_de_la_sance"]].sum()
fig_duration_therapist = px.bar(
    duration_by_therapist,
    x=duration_by_therapist.index,
    y="Dure_de_la_sance",
    title="<b>Durée par Thérapeute</b>",
    color_discrete_sequence=["#FF5733"] * len(duration_by_therapist),
    template="plotly_dark",
)
fig_duration_therapist.update_layout(
    xaxis=dict(tickmode="linear"),
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=dict(showgrid=False),
    yaxis_title=None,
    xaxis_title=None,
    title_x=0.5,
    title_font=dict(size=24, color='#FF5733', family="Arial, sans-serif"),
    font=dict(color="#ffffff"),
)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_duration_therapist, use_container_width=True)
right_column.plotly_chart(fig_therapy_cost, use_container_width=True)

# ---- AJOUT D'EFFETS ANIMÉS AVANCÉS ET CSS INTERACTIF ----
st.markdown("""
<style>
@import url('https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css');
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css');
body {
    background-image: linear-gradient(to right, #f7f7f7, #e3e3e3);
    font-family: 'Arial', sans-serif;
}
div[data-testid="stSidebar"] {
    background-color: #2c3e50;
    color: white;
    border-right: 1px solid #34495e;
}
</style>
""", unsafe_allow_html=True)

# ---- CACHER LE STYLE DE STREAMLIT ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
