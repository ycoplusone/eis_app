'''
목표사항 : 데이터들을 비슷한 속성낄 분류
알고리즘 : k-means clustering
종속변수 : 비지도학습이라 종속변수 없음
평가지표 : 엘보우 기법, 실루엣 점수
사용모델 : kmeans
데이터셋 : 
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans # 학습 모델
from sklearn.preprocessing import StandardScaler 
from sklearn.metrics import silhouette_score # 실루엣 측정




file_url = 'https://raw.githubusercontent.com/musthave-ML10/data_source/main/example_cluster.csv'
data = pd.read_csv( file_url )



#sns.scatterplot(x='var_1' , y='var_2' , data = data) # 산점도 그리기
#plt.show()

def knn01():
    from sklearn.cluster import KMeans # 학습 모델
    distance = []
    for i in range(2,10):        
        k_model = KMeans(n_clusters=i , random_state=100 ) # 모델 객체 생성
        k_model.fit(data)
        print(i ,k_model.inertia_ )
        distance.append( k_model.inertia_ ) # 이너셔 계수가 평평해지는 구간이 군집의 적정 계수라고 이해.
    
    sns.lineplot( x=range(2,10) , y=distance ) # 
    plt.show()

def app01():
    
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
    scaler = StandardScaler()
    scaler_df = pd.DataFrame( scaler.fit_transform(customer_agg) , columns = customer_agg.columns , index = customer_agg.index )

    #print( scaler_df.head() )
    #이너셔 거리 측정
    dis = []
    for i in range(2,10):
        km = KMeans( n_clusters = i )
        km.fit( scaler_df )
        labels = km.predict( scaler_df )
        dis.append( km.inertia_ ) #이너셔 리스트
    print(dis)

    # 실루엣 측정 # 실루엣 측정은 가장 높은 계수의 갯수가 좋은 값이다.
    sil = []
    for i in range(2,10):
        km = KMeans( n_clusters=i )
        km.fit( scaler_df )
        labels = km.predict(scaler_df)
        sil.append( silhouette_score( scaler_df , labels ) )
    print(sil)

    km = KMeans( n_clusters=4 )
    km.fit( scaler_df )
    scaler_df['label'] = km.predict(scaler_df)
    
    scaler_df_mean = scaler_df.groupby('label').mean() #평균
    scaler_df_count = scaler_df.groupby('label').count()['category_travel'] # 등장ㅅ횟수
    #print( scaler_df_mean )

    #print( scaler_df_count )
    print( data.count() )
    print( scaler_df.count() )

def app03():
    '''판다스 코드 테스트
    select => 컬럼 , 조건
    delete => 조건
    update => 조건
    insert => 문법
    join , union , merge
    '''
    # 0. 데이터 준비.
    file_url = 'https://media.githubusercontent.com/media/musthave-ML10/data_source/main/insurance.csv'
    df = pd.read_csv( file_url )
    #print(df.head())

    # 1-1.  컬럼 확인. => ['age', 'sex', 'bmi', 'children', 'smoker', 'charges']    
    # print( df.columns )

    # 1-2. 데이터 조회 -- 전체 , 특정 컬럼 
    #print( df.head(10) )
    #print(df[['age', 'sex', 'bmi', 'children', 'smoker']].head(10))
    #print( df[['age']].head(10))

    # 1-3. 특정 행 선택 열의 인덱스 값으로 행 선택
    #print( df.loc[1] ) 
    #print( df.loc[0:1] ) 
    #print( df.loc[0:1]['age'] )  # 특정 열 
    #print( df.loc[0:1][['age', 'sex', 'bmi', 'children', 'smoker']] )   #특정열

    # 1-4. 조건의 
    # print( df[df['age'] == 19].head(10)  ) # 조건 하나 나이가 19살인 조건
    print( df[df['age'] == 19][ ['sex', 'bmi', 'children', 'smoker'] ]  ) # 조건 하나 나이가 19살인 조건 






    




    



    

    

app03()