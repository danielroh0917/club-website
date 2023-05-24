import sqlite3 as sq # as <-- sqlite3를 sq로 짧게 바꿔주는 코드
import bcrypt

def hash_password(password):
    password = password.encode('utf-8') # 비밀번호를 컴퓨터 언어로 암호화
    salt = bcrypt.gensalt() # 한번더 꼬아서 암호화를 해주는 코드
    hashed = bcrypt.hashpw(password, salt) # 암호화된 password와 salt를 합쳐주는 역할 -> hash할때 비밀번호가 컴퓨터 언어로 암호화 되어있어야하기때문에 앞에서 encode 해줬음
    hashed = hashed.decode('utf-8')
    return hashed

def register(username,password,re_password,birthday,gender,email,phone):
    conn = sq.connect("database/project.db") # conn = database 그자체(?)
    cur = conn.cursor() # cur = database에서 실행되는 모든것들을 책임지는 object(?)
    if password == re_password:
        try: # Primary Key인 username이 이미 존재할때 오류가 뜨지않고 메세지로 보여지게 만드는 코드 (오류가 뜨면 서버에 문제가 생기고 웹사이트가 작동이 안되기때문에 오류 메세지가 필요함)
            hashed = hash_password(password)
            conn.execute("INSERT INTO USERINFO(username,password,birthday,gender,email,phone) VALUES(?,?,?,?,?,?)",(username,hashed,birthday,gender,email,phone))
        except sq.IntegrityError:
            print("Already Exist")
        conn.commit()
        conn.close()
    else:
        print("비밀번호가 일치하지않습니다")

def login(username,password):
    if checkPassword(username, password): # == True는 생략
        return True
    else:
        return False

def checkPassword(username, password):
    conn = sq.connect("database/project.db")
    cur = conn.cursor()
    cur.execute('SELECT password FROM USERINFO WHERE username=(?)',(username,))
    user = cur.fetchone() # 바로 위에서 실행된 코드의 결과값을 가져오는 코드
    # If there is no 'username' in our database, user = None
    if user == None: #유저가 존재하지 않음
        return False
    #print(user) --> ('qwer',)
    pw = user[0] # 'qwer' # user[0]에서 0은 user(Tuple)에서 index를 의미함
    password_encoded = password.encode('utf-8') # 유저가 입력한 password를 컴퓨터 언어로 바꿔주는 코드
    result = bcrypt.checkpw(password_encoded, pw.encode('utf-8')) # pw.encode('utf-8')를 통해 pw(hashed)를 password_encoded와 마찬가지로 컴퓨터 언어로 바꾼뒤에 둘을 비교해주는 코드
    if result == True:
        return True
    else:
        return False

def getBirthday(username):
    conn = sq.connect("database/project.db")
    cur = conn.cursor()
    cur.execute('SELECT birthday FROM USERINFO WHERE username=(?)',(username,))
    birthday = cur.fetchone()
    return birthday[0]

def getGender(username):
    conn = sq.connect("database/project.db")
    cur = conn.cursor()
    cur.execute('SELECT gender FROM USERINFO WHERE username=(?)',(username,))
    gender = cur.fetchone()
    return gender[0]

def getEmail(username):
    conn = sq.connect("database/project.db")
    cur = conn.cursor()
    cur.execute('SELECT email FROM USERINFO WHERE username=(?)',(username,))
    email = cur.fetchone()
    return email[0]

def getPhone(username):
    conn = sq.connect("database/project.db")
    cur = conn.cursor()
    cur.execute('SELECT phone FROM USERINFO WHERE username=(?)',(username,))
    phone = cur.fetchone()
    return phone[0]
