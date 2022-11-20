# from tkinter.tix import Form
from flask import Flask ,render_template,url_for,request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods = ["POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        qualification = request.form["qualify"]
        age = request.form["age"]
        email = request.form["email"]
        
        
        message = name + " --- " + email + " --- " + qualification + " --- " + age
        
        return render_template("index.html", y = message)
        
        
    

if __name__ == '__main__':
    app.run(debug=True)