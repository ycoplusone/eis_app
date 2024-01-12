from datetime import datetime
import math

from flask import Blueprint, url_for, request, render_template, g, flash
from werkzeug.utils import redirect

#from ..lib.dbconMysql import dbcon as dbcon
import index.lib.dbconMysql as dbcon


bp = Blueprint('themore', __name__, url_prefix='/themore')
dd = dbcon.DbConn()

@bp.route('/ratecal/<cur_id>' , methods=('GET', 'POST'))
def ratecal(cur_id):
     
     print('시작 cur_id',cur_id)
     ex_list = dd.get_exchange_info( {'CUR_ID':cur_id} )  # 결제 리스트     
     sh_info = dd.get_exchange_shinhan_info() # 신한 금액
     cal_info = {}

     def get_rate(cur_id , amt):
          _data = dd.get_ex_info( {'CUR_ID':cur_id  } )
          _ex_info = _data[0]
          _rate           = float( _ex_info['RATE'] )             #환율
          _bank_rate      = float( _ex_info['BANK_FIX_RATE'] )    #고시환율1차    
          _glo_brand_fee  = 0.011                     #국제브랜드수수료
          _for_sv_fee     = 0.0018                    #해외서비스수수료
          def rounddown(num):
            #내림
            return math.floor( num * 100) / 100
          
          _amt = round( (amt) ,2) #수량
          _aa1 = math.trunc( rounddown( round( _amt * _rate,2 ) * (1+_glo_brand_fee) ) * _bank_rate  )
          _aa2 = math.trunc( _aa1 * _for_sv_fee )   
          _aa3 = _aa1 + _aa2
          _aa4 = round(( _aa3 % 1000) * 2 / _aa3 ,4) if _aa3 != 0  else 0 
          _tmp = { 'QTY':_amt , 'AMT':_aa3 , 'ACC': _aa4 , 'CUR_ID':cur_id}
          return _tmp

     if request.method == 'POST':  # POST 요청
          print('post','='*30)
          _currencyAmount     = request.form['currencyAmount']
          _currencySelectBox  = request.form['currencySelectBox']
          print( '금액 : ', _currencyAmount , type( float(_currencyAmount )) )
          print( '외화 : ', _currencySelectBox )
          cal_info = get_rate( _currencySelectBox , float(_currencyAmount) )
     else :
          print('else','='*30)
          cal_info = None #get_rate( cur_id , 1.0 )


     return render_template('themore/ratecal.html' , ex_list = ex_list , sh_info = sh_info , cal_info=cal_info )
