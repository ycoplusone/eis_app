'''
목표 flask 환경 테스트
dash  연동
nicon 사이트 개편.
'''


# 1. 프로젝트 개발 폴더 생성
mkdir 개발폴더이름

# 2.가상화 환경 설정.
python -m venv 가상화이름

    # 2-1.가상화 활성화
    가상화이름\Scripts\activate 

    # 2-2.가상화 비활성화
    가상화이름\Scripts\deactivate 


# 3.설치 라이브러리
    # 플라스크 라이브러리
    pip install flask
    # SQLAlchemy ORM을 이용하기 위한 라이브러리.
    pip install flask-migrate
    # flask form 모듈 
    pip install flask-wtf
    # email-validator 라이브러리
    pip install email_validator
    # dash 라이브러리
    pip install dash
    # pandas 
    pip install pandas


# 4. 윈도우 path 설정
    - sysdm.cpl
    - 고급설정
    - 가상화이름 까지의 path 를 설정
    - set path 실행으로 등록된 path 확인.

# 5. activate , deactivate 실행파일 생성.
    - activate 파일 가상화 패스에 생성
    @echo off
    D:
    cd 개발폴더이름
    가상화이름\Scripts\activate

    - deactivate 파일 가상화 패스에 생성
    @echo off
    가상화이름\Scripts\deactivate    

# 6. sqlite3 파일 생성
    import sqlite3
    try:
        con = sqlite3.connect('test.db')    
    except Exception as e:
        print(e)
    finally:
        con.close()

# 7. ORM 관련 명령어
    - db 초기화 => 아래 코드 실행 후 프로젝트 폴더 확인 migrations 이 생성되었을것이다.
    flask db init

    - 모델 생성및 변경
    flask db migrate

    - 모델의 변경 내용을 실제 데이터 베이스에 적용할때
    flask db upgrade

# 8. flask shell 사용
    from index.models import questionboard, answerboard
    from datetime import datetime
    from index import db

    q = questionboard(subject='pybo가 무엇인가요?', content='pybo에 대해서 알고 싶습니다.', create_date=datetime.now())    
    
    db.session.add(q)
    db.session.commit()
