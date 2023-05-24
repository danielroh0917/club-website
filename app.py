from flask import Flask, render_template, request, flash, redirect, url_for, session # 이건 따로 설치해야하는 library여서 method나 class의 양이 많기때문에 필요한것만 가져와서 쓸수있게 from을 붙인거
# flask는 html과 python을 연결해주는 역할
from registration import register, login, getPhone, getBirthday, getGender, getEmail # registration.py
from edit import changeInfo
from datetime import timedelta
# import random --> python 설치하면 자동으로 설치되는 library의 method/python 파일

app = Flask(__name__) # Flask라는 Object의 객체를 만드는 코드
SECRET_KEY = "abc" # 백앤드를 위한 웹사이트 password
app.config["SECRET_KEY"] = SECRET_KEY
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=60) # 웹사이트에 로그인한 상태로 머물수있는 시간을 제한하는 코드 (60분 뒤에 로그아웃) -> session이 초기화 되는 주기

# isLogin = False
# Get -> Read website data
# POST -> generate/create new data
@app.route('/', methods=["GET"])
def index():
    if 'username' in session:
        return render_template("index.html", isLogin = True, username = session['username']) # isLogin -> 로그인이 되어있는 상태인지 아닌지 판별해주는 역할
    else:
        return render_template("index.html", isLogin = False)

@app.route('/signup', methods=["GET","POST"]) # / <-- 웹사이트의 각 페이지를 구분짓는 표기
def signup(): # def <-- method 선언 : <-- 얘는 java로치면 {}
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        re_password = request.form["re-password"]
        birthday = request.form.get("birthday")
        gender = request.form.get("gender")
        phone = request.form["phone"]
        email = request.form["email"]
        register(username,password,re_password,birthday,gender,email,phone)
        print("Success")
    else: # Get Request
        return render_template("signUp.html") # 웹사이트의 각 페이지가 만들어질때마다 이렇게 return해야함

@app.route('/login', methods=["GET","POST"])
def signin():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if (login(username,password) == True):
            session['username'] = username # 어떤 유저가 login 되어있는지 구분해주는 역할 (username으로 식별)
            return redirect(url_for('index'))
        else:
            flash("아이디 혹은 비밀번호가 틀렸습니다.") # flash -> html에 메세지를 보낼수있게 해주는 코드
            return render_template("login.html")
    else:
        if 'username' in session:
            return redirect(url_for('index')) # 현재 페이지에서 다른 페이지로 return할때는 redirect 왜냐하면 다른 페이즈로 넘어갈때는 각 페이지의 함수를 통해야하기때문이다
        return render_template("login.html") # 현재 페이지 -> 현재 페이즈로 return할때는 render_template 왜냐하면 다른 함수를 통해갈 필요가 없기때문이다

@app.route('/logout')
def logout():
    session.pop("username", None) # session에 있는 username을 None으로 바꿈 -> username을 remove하는 역할
    return redirect(url_for('index'))

@app.route('/userinfo')
def userinfo():
    return render_template("userinfo.html", username = session['username'], birthday = getBirthday(session['username']), gender = getGender(session['username']), email = getEmail(session['username']), phone = getPhone(session['username']))

@app.route('/editinfo', methods=["GET","POST"])
def editinfo():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        new_password = request.form["re-password"]
        birthday = request.form.get("birthday")
        gender = request.form.get("gender")
        phone = request.form["phone"]
        email = request.form["email"]
        print(username,password,new_password,birthday,gender,email,phone)
        changeInfo(username,password,new_password,birthday,gender,email,phone)
        print("Success")
    else: # Get Request
        return render_template("editinfo.html")

if __name__=="__main__":
    app.run(host='127.0.0.1', port=8000)
    # IP address: #.#.#.# --> 0~255 --> Domain name service: www.naver.com
    # port: service에 여러 문과 같은 존재 Ex) 네이버의 웹툰, 스포츠뉴스, 이메일 등등 각각의 서비스는 각각의 port가 지정되어있음
