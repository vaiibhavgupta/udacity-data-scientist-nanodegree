import os
import pickle
import base64

import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

from models.train_classifier import tokenize


class GetGlobalVariables:

    models_folder = os.getcwd()+'/models'
    data_viz_folder = os.getcwd()+'/plots'
    model_name_list = ['RFC_direct_report', 'RFC_clothing', 'RFC_water', 'RFC_weather_related', 'RFC_fire', 'RFC_earthquake', 'RFC_transport', 
    'RFC_other_infrastructure', 'RFC_aid_centers', 'RFC_money', 'RFC_death', 'RFC_electricity', 'RFC_military', 'RFC_floods', 'RFC_cold', 
    'RFC_missing_people', 'RFC_search_and_rescue', 'RFC_other_weather', 'RFC_shops', 'RFC_tools', 'RFC_refugees', 'RFC_aid_related', 'RFC_shelter', 
    'RFC_other_aid', 'RFC_security', 'RFC_related', 'RFC_buildings', 'RFC_request', 'RFC_offer', 'RFC_infrastructure_related', 'RFC_food', 
    'RFC_hospitals', 'RFC_medical_help', 'RFC_storm', 'RFC_medical_products']

    RFC_direct_report = pickle.load(open(f'{models_folder}/RFC_direct_report.pickle', 'rb'))
    RFC_clothing = pickle.load(open(f'{models_folder}/RFC_clothing.pickle', 'rb'))
    RFC_water = pickle.load(open(f'{models_folder}/RFC_water.pickle', 'rb'))
    RFC_weather_related = pickle.load(open(f'{models_folder}/RFC_weather_related.pickle', 'rb'))
    RFC_fire = pickle.load(open(f'{models_folder}/RFC_fire.pickle', 'rb'))
    RFC_earthquake = pickle.load(open(f'{models_folder}/RFC_earthquake.pickle', 'rb'))
    RFC_transport = pickle.load(open(f'{models_folder}/RFC_transport.pickle', 'rb'))
    RFC_other_infrastructure = pickle.load(open(f'{models_folder}/RFC_other_infrastructure.pickle', 'rb'))
    RFC_aid_centers = pickle.load(open(f'{models_folder}/RFC_aid_centers.pickle', 'rb'))
    RFC_money = pickle.load(open(f'{models_folder}/RFC_money.pickle', 'rb'))
    RFC_death = pickle.load(open(f'{models_folder}/RFC_death.pickle', 'rb'))
    RFC_electricity = pickle.load(open(f'{models_folder}/RFC_electricity.pickle', 'rb'))
    RFC_military = pickle.load(open(f'{models_folder}/RFC_military.pickle', 'rb'))
    RFC_floods = pickle.load(open(f'{models_folder}/RFC_floods.pickle', 'rb'))
    RFC_cold = pickle.load(open(f'{models_folder}/RFC_cold.pickle', 'rb'))
    RFC_missing_people = pickle.load(open(f'{models_folder}/RFC_missing_people.pickle', 'rb'))
    RFC_search_and_rescue = pickle.load(open(f'{models_folder}/RFC_search_and_rescue.pickle', 'rb'))
    RFC_other_weather = pickle.load(open(f'{models_folder}/RFC_other_weather.pickle', 'rb'))
    RFC_shops = pickle.load(open(f'{models_folder}/RFC_shops.pickle', 'rb'))
    RFC_tools = pickle.load(open(f'{models_folder}/RFC_tools.pickle', 'rb'))
    RFC_refugees = pickle.load(open(f'{models_folder}/RFC_refugees.pickle', 'rb'))
    RFC_aid_related = pickle.load(open(f'{models_folder}/RFC_aid_related.pickle', 'rb'))
    RFC_shelter = pickle.load(open(f'{models_folder}/RFC_shelter.pickle', 'rb'))
    RFC_other_aid = pickle.load(open(f'{models_folder}/RFC_other_aid.pickle', 'rb'))
    RFC_security = pickle.load(open(f'{models_folder}/RFC_security.pickle', 'rb'))
    RFC_related = pickle.load(open(f'{models_folder}/RFC_related.pickle', 'rb'))
    RFC_buildings = pickle.load(open(f'{models_folder}/RFC_buildings.pickle', 'rb'))
    RFC_request = pickle.load(open(f'{models_folder}/RFC_request.pickle', 'rb'))
    RFC_offer = pickle.load(open(f'{models_folder}/RFC_offer.pickle', 'rb'))
    RFC_infrastructure_related = pickle.load(open(f'{models_folder}/RFC_infrastructure_related.pickle', 'rb'))
    RFC_food = pickle.load(open(f'{models_folder}/RFC_food.pickle', 'rb'))
    RFC_hospitals = pickle.load(open(f'{models_folder}/RFC_hospitals.pickle', 'rb'))
    RFC_medical_help = pickle.load(open(f'{models_folder}/RFC_medical_help.pickle', 'rb'))
    RFC_storm = pickle.load(open(f'{models_folder}/RFC_storm.pickle', 'rb'))
    RFC_medical_products = pickle.load(open(f'{models_folder}/RFC_medical_products.pickle', 'rb'))


