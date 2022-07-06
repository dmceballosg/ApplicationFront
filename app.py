from turtle import ht
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import dcc
import base64
import os
from urllib.parse import quote as urlquote
from flask import Flask, send_from_directory

from dash import Input, Output, State, html
from dash_bootstrap_components._components.Container import Container

GOVLOGO = "https://www.unidadvictimas.gov.co/sites/default/files/imageblock/logo-gov-co.png"
BACKGROUNDHEADER = "https://www.unidadvictimas.gov.co/sites/default/files/styles/slide_700_350/public/banner_unidad_en_linea-01_opt_1.jpg?itok=wK_UE0xp"
IMGFOOTER = "/assets/img/logo-footer.png"


links = html.Div([

    dbc.NavItem(dcc.Link('Search Batch', href='/search_batch', style={
        "textDecoration": "none", "marginRight": "10px", "color": "#fff"})),
    dbc.NavItem(dcc.Link('Upload Data', href='/upload_data', style={
        "textDecoration": "none", "color": "#fff"})),
    dbc.NavItem(dbc.NavLink("About", href="/", style={
        "textDecoration": "none", "color": "#fff"})),
], className="navbar-nav-link")

search_bar = dbc.Row(
    [
        links,
        dbc.Row([
            dbc.Col(dbc.Input(type="search", placeholder="Search")),
            dbc.Col(
                dbc.Button(
                    "Search", color="primary", className="ms-2", n_clicks=0
                ),
                width="auto",
            )],style={"width":"auto"}),
    ],
    className="g-0 ms-auto flex-nowrap mt-3 mt-md-0 visible-menu",
    align="center",
)


navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.NavItem(dcc.Link(html.I(className="bi bi-house-fill", style={"fontSize": "25px", "marginTop": "-3px"}), href='/',
                                 style={"textDecoration": "none", "marginRight": "15px", "color": "#fff"})),

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

            dcc.Location(id='url', refresh=False),


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
    className="navbar-fixed-top",
)

backgroundHeader = dbc.Container(
    dbc.Container(
        dbc.Row(
            dbc.Col(html.Img(src=BACKGROUNDHEADER,
                             style={"width": "80%"}, className="img-padding")),
            align="center",
            className="img-background"), style={"padding": "0px"}
    ), style={"padding": "0px"},
)

img_footer = dbc.Container(
    dbc.Row(
        [
            dbc.Col(html.Img(src=IMGFOOTER, style={
                "width": "150px", "height": "100px"})),
        ],
        align="center",
        className="img-background",
    ),
),

list_group = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        dbc.Row(
                            [
                                dbc.Col(html.I(className="bi bi-facebook",
                                               style={"fontSize": "25px", "marginTop": "-3px"})
                                        ),
                                dbc.Col(html.I(className="bi bi-twitter",
                                               style={"fontSize": "25px", "marginTop": "-3px"})
                                        ),
                            ]),
                        dbc.Row(
                            [
                                dbc.Col(html.I(className="bi bi-instagram",
                                               style={"fontSize": "25px", "marginTop": "-3px"})
                                        ),
                                dbc.Col(html.I(className="bi bi-youtube",
                                               style={"fontSize": "25px", "marginTop": "-3px"})
                                        ),
                            ]

                        )

                    ], md=2, className="icons-footer"),

                dbc.Col(html.Div(
                    [
                        html.P(
                            "Unidad para la Atención y la Reparación Integral a las Víctimas"),
                        html.P("Sede administrativa"),
                        html.P(
                            "Carrera 85D No. 46A - 65, Complejo logístico San Cayetano. Conmutador: +57 (601) 7965150"),
                        html.P("Bogotá: Carrera 85D No. 46A - 65, Complejo logístico San Cayetano. Código Postal: 111071.Medellín: Calle 49 No 50-21 piso 14, Edificio del Café. Código Postal: 050010."),
                        html.P(
                            "© Copyrigth 2019 - Todos los derechos reservados Gobierno de Colombia."),
                    ]), md=6),
                dbc.Col(html.Div([
                        html.P("Teléfono conmutador: +57 (601) 426 11 11."),
                        html.P("Línea Gratuita Nacional: (01 8000 911 119)."),
                        html.P("Correo institucional:"),
                        html.P("servicioalciudadano@unidadvictimas.gov.co"),
                        ], style={'paddingTop': '15px'}), md=4,),
            ],
            className="footer",
            style={"minWidth": "100%"},
        )
    ],
    style={"minWidth": "100%"}
)

