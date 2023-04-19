import sqlite3 as sq # as <-- sqlite3를 sq로 짧게 바꿔주는 코드

def register(username,password,re_password,birthday,gender,email,phone):
    conn = sq.connect("database/project.db") # conn = database 그자체(?)
    cur = conn.cursor() # cur = database에서 실행되는 모든것들을 책임지는 object(?)
    if password == re_password:
        try: # Primary Key인 username이 이미 존재할때 오류가 뜨지않고 메세지로 보여지게 만드는 코드 (오류가 뜨면 서버에 문제가 생기고 웹사이트가 작동이 안되기때문에 오류 메세지가 필요함)
            conn.execute("INSERT INTO USERINFO(username,password,birthday,gender,email,phone) VALUES(?,?,?,?,?,?)",(username,password,birthday,gender,email,phone))
        except sq.IntegrityError:
            print("Already Exist")
        conn.commit()
        conn.close()
    else:
        print("비밀번호가 일치하지않습니다")

def login(username,password):
    conn = sq.connect("database/project.db")
    cur = conn.cursor()
    cur.execute('SELECT password FROM USERINFO WHERE username=(?)',(username,))
    user = cur.fetchone() # 바로 위에서 실행된 코드의 결과값을 가져오는 코드
    # If there is no 'username' in our database, user = None
    if user == None: #유저가 존재하지 않음
        return False
    #print(user) --> ('qwer',)
    pw = user[0] # 'qwer' # user[0]에서 0은 user(Tuple)에서 indexr를 의미함
    if password == pw:
        return True
    else: #유저는 존재하나 패스워드가 다름
        return False

login("abcd","123456") #('qwer',)
