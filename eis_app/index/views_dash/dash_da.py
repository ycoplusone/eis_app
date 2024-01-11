import dash
from dash import Dash , dcc , html,dash_table
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output


import pandas as pd
import numpy as np

from sklearn.cluster import KMeans # 학습 모델
from sklearn.preprocessing import StandardScaler 

#import matplotlib.pyplot as plt
#import seaborn as sns

external_stylesheets = ['../static/dash_style.css']

class dash_da:
    def wij_dash_da_01( sname , url_path):
        '''
        목표사항 : 데이터들을 비슷한 속성낄 분류
        알고리즘 : k-means clustering
        종속변수 : 비지도학습이라 종속변수 없음
        평가지표 : 엘보우 기법, 실루엣 점수
        사용모델 : kmeans
        데이터셋 : 가짜 데이터 이다.
        '''
        app = Dash( server= sname , url_base_pathname=url_path ,  external_stylesheets=external_stylesheets )
        #http://127.0.0.1:5000/static/data/example_cluster.csv
        file_url = 'https://raw.githubusercontent.com/musthave-ML10/data_source/main/example_cluster.csv'
        data = pd.read_csv( file_url )
        
        distance = []
        for i in range(2,10):        
            k_model = KMeans(n_clusters=i , random_state=100 , n_init=10) # 모델 객체 생성
            k_model.fit(data)
            #print(i ,k_model.inertia_ )
            distance.append( k_model.inertia_ ) # 이너셔 계수가 평평해지는 구간이 군집의 적정 계수라고 이해.
        
        kmean_model = KMeans(n_clusters=3 , random_state=100 , n_init=10) # 모델 객체 생성
        kmean_model.fit(data)
        
        data['label'] = kmean_model.predict(data) # 예측 레이블링

        #sns.lineplot( x=range(2,10) , y=distance ) # 
        #fig = px.scatter(df, x="sepal_length", y="sepal_width", color="species")
        fig0 = px.scatter( data , x='var_1' , y='var_2'  )
        fig1 = px.line(x=range(2,10) , y=distance        )
        fig2 = px.scatter( data , x='var_1' , y='var_2' , color='label' )



        # app layout: html과 dcc 모듈을 이용
        app.layout = html.Div(children=[
            # Dash HTML Components module로 HTML 작성 
            html.H1(children='K-Means 모델 테스트'),
            html.Div(children='''0. 데이터 로드 2 table'''),
            dash_table.DataTable(
                id='datatable-interactivity',
                columns=[
                    {"name": i, "id": i, "deletable": False, "selectable": False} for i in data.columns
                ],
                data=data.to_dict('records'),
                editable=False,
                #filter_action="native",
                #sort_action="native",
                sort_mode="multi",
                column_selectable="single",
                #row_selectable="multi",
                #row_deletable=True,
                selected_columns=[],
                selected_rows=[],
                page_action="native",
                page_current= 0,
                page_size= 10,
            ),

            html.Div(children='''1. 군집 이전 데이터 차트'''),
            dcc.Graph( id='graph0', figure = fig0  ),            
            
            html.Div(children='''2. 군집 차수 확인 그래프'''),
            dcc.Graph( id='graph1', figure = fig1  ),

            html.Div(children='''3. 군집 이전 데이터 차트'''),
            dcc.Graph( id='graph2', figure = fig2  ),

        ])
        


        return app
    
    def wij_dash_da_02( sname , url_path):
        ''''''        
        app = Dash( server= sname , url_base_pathname=url_path ,  external_stylesheets=external_stylesheets)

        file_url = 'https://raw.githubusercontent.com/musthave-ML10/data_source/main/customer.csv'
        data = pd.read_csv( file_url )

        #print( data.describe(include='all') )  #전체 개수 240454
        #print( 'data[cc_num].nunique()',data['cc_num'].nunique() ) #카드 번호 갯수 100개
        #print( 'data[category].nunique()',data['category'].nunique() ) # 카테고리 갯수 11개

        customer_dummy = pd.get_dummies( data , columns=['category'] ) # 더미 변수 변환
        #print(customer_dummy.head()) 
        cat_list = customer_dummy.columns[2:] # catlog 리스트
        #print(cat_list)
        for i in cat_list:
            customer_dummy[i] = customer_dummy[i] * customer_dummy['amt'] # 해당 값이
        #print(customer_dummy.head())

        customer_agg = customer_dummy.groupby('cc_num').sum() #카드번호별 금액 집계
        #print(customer_agg.head())


        app.layout = html.Div([
            html.H1('Hello Dash1'),
            html.Div([
                html.P('Dash converts Python classes into HTML'),
                html.P("This conversion happens behind the scenes by Dash's JavaScript front-end")
            ])
        ])
        return app

    