tab1_content = dbc.Card(
    dbc.CardBody(
        [
            html.Div(
                [
                    dbc.Row(
                        [
                            dbc.Col(html.Div([
                                dcc.Input(id='name1', placeholder='Name 1', type='text'),
                            ])),
                            dbc.Col(html.Div([
                                dcc.Input(id='name2', placeholder='Name 2', type='text'),
                            ])),
                            dbc.Col(html.Div([
                                dcc.Input(id='lastname1', placeholder='LastName 1', type='text'),
                            ])),
                            dbc.Col(html.Div([
                                dcc.Input(id='lastname2', placeholder='LastName 2', type='text')
                            ])),
                        ]
                    ),
                    dbc.Row(
                        dbc.Button("Search", color="primary",
                                   className="button-send",),
                        style={"display": "flex", "justifyContent": "center",
                        "margin-top": "30px"}
                    ),
                ],
            )
        ], className="search-name",
    ),
    className="search-name",
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            html.Div([
                dcc.Upload(
                    id='upload-data',
                    children=html.Div([
                        'Drag and Drop or ',
                        html.A('Select Files')
                    ]),
                    style={
                        'width': '400px',
                        'display': 'flex',
                        'justifyContent': 'center',
                        'height': '60px',
                        'lineHeight': '60px',
                        'borderWidth': '1px',
                        'borderStyle': 'dashed',
                        'borderRadius': '5px',
                        'textAlign': 'center',
                    },
                    # Allow multiple files to be uploaded
                    multiple=True
                ),
                html.Div(id='output-data-upload'),
            ]),
            html.Div(
                dbc.Alert("Upload your file in csv format", color="warning", className="alert"), className="alert-div"),
        ]
    ),
    className="mt-3",
)

tabs = dbc.Tabs(
    [
        dbc.Tab(tab1_content, label="Search by name"),
        dbc.Tab(tab2_content, label="Search in batch")
    ],
)

app = dash.Dash(external_stylesheets=[
                dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP])
app.title = "DS4A"

# UPLOAD FILES
UPLOAD_DIRECTORY_ND = "./upload_new_data"

if not os.path.exists(UPLOAD_DIRECTORY_ND):
    os.makedirs(UPLOAD_DIRECTORY_ND)

def download(path):
    """Serve a file from the upload directory."""
    return send_from_directory(UPLOAD_DIRECTORY_ND, path, as_attachment=True)


upload = html.Div(
    [
        dcc.Upload(
                id='upload-data',
                children=html.Div([
                'Drag and Drop or ',
                html.A('Select Files')
                ]),
                style={
                'width': '400px',
                'display': 'flex',
                'justifyContent': 'center',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
                },
                multiple=True
            ),
            html.Div(id='output-data-upload'),
            html.Div(dbc.Alert("Upload your file in csv format",
            color="warning", className="alert"), className="alert-div"),
        html.H5("File List"),
        html.Ul(id="file-list"),
    ],
)

def save_file(name, content):
    """Decode and store a file uploaded with Plotly Dash."""
    data = content.encode("utf8").split(b";base64,")[1]
    with open(os.path.join(UPLOAD_DIRECTORY_ND, name), "wb") as fp:
        fp.write(base64.decodebytes(data))


def uploaded_files():
    """List the files in the upload directory."""
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY_ND):
        path = os.path.join(UPLOAD_DIRECTORY_ND, filename)
        if os.path.isfile(path):
            files.append(filename)
    return files


def file_download_link(filename):
    """Create a Plotly Dash 'A' element that downloads a file from the app."""
    location = "/download/{}".format(urlquote(filename))
    return html.A(filename, href=location)


@app.callback(
    Output("file-list", "children"),
    [Input("upload-data", "filename"), 
    Input("upload-data", "contents")],
)

def update_output(uploaded_filenames, uploaded_file_contents):
    """Save uploaded files and regenerate the file list."""

    if uploaded_filenames is not None and uploaded_file_contents is not None:
        for name, data in zip(uploaded_filenames, uploaded_file_contents):
            save_file(name, data)

    files = uploaded_files()
    if len(files) == 0:
        return [html.Li("No files yet!")]
    else:
        return [html.Li(file_download_link(filename)) for filename in files]

# FOOTER
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

dinamicLayout = html.Div([
    navbar,
    html.Div(id='page-content'),
    footer
])



@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/upload_data':
        return upload
    elif pathname == '/search_batch':
        return tabs
    else:
        return backgroundHeader


app.layout = dbc.Container(
    [
        dinamicLayout
    ],
    style={"maxWidth": "none", "padding": "0px"},
)

if __name__ == "__main__":
    app.run_server(debug=True, port=1234)

