# from tkinter.tix import Form
from flask import Flask ,render_template,url_for,request
from werkzeug.utils import secure_filename


app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/login', methods = ['GET',"POST"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        qualification = request.form["qualify"]
        age = request.form["age"]
        email = request.form["email"]
        
        f = request.files['file']
        f.save(secure_filename(f.filename))
        
        
        message = name + " --- " + email + " --- " + qualification + " --- " + age + " --- Your file uploaded successfully"
        
        return render_template("index.html", y = message)
        
        
    

if __name__ == '__main__':
    app.run(debug=True)