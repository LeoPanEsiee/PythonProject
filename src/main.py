# filename 'main.py'

"""
    Authors : linda.luu@edu.esiee.fr, leo.pan@edu.esiee.fr
    Création de la carte et des histogrammes.
"""

# # # # # # # #
#   Imports   #
# # # # # # # #
import json
import dash
import pandas as pd
import plotly.express as px
import plotly.graph_objects
import plotly.validator_cache
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# # # # # # # # # # #
#   Partie Graphes  #
# # # # # # # # # # #

# Récupérer les données du csv
dataf = pd.read_csv(
    "datas/number_times_attacked.csv",
    delim_whitespace=True, header=13
)

# Liste des pays l'UE présent dans la BDD
col_options = [
    dict(label=x, value=x)
    for x in dataf['CountryCode'].unique()
]


# Création d'une instance de dash
app = dash.Dash(__name__)
app.title = "Endangered Rainbow"

#
# Histogramme 1
#


@app.callback(Output('graph1', 'figure'), [Input('CountryCode-dropdown', 'value')])
def chosen_country(country):
    """
    Return : la figure en fonction du pays choisi
    Args:
        country: Chaîne de caractères, pays dans l'UE.
        Obtenu à partir de la dropdown menu
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
def compare_countries():
    """
    Return : la Figure représentant un histogramme animé comparant les réponses des pays de l'UE.
    """
    fig = px.bar(
        dataf, x="answer", y="percentage",
        title="Animation des réponses de chaque pays",
        color="CountryCode",
        labels={
            'answer': 'Fréquence',
            'percentage': 'Pourcentage',
            'CountryCode': 'Pays'
        },
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


def compare_answers():
    """
    Return : la figure représentant les réponses des pays de l'UE regroupé par réponse.
    """
    fig = px.histogram(
        dataf, x="answer", y="percentage",
        title="Comparaison des réponses entre pays de l'UE",
        color='CountryCode',
        labels={
            'answer': 'Fréquence',
            'percentage': 'Percentage',
            'CountryCode': 'Pays'
        },
        height=600,
        width=1500,
        hover_name="CountryCode",
        barmode="group"
    )
    return fig


# # # # # # # # # # #
#    Partie Map     #
# # # # # # # # # # #

# Récupérer les données du geojson
europe_countries = json.load(open("datas/europe_countries.json", "r"))

# Création d'un id pour chaque pays du geojson
country_id_map = {}
i = 0
for feature in europe_countries['features']:
    feature['id'] = i
    country_id_map[feature['properties']['name']] = feature['id']
    i = i+1

# Récupérer les données du csv
df = pd.read_csv(
    "datas/attacked_because_lgbt.csv",
    delim_whitespace=True, header=13, encoding='latin1'
)

#Ne prendre que les réponses positives
df = df[df.answer == 'Yes']

# Retirer les pays du csv non trouvés dans les pays du geojson
for currentCountry in df['CountryCode'].unique():
    if currentCountry not in country_id_map.keys():
        df = df[df.CountryCode != currentCountry]

# Associer les pays du csv aux ids des pays du geojson
df['id'] = df['CountryCode'].apply(lambda x: country_id_map[x])

#
# Carte
#
def interactive_map():
    """
    Return : la figure représentant la carte des réponses positives à la question :
    "Votre dernière agression physique ou sexuelle
    est-elle due au fait vous étiez perçu comme LGBT ?
    (durant les 12 derniers moins)"
    """
    fig = px.choropleth_mapbox(
        df, locations='id', geojson=europe_countries, color='percentage',
        title="A été physiquement ou sexuellement attaqué ou menacé dans ces 12 dernières mois "
        "pour des raisons d'appartenance aux groupes LGBT",
        color_continuous_scale=px.colors.sequential.Blues,
        hover_name='CountryCode',
        hover_data={'percentage': True, 'id': False},
        labels={
            "percentage": "Pourcentage de oui"
        },
        mapbox_style="carto-positron",
        center={'lat': 56.7, 'lon': 10},
        zoom=2.8,
        opacity=0.7,
        height=800
    )
    fig.update_layout(
        margin={"l":10}
    )
    return fig


# # # # # # # # # # #
#    Partie App     #
# # # # # # # # # # #

# Création du HTML du dash
app.layout = html.Div(
    children=[
        html.H1(
            "Fréquence d'agression envers la communauté LGBTQ+ dans l'UE",
            style={
                'textAlign': 'center', 'color': 'black',
                'font-size': 23, 'font-family': 'Courier New'
            }
        ),
        dcc.Dropdown(
            id="chosen-graph-dropdown", value=1,
            options=[
                {'label': 'Carte de pourcentage de personnes agressés par pays', 'value': 1},
                {'label': 'Nombre d\'agressions', 'value': 2},
                {'label': 'Comparaison des réponses', 'value': 3}
            ],
            style={
                'textAlign': 'center', 'color': 'black',
                'font-size': 18, 'font-family': 'Courier New'
            }
        ),
        dcc.Dropdown(
            id="CountryCode-dropdown", value="France", options=col_options,
            style={
                'display': 'inline',
                'textAlign': 'center', 'color': 'black',
                'font-size': 18, 'font-family': 'Courier New'
            }
        ),

        dcc.Graph(id="graph1", figure={}),
        dcc.Graph(id="graph2", figure=compare_countries()),
        dcc.Graph(id="graph3", figure=compare_answers()),
        dcc.Graph(id="graph4", figure=interactive_map()),
    ]
)

# # # # # # # # # # # #
#  CSS Supplémentaire #
# # # # # # # # # # # #

@app.callback(
    [
        Output('CountryCode-dropdown', 'style'),
        Output('graph1', 'style'),
        Output('graph2', 'style'),
        Output('graph3', 'style'),
        Output('graph4', 'style')
    ],
    [Input('chosen-graph-dropdown', 'value')]
)
def dropdown_choice(value):
    """
    Gère la visibilité des graphes à afficher
    Return : les styles de chaque graphes
    Args:
        value : du choix sélectionné dans le dropdown menu
    """
    visible = {'display': 'inline-block', 'width': '100%'}
    halfscreen = {'display': 'inline-block', 'width': '50%'}
    hidden = {'display': 'none'}
    if value == 1:
        return hidden, hidden, hidden, hidden, visible
    if value == 2:
        return countrycode_dropdown_style(), halfscreen, halfscreen, hidden, hidden
    if value == 3:
        return hidden, hidden, hidden, visible, hidden
    return visible, halfscreen, halfscreen, hidden, hidden


def countrycode_dropdown_style():
    """
    Return : le style du countryCode dropdown
    """
    return {
        'textAlign': 'center', 'color': 'black',
        'margin-top': '10px',
        'width': '200px',
        'font-size': 18, 'font-family': 'Courier New'
    }


# Lancer l'application
app.run_server(debug=False, port="8888")
