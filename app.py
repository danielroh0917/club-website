from flask import Flask, render_template, request # 이건 따로 설치해야하는 library여서 method나 class의 양이 많기때문에 필요한것만 가져와서 쓸수있게 from을 붙인거
from registration import register # registration.py
# import random --> python 설치하면 자동으로 설치되는 library의 method/python 파일

app = Flask(__name__) # Flask라는 Object의 객체를 만드는 코드

# Get -> Read website data
# POST -> generate/create new data
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
        #지금은 홈페이지가 없어서 index에 signup 페이지 return

if __name__=="__main__":
    app.run(host='127.0.0.1', port=8000)
    # IP address: #.#.#.# --> 0~255 --> Domain name service: www.naver.com
    # port: service에 여러 문과 같은 존재 Ex) 네이버의 웹툰, 스포츠뉴스, 이메일 등등 각각의 서비스는 각각의 port가 지정되어있음
