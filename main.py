import pyshorteners
from flask import Flask, render_template, request, redirect, url_for, flash, make_response, session
import os
import sys
import bd
import bcrypt



app = Flask(__name__)

app.secret_key = os.urandom(30).hex()

data = list()


def short(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)

@app.route("/", methods=['POST','GET'])
def hello_world():
    start_url = request.form.get('shortener')
    
    if request.method == 'POST':
        if('user' in session):
            bd.cur.execute(f"INSERT INTO urls (url_name,short_url,user_email,count) VALUES (?,?,?,?)",(start_url,short(start_url),session['user'],1))
            # data = bd.cur.execute(f"SELECT short_url FROM urls WHERE user_email=?",(session['user'],)).fetchall()
        else:
            data.append(short(start_url))

    return render_template("index.html",urls=data)


@app.route("/reg", methods=['POST','GET'])
def reg():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        true_email = bd.cur.execute("SELECT email FROM users WHERE email=?",(email,)).fetchone()
        if true_email == email:
            return redirect(url_for('auth'))
        else:
            salt = bcrypt.gensalt()
            hash = bcrypt.hashpw(password.encode('utf-8'),salt)
            bd.cur.execute(f"INSERT INTO users (name,password,email) VALUES (?,?,?)",(name, hash, email))
            bd.con.commit()
            return redirect(url_for('auth'))

    return render_template("reg.html", title="Registration")


@app.route("/auth", methods=['POST', 'GET'])
def auth():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        true_email = bd.cur.execute(
            "SELECT email,password FROM users WHERE email=?", (email,)).fetchone()
        hash_pass = true_email[1]
        true_password = bcrypt.checkpw(password.encode('utf-8'),hash_pass)
        if true_email and true_password:
            session['user'] = email

            return redirect(url_for('hello_world'))
        else :
            return 'Проверьте правильность введенных данных или зарегистрируйтесь'

    return render_template("auth.html", title="Auth")

if __name__ == '__main__':
    app.run()




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
