# filename 'app.py'

"""
    Authors : linda.luu@edu.esiee.fr, leo.pan@edu.esiee.fr
    Création de l'histogramme.

"""

#
# Imports
#
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

#
# Data
#
dataf = pd.read_csv("Numbers.csv",
                    delim_whitespace=True, header=13)

# Options dispo : pays de l'UE présent dans la BDD
col_options = [dict(label=x, value=x)
               for x in dataf['CountryCode'].unique()]

# Création instance dash
app = dash.Dash(__name__)

#
# Front-end
#
app.layout = html.Div(children=[
    html.H1("Fréquence d'agression envers la communauté LGBTQ+ dans l'UE",
            style={'textAlign': 'center', 'color': '#1B1E2C', 'font-size': 23}),
    html.Button("1", id='button1',
                style={
                    'margin-left': 1250, 'margin-bottom': 15,
                    'padding': 8, 'color': "#ffffff",
                    'background-color': "#1B1E2C"}),
    html.Button("2", id='button2',
                style={'margin-bottom': 15,
                       'padding': 8, 'color': "#ffffff",
                       'background-color': "#1B1E2C"}),
    html.Button("3", id='button3',
                style={'margin-bottom': 15,
                       'padding': 8, 'color': "#ffffff",
                       'background-color': "#1B1E2C"}),
    dcc.Dropdown(id="CountryCode", value="France", options=col_options,
                 style={
                    'textAlign': 'center', 'color': '#1B1E2C',
                    'font-size': 16, 'width': 300}),
    dcc.Graph(id="graph", figure={}, style={'display': 'inline-block'}),
    dcc.Graph(id="graph2", figure={}, style={'display': 'inline-block'}),
    dcc.Graph(id="graph3", figure={}, style={'margin-left': 100}),
])

#
# Histogramme 1
#


@ app.callback(Output('graph', 'figure'),
               [Input('CountryCode', 'value')])
# La figure dépend de value, du pays choisi
def chose_country(country):
    """
    Retourne la figure en fonction du pays choisi.

    Args:
        country: Chaîne de caractères, pays dans l'UE. 
        Pays par défaut : France.
    """
    country = country if country else "France"
    # Sous ensemble du dataframe, sous ensemble en fonction des pays
    dataf_country = dataf.query("CountryCode == @country")
    # Création de l'histogramme
    fig = px.bar(dataf_country, x="answer", y="percentage",
                 title="Nombre d'agression qu'une personne LGBTQ+ a vécu ces 12 derniers mois",
                 color='answer',
                 labels={'answer': 'Fréquence', 'percentage': 'Pourcentage'},
                 color_discrete_sequence=[
                     "red", "orange", "yellow", "green", "blue", "purple", "brown"],
                 height=500,
                 width=700)
    fig.update_layout(
        modebar_color="#800080",
        bargap=0,
        font_size=10)
    return fig

#
# Histogramme 2
#


@ app.callback(Output('graph2', 'figure'),
               [Input('CountryCode', 'value')])
def compare_countries(country):
    """
    Permet de créer l'histogramme animé de comparaison entre pays de l'UE.
    Vue sur chaque pays de l'UE en quelques secondes.

    Args:
        country: Chaîne de caractères, pays dans l'UE. Pays par défaut : France.
    """
    fig = px.bar(dataf, x="answer", y="percentage",
                 title="Vue de chaque pays",
                 color="CountryCode",
                 labels={'answer': 'Fréquence', 'percentage': 'Pourcentage'},
                 height=500,
                 width=700,
                 animation_frame="CountryCode",
                 animation_group="answer",
                 range_x=[-1, 7],
                 range_y=[0, 50],
                 template="plotly_white",
                 color_discrete_sequence=px.colors.qualitative.Prism,
                 )
    fig.update_layout(
        modebar_color="#800080",
        font_size=10,
        bargap=0
    )
    return fig


#
# Histogramme 3
#

@ app.callback(Output('graph3', 'figure'),
               [Input('CountryCode', 'value')])
def compare_answers(country):
    """
    Permet de créer l'histogramme de comparaison des réponses entre pays de l'UE.
    Les réponses sont groupées entre elles.

    Args:
        country: Chaîne de caractères, pays dans l'UE. Pays par défaut : France.

    """
    fig = px.histogram(dataf, x="answer", y="percentage",
                       title="Comparaison des réponses entre pays de l'UE",
                       color='CountryCode',
                       labels={'answer': 'Fréquence',
                               'percentage': 'Pourcentage'},
                       height=600,
                       width=1200,
                       hover_name="CountryCode",
                       barmode="group")
    return fig


app.run_server(debug=True)
