from flask import Flask, render_template, request, redirect, url_for, session
import ibm_db
from flask_mysqldb import MySQL
import re


app = Flask(__name__)
  
app.secret_key = 'a'

conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=125f9f61-9715-46f9-9399-c8177b21803b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30426;SECURITY=SSL;SSLServerCertificate=Certificate.crt;UID=dsl67814;PWD=SiCg7kTzUC9X1ICU",'','')

@app.route('/')

def home():
    return render_template('index.html')


@app.route('/login',methods =['GET', 'POST'])
def login():
    global userid
    msg = ''
    if request.method == 'POST' :
        username = request.form['username']
        password = request.form['password']
        sql = "SELECT * FROM user WHERE username =? AND password=?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print (account)
        if account:
            session['loggedin'] = True
            session['id'] = account['USERNAME']
            userid=  account['USERNAME']
            session['username'] = account['USERNAME']
            msg = 'Logged in successfully !'
            return render_template('home-page.html', msg = msg)
        else:
            msg = 'Incorrect username / password !'
    return render_template('login.html', msg = msg)

        

   
@app.route('/signup', methods =['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' :
        name = request.form['username']
        email = request.form['email']
        password = request.form['password']
        sql = "SELECT * FROM user WHERE password =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            msg = 'Account already exists !'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address !'
        elif not re.match(r'[A-Za-z0-9]+', name):
            msg = 'name must contain only characters and numbers !'
        else:
            insert_sql = "INSERT INTO  user VALUES (?, ?, ?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt,1,name)
            ibm_db.bind_param(prep_stmt,2,password)
            ibm_db.bind_param(prep_stmt,3,email)
            ibm_db.execute(prep_stmt)
            msg = 'You have successfully registered !'
    elif request.method == 'POST':
        msg = 'Please fill out the form !'
    return render_template('registration.html', msg = msg)

@app.route('/home-page')
def dashboard():
    return render_template('home-page.html')

@app.route('/product')
def product():
    return render_template('product-screen.html')

@app.route('/cart')
def cart():
    return render_template('products-cart.html')

@app.route('/buy-now')
def buy():
    return render_template('shopnow.html')

@app.route('/confirm')
def confirm():
    return render_template('confirmation.html')

@app.route('/about')
def about():
    return render_template('about.html')






@app.route('/logout')
def logout():
    session.pop('loggedin',None)
    session.pop('id',None)
    session.pop('username',None)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
    