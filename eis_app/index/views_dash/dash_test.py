import dash
from dash import Dash , dcc , html
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

class dash_test:
    def wij_dashapp1( sname , url_path):
        dash_app1 = Dash( server= sname , url_base_pathname=url_path)
        dash_app1.layout = html.Div([
        html.H1('Hello Dash1'),
        html.Div([
            html.P('Dash converts Python classes into HTML'),
            html.P("This conversion happens behind the scenes by Dash's JavaScript front-end")
        ])
        ])
        return dash_app1

    def wij_dashapp2( sname , url_path):
        dash_app4 = Dash( server= sname , url_base_pathname=url_path)
        dash_app4.layout = html.Div([
            # display link and html
            dcc.Link('Navigate to "/dashapp1"',  href='/dashapp1/'),
            html.Br(),
            #dcc.Link('Navigate to "/dashapp4/page1"',href='/dashapp4/page1'),

            # represents the URL bar, doesn't render anything
            dcc.Location(id='url', refresh=False),

            # content will be rendered in this element
            html.Div(id='page-content'),
        ])

        @dash_app4.callback(Output('page-content', 'children'), 
                            [Input('url', 'href'), 
                            Input('url', 'pathname'),
                            Input('url', 'search'),
                            Input('url', 'hash')])
        def display_page(href, pathname, search, hash):
            return html.Div([
                html.H2('Displayed by callback:'),
                html.H4('href = {}'.format(href)),
                html.H4('pathname = {}'.format(pathname)),
                html.H4('search = {}'.format(search)),
                html.H4('hash = {}'.format(hash)),
            ])

        return dash_app4
    
    def wij_dashapp3( sname , url_path):
        app = Dash( server= sname , url_base_pathname=url_path)
        df = px.data.iris() # iris data 불러오기
        fig = px.scatter(df, x="sepal_length", y="sepal_width", color="species")

        # app layout: html과 dcc 모듈을 이용
        app.layout = html.Div(children=[
            # Dash HTML Components module로 HTML 작성 
            html.H1(children='Dash 테스트'),
            html.Div(children='''
                잉? 잘되네.?...
            '''),
            # dash.core.component(dcc)의 그래프컴포넌트로 plotly 그래프 렌더링
            dcc.Graph(
                id='graph1',
                figure=fig
            )
        ])       
        return app 
