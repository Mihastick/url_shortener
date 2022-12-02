import pyshorteners
from flask import Flask,render_template
import os
import sys
import bd
import bcrypt


app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html",title="Main")

@app.route("/reg")
def reg():
    return render_template("registration.html",title="Registration")

if __name__ == '__main__':
    app.run()

def short(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))

# command = input("Введите команду ")
# if command == 'reg':
#     login = input("Введите ваш логин ")
#     email = input("Введите вашу почту ")
#     password = input("Введите ваш пароль ")
#     true_email = bd.cur.execute("SELECT email FROM users WHERE email=?",(email,)).fetchone()
#     if true_email == email:
#         print("Вы уже зарегистророваны ")
#     else:
#         salt = bcrypt.gensalt()
#         hash = bcrypt.hashpw(password.encode('utf-8'),salt)
#         bd.cur.execute(f"INSERT INTO users (name,password,email) VALUES (?,?,?)",(login, hash, email))
#         bd.con.commit()
#         print('Вы успешно зарегестрировались')
# if command == 'auth':
#     email = input("Введите вашу почту ")
#     password = input("Введите ваш пароль ")
#     true_email = bd.cur.execute("SELECT email,password FROM users WHERE email=?",(email,)).fetchone()
#     if(true_email) :

#         hash_pass = true_email[1]
#         true_password = bcrypt.checkpw(password.encode('utf-8'),hash_pass)
#         print("Вы успешно зашли в аккаунт")
#         command = input("Введите команду ")
        
#         if command == 'short_url':
#             start_url = input('Введите ссылку которую хотите сократить ')
#             bd.cur.execute(f"INSERT INTO urls (url_name,short_url,user_email,count) VALUES (?,?,?,?)",(start_url,short(start_url),email,1))

#     else :
#         print("Проверьте правильность введенных данных или зарегистрируйтесь.")



# short()