headbar_style = {
    'text-align': 'center',
    'width': '33.33%',
    'fontSize': '27px',
    'fonColor': 'black',
    'border':'1px black solid',
    'border-radius': '25px',
} 

heading_style_h1 = {
    'text-align': 'center',
    'fontSize': '61px',
    'fontColor': 'black',
}

heading_style_h2 = {
    'text-align': 'center',
    'fontSize': '30px',
    'fontColor': 'black',
}

heading_style_h3 = {
    'text-align': 'center',
    'fontSize': '24px',
    'fontColor': 'black',
}

button_style_default = {
    'width':'10%',
    'border-radius': '10px',
    'border':'2px black solid',
    'text-align': 'center',
    'margin-left': '45%',
    'background-color': 'white',
    'color': 'black'
}

output_button_style_default = {
    'width':'14.25%',
    'border-radius': '10px',
    'border':'2px black solid',
    'text-align': 'center',
    'background-color': 'white',
    'color': 'black'
}

output_button_style_success = {
    'width':'14.25%',
    'border-radius': '10px',
    'border':'2px black solid',
    'text-align': 'center',
    'background-color': 'white',
    'color': 'black',
    'background-color': 'green',
    'color': 'black'
}

image_style_dict = {
    'text-align': 'center'
}

welcome_page_layout = html.Div([
    html.Br(),
    html.Br(),
    html.P('Welcome!', style=heading_style_h1),
    html.Br(),
    html.P('You have landed on Disaster Response Message Classification Project. This project helps in clssifying disaster response messages '\
            'in 35 Categories and vizualizing interesting trends in data provided by Figure 8.', style=heading_style_h2),
    html.Br(),
    html.Br(),
    html.Br(),
    html.P("Navigate to 'Classify Messages' and 'Vizualize Data' to play around with Classification Tool and Vizualize Trends in Training Data, "\
            "respectively.", style=heading_style_h3)

])

classify_message_page_layout = html.Div([
    html.Br(),
    html.Br(),
    html.P('Disaster Response Project', style=heading_style_h2),
    dcc.Textarea(placeholder='Enter your message here...', id='message-box', style={'width': '100%', 'border-radius': '10px'}),
    html.Br(),
    html.Button('Classify', id='classify-button', style=button_style_default),
    html.Br(),
    html.Br(),
    html.Br(),
    html.P('Message Categories:', style=heading_style_h3),
    html.Br(),
    html.Div([
        html.Button('Direct Report', id='Direct Report', style=output_button_style_default),
        html.Button('Clothing', id='Clothing', style=output_button_style_default),
        html.Button('Water', id='Water', style=output_button_style_default),
        html.Button('Weather Related', id='Weather Related', style=output_button_style_default),
        html.Button('Fire', id='Fire', style=output_button_style_default),
        html.Button('Earthquake', id='Earthquake', style=output_button_style_default),
        html.Button('Transport', id='Transport', style=output_button_style_default)
    ]),
    html.Div([
        html.Button('Other Infrastructure', id='Other Infrastructure', style=output_button_style_default),
        html.Button('Aid Centers', id='Aid Centers', style=output_button_style_default),
        html.Button('Money', id='Money', style=output_button_style_default),
        html.Button('Death', id='Death', style=output_button_style_default),
        html.Button('Electricity', id='Electricity', style=output_button_style_default),
        html.Button('Military', id='Military', style=output_button_style_default),
        html.Button('Floods', id='Floods', style=output_button_style_default),
    ]),
    html.Div([
        html.Button('Cold', id='Cold', style=output_button_style_default),
        html.Button('Missing People', id='Missing People', style=output_button_style_default),
        html.Button('Search And Rescue', id='Search And Rescue', style=output_button_style_default),
        html.Button('Other Weather', id='Other Weather', style=output_button_style_default),
        html.Button('Shops', id='Shops', style=output_button_style_default),
        html.Button('Tools', id='Tools', style=output_button_style_default),
        html.Button('Refugees', id='Refugees', style=output_button_style_default),
    ]),
    html.Div([
        html.Button('Aid Related', id='Aid Related', style=output_button_style_default),
        html.Button('Shelter', id='Shelter', style=output_button_style_default),
        html.Button('Other Aid', id='Other Aid', style=output_button_style_default),
        html.Button('Security', id='Security', style=output_button_style_default),
        html.Button('Related', id='Related', style=output_button_style_default),
        html.Button('Buildings', id='Buildings', style=output_button_style_default),
        html.Button('Request', id='Request', style=output_button_style_default),
    ]),
    html.Div([
        html.Button('Offer', id='Offer', style=output_button_style_default),
        html.Button('Infrastructure Related', id='Infrastructure Related', style=output_button_style_default),
        html.Button('Food', id='Food', style=output_button_style_default),
        html.Button('Hospitals', id='Hospitals', style=output_button_style_default),
        html.Button('Medical Help', id='Medical Help', style=output_button_style_default),
        html.Button('Storm', id='Storm', style=output_button_style_default),
        html.Button('Medical Products', id='Medical Products', style=output_button_style_default)
    ])
])

