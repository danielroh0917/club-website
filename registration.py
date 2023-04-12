import sqlite3 as sq # as <-- sqlite3를 sq로 짧게 바꿔주는 코드

def register(username,password,re_password,birthday,gender,email,phone):
    conn = sq.connect("database/project.db")
    cur = conn.cursor()
    if password == re_password:
        try: # Primary Key인 username이 이미 존재할때 오류가 뜨지않고 메세지로 보여지게 만드는 코드 (오류가 뜨면 서버에 문제가 생기고 웹사이트가 작동이 안되기때문에 오류 메세지가 필요함)
            conn.execute("INSERT INTO USERINFO(username,password,birthday,gender,email,phone) VALUES(?,?,?,?,?,?)",(username,password,birthday,gender,email,phone))
        except sq.IntegrityError:
            print("Already Exist")
        conn.commit()
        conn.close()
    else:
        print("비밀번호가 일치하지않습니다")

register("xyz4","09814","09814","12/04/2023","M","sdjoj2@ijfd4","010214")
