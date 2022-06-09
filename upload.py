from turtle import ht
import dash
import dash_bootstrap_components as dbc
from dash import dcc

from dash import Input, Output, State, html
from dash_bootstrap_components._components.Container import Container

GOVLOGO = "https://www.unidadvictimas.gov.co/sites/default/files/imageblock/logo-gov-co.png"
BACKGROUNDHEADER = "https://www.unidadvictimas.gov.co/sites/default/files/styles/slide_700_350/public/banner_unidad_en_linea-01_opt_1.jpg?itok=wK_UE0xp"
IMGFOOTER = "/assets/img/logo-footer.png"

# HEADER

search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(
            dbc.Button(
                "Search", color="primary", className="ms-2", n_clicks=0
            ),
            width="auto",
        ),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=GOVLOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("", className="ms-2")),
                    ],
                    align="center",
                    className="g-0",
                ),
                href="https://www.unidadvictimas.gov.co",
                style={"textDecoration": "none"},
            ),
            dbc.NavItem(dbc.NavLink("Search Batch", href="#", style={
                        "textDecoration": "none", "color": "#fff"})),
            dbc.NavItem(dbc.NavLink("Upload New Data", href="#", style={
                        "textDecoration": "none", "color": "#fff"})),
            dbc.NavItem(dbc.NavLink("About", href="#", style={
                        "textDecoration": "none", "color": "#fff"})),

            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                search_bar,
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
)

# FOOTER

img_footer =  dbc.Container(
        dbc.Row(
            [
                dbc.Col(html.Img(src=IMGFOOTER, style={"width": "150px", "height":"100px"})),
            ],
            align="center",
            className="img-background",
        ),
    ),

list_group =  html.Div(
    [
        dbc.Row(
            [
                dbc.Col(html.Div(img_footer),width=2),
                dbc.Col(html.Div(
                    [
                        html.P("Unidad para la Atención y la Reparación Integral a las Víctimas"),
                        html.P("Sede administrativa"),
                        html.P("Carrera 85D No. 46A - 65, Complejo logístico San Cayetano. Conmutador: +57 (601) 7965150"),
                        html.P("Bogotá: Carrera 85D No. 46A - 65, Complejo logístico San Cayetano. Código Postal: 111071.Medellín: Calle 49 No 50-21 piso 14, Edificio del Café. Código Postal: 050010."),
                        html.P("© Copyrigth 2019 - Todos los derechos reservados Gobierno de Colombia."),
                    ]), width=6),
                dbc.Col(html.Div([
                        html.P("Teléfono conmutador: +57 (601) 426 11 11."),
                        html.P("Línea Gratuita Nacional: (01 8000 911 119)."),
                        html.P("Correo institucional:"),
                        html.P("servicioalciudadano@unidadvictimas.gov.co"),
                    ], style={'paddingTop': '15px'}),width=4,),
            ],
            className="footer",
            style={"minWidth": "100%"},
        )
    ],
    style={"minWidth": "100%"}
)

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

footer = dbc.Container(
    dbc.Navbar(
        dbc.Container(
            [
               list_group
            ]
        ),
        color="#355bc6",
        dark=True,
        style={"maxWidth": "none"},
    ),
    className="footer-nav",
    style={"maxWidth": "none"},
)

# BODY

alert = html.Div(
    [
        dbc.Alert("Upload your file in csv format", color="warning")
    ]
)


upload = html.Div([
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-data-upload'),
])


def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'csv' in filename:
            message = "Correct format"

    except Exception as e:
        print(e)
        return html.Div([
            'There was an error processing this file. Remember upload a csv file'
        ])

    return html.Div([
        html.H5(message)
    ])


# RUNNING APP

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# add callback for toggling the collapse on small screens


@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


app.layout = dbc.Container(
    [
        navbar,
        upload,
        alert,
        footer
    ],
    style={"maxWidth": "none"},
)

if __name__ == "__main__":
    app.run_server(debug=True)
