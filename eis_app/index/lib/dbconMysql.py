'''
Created on 2022. 7. 22.

@author: DLIVE
'''
import pymysql

class DbConn(object):
    ''' '''
    __url = 'themoreschool.cafe24.com'
    __id = 'themoreschool'
    __ps = 'school2@'
    __db = 'themoreschool'    
    __charset = 'utf8'
    
    __conn = ''
    

    def __init__(self):
        '''        
        '''
        self.__conn = pymysql.connect(host = self.__url , user = self.__id , password = self.__ps , db= self.__db , charset= self.__charset  )

    def upsert_ex_info(self , param ):
        ''' 환율 업데이트 '''
        try :
            cur = self.__conn.cursor()                        
            query = (
                " INSERT INTO exchange_rate_other_currency (BASE_DT, CUR_ID, CUR_NM, TO_CUR_ID,INPUT_DT, RATE,U_DATE,c_date) "
                " VALUES('{BASE_DT}', '{CUR_ID}', '{CUR_NM}', '{TO_CUR_ID}','{INPUT_DT}', '{RATE}', now(), now() ) "
                " on DUPLICATE key update INPUT_DT='{INPUT_DT}' , RATE='{RATE}' , PRE_RATE=RATE , PRE_U_DATE=U_DATE, u_date = now() "
            )
            query = query.format( **param )     
            
            cur.execute( query )
            self.__conn.commit()
        except Exception as e:
            print( 'upsert_ex_info', e ,'\n',query ,'\n',param )
        finally:
            pass                     

    def get_ex_info(self , param): 
              
        try :
            _lists = []
            query = (
                " select a.BASE_DT , a.CUR_ID , a.CUR_NM , a.RATE , a.INPUT_DT  , b.amt BANK_FIX_RATE "
                " from exchange_rate_other_currency a "
                " join exchange_shinhan_info b on (a.base_dt = b.base_dt ) "
                " where a.BASE_DT = ( select max(base_dt) from exchange_rate_other_currency ) "
                " AND a.CUR_ID = '{CUR_ID}' "
            )
            query = query.format( **param )
            cur = self.__conn.cursor(  pymysql.cursors.DictCursor)            
            cur.execute( query )            
            return cur.fetchall()         
        except Exception as e:
            print( 'get_ex_info => ' , e )  

    def upsert_ex_info2(self , param ):
        ''' 환율 업데이트 '''
        try :
            cur = self.__conn.cursor()                        
            query = (
                " INSERT INTO exchange_info (BASE_DT, CUR_ID , KIND , QTY, AMT, ACC, u_date, c_date)  "
                " VALUES('{BASE_DT}', '{CUR_ID}', '{kind}', {QTY}, {AMT},{ACC}, now(), now() ) "
                " on DUPLICATE key update QTY='{QTY}' , AMT='{AMT}' , ACC={ACC} , u_date = now() "
            )
            query = query.format( **param )
            cur.execute( query )
            self.__conn.commit()
        except Exception as e:
            print( 'upsert_ex_info2', e ,'\n',query ,'\n',param )
        finally:
            pass              

    def get_exchange_info(self , param): 
        ''' 환율 정보 리스트 '''              
        try :
            _lists = []
            query = (
                " SELECT   a.BASE_DT, a.CUR_ID, a.KIND, a.QTY, a.AMT, a.ACC , date_format(U_DATE, '%Y-%m-%d %H:%i') U_DATE , date_format(C_DATE, '%Y-%m-%d %H:%i') C_DATE "
                " FROM exchange_info a "
                " where a.base_dt = (select max(base_dt) from exchange_info) "
                " and a.CUR_ID  = '{CUR_ID}' "
                " ORDER BY 5 " 
            )
            query = query.format( **param )
            cur = self.__conn.cursor(  pymysql.cursors.DictCursor)            
            cur.execute( query )            
            return cur.fetchall()         
        except Exception as e:
            print( 'get_exchange_info => ' , e )   

    def get_exchange_shinhan_info( self ): 
        ''' 신한 송금 환율 정보 리스트'''              
        try :
            _lists = []
            query = (
                " SELECT  DATE(BASE_DT) BASE_DT , AMT ,  date_format(U_DATE, '%Y-%m-%d %H:%i') U_DATE "
                " from exchange_shinhan_info ei "
                " where base_dt = (select max(base_dt) from exchange_shinhan_info ) "
            )
            #query = query.format( **param )
            cur = self.__conn.cursor(  pymysql.cursors.DictCursor)            
            cur.execute( query )            
            return cur.fetchall()         
        except Exception as e:
            print( 'get_exchange_shinhan_info => ' , e ) 