vizualize_data_page_layout = html.Div([
    html.Br(),
    html.Br(),
    html.P("Disaster Response Project Data Vizualization", style=heading_style_h2),
    html.Br(),
    html.Div([
        html.Img(src=f"data:image/png;base64,{base64.b64encode(open(GetGlobalVariables.data_viz_folder+'/Number of Messages received via different Genre.png', 'rb').read()).decode('ascii')}")
    ], style = image_style_dict),
    html.Br(),
    html.Div([
        html.Img(src=f"data:image/png;base64,{base64.b64encode(open(GetGlobalVariables.data_viz_folder+'/Number of Messages in different Categories.png', 'rb').read()).decode('ascii')}")
    ], style = image_style_dict),
    html.Br(),
    html.Div([
        html.Img(src=f"data:image/png;base64,{base64.b64encode(open(GetGlobalVariables.data_viz_folder+'/Number of Messages in different Categories by Genre.png', 'rb').read()).decode('ascii')}")
    ], style = image_style_dict),
    html.Br(),
    html.Div([
        html.Img(src=f"data:image/png;base64,{base64.b64encode(open(GetGlobalVariables.data_viz_folder+'/Distribution of Number of Categories to which a Message belongs.png', 'rb').read()).decode('ascii')}")
    ], style = image_style_dict),
    html.Br()
])


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.LITERA], title='Disaster Response Message Classifier')

app.layout = html.Div([
    dcc.Location(id='url'),
    html.Div([
        dbc.Nav([
            dbc.NavLink('Home', href='/home',active='exact', style = headbar_style),
            dbc.NavLink('Classify Messages', href='/classify-messages',active='exact', style = headbar_style),
            dbc.NavLink('Vizualize Data', href='/vizualize-data',active='exact', style = headbar_style)
        ], id='navigation-bar')
    ]),
    html.Div(children=[], id='content-space')
], style={'margin-left': '0.5%', 'margin-right': '0.5%', 'font-family': 'Garamond'})

app.validation_layout = html.Div([
    app.layout,
    welcome_page_layout,
    classify_message_page_layout,
    vizualize_data_page_layout,
])


@app.callback(
    dash.dependencies.Output('content-space', 'children'),
    dash.dependencies.Input('url', 'pathname')
)
def navigate_page(pathname):

    if pathname in ['/', '/home']:
        return welcome_page_layout
    elif pathname == '/classify-messages':
        return classify_message_page_layout
    elif pathname == '/vizualize-data':
        return vizualize_data_page_layout
    
    return welcome_page_layout


@app.callback(
    [dash.dependencies.Output(div_name.replace('RFC_', '').replace('_', ' ').title(), 'style') for div_name in GetGlobalVariables.model_name_list],
    dash.dependencies.Input('classify-button', 'n_clicks'),
    dash.dependencies.State('message-box', 'value')
)
def run_classifiers(n_clicks, input_text):
    if n_clicks:
        output_dict = {}
        for member in GetGlobalVariables.model_name_list:
            output_dict[member.replace('RFC_', '').replace('_', ' ').title()] = vars(GetGlobalVariables)[member].predict([input_text]).tolist()[0]
        
        output_style_list = []
        for key in output_dict.keys():
            if output_dict[key] == 1:
                output_style_list.append(output_button_style_success)
            else:
                output_style_list.append(output_button_style_default)

        return output_style_list
    return [output_button_style_default for i in GetGlobalVariables.model_name_list]


if __name__ =='__main__':
    app.run_server(debug=True, host='localhost', use_reloader=False)
