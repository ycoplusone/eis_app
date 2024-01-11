import dash
from dash import Dash , dcc , html,dash_table , Input, Output,callback
from dash.exceptions import PreventUpdate
import plotly.express as px
import pandas as pd


external_stylesheets = ['../static/dash_style.css']

class dash_test:
    def wij_dash_test_app1( sname , url_path):
        dash_app1 = Dash( server= sname , url_base_pathname=url_path , external_stylesheets=external_stylesheets)
        dash_app1.layout = html.Div([
            html.Button('Click here to see the content', id='show-secret'),
            html.Div(id='body-div')
        ])

        @callback(
            Output('body-div', 'children'),
            Input('show-secret', 'n_clicks')
        )
        def update_output(n_clicks):
            if n_clicks is None:
                raise PreventUpdate
            else:
                return "Elephants are the only animal that can't jump"
        return dash_app1

    def wij_dash_test_app2( sname , url_path):
        dash_app4 = Dash( server= sname , url_base_pathname=url_path  , external_stylesheets=external_stylesheets )
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
    
    def wij_dash_test_app3( sname , url_path):
        app = Dash( server= sname , url_base_pathname=url_path , external_stylesheets=external_stylesheets )
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

    def wij_dash_test_app4( sname , url_path):
        '''판다스 코드 테스트
        select => 컬럼 , 조건
        delete => 조건
        update => 조건
        insert => 문법
        join , union , merge
        '''
        app = Dash( __name__ , server= sname , url_base_pathname=url_path , external_stylesheets=external_stylesheets)
        df  = px.data.iris() # iris data 불러오기
        fig = px.scatter(df, x="sepal_length", y="sepal_width", color="species")


        app.layout = html.Div([            
            html.H1(children='Pandas 테스트') ,
            html.Div(children='0. 데이터 로드(iris 데이터)') ,
            # dcc.Graph( id='graph1' , figure = fig) , 
            dash_table.DataTable(
                #id='datatable-interactivity',
                columns=[
                    {"name": i, "id": i, "deletable": False, "selectable": False} for i in df.columns
                ],
                data=df.to_dict('records'),
                editable=False,
                #filter_action="native",
                sort_action="native",
                sort_mode="multi",
                column_selectable="single",
                #row_selectable="multi",
                #row_deletable=True,
                selected_columns=[],
                selected_rows=[],
                page_action="native",
                page_current= 0,
                page_size= 5,
            ),            
            html.Div(children='1. 컬럼 확인' , id='output_01' ) ,
            dcc.Dropdown( df.columns  , id='input_01'),
            html.Br() , 
            html.Div(children='2. 데이터 조회 - 특정컬럼' ) ,
            dash_table.DataTable(
                columns=[
                    {"name": i, "id": i, "deletable": False, "selectable": False} for i in df[['sepal_width','petal_length']].columns
                ],
                data=df[['sepal_width','petal_length']].to_dict('records'),
                page_size= 5,
            ), 
            # 1-2. 데이터 조회 -- 전체 , 특정 컬럼 
            #print( df.head(10) )
            #print(df[['age', 'sex', 'bmi', 'children', 'smoker']].head(10))
            #print( df[['age']].head(10))


        ])
        @app.callback(
            Output('output_01', 'children'),
            Input('input_01', 'value')
        )
        def update_output(value):
            return f'1. 컬럼 확인 - {value}'


        return app     
    
    
