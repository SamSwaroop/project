import datetime
from flask import Flask,render_template,request

app=Flask(__name__)

# @app.route('/')
# def index():
#     now=datetime.datetime.now()
#     new_year=now.month == 1 and now.day == 1
#     return render_template("index.html",new_year=new_year)


# @app.route('/index')
# def first():
#     name="Sam"
#     return render_template("index.html",headline=name)


# @app.route('/first')
# def first1():
#     return "Goodbye"

# @app.route('/second')
# def second1():
#     d=['Sam','Vishal','Mohan','Sai Kiran']
#     return render_template("second1.html",name=d)

# @app.route('/URL1')
# def Nav1():
#     return render_template("URLnav1.html")

# @app.route('/URL2')
# def Nav2():
#     return render_template("URLnav2.html")

# @app.route('/nav1')
# def navigation1():
#     return render_template("navigation1.html")

# @app.route('/nav2')
# def navigation2():
#     return render_template("navigation2.html")

@app.route('/')
def first():
    return render_template("index1.html")


@app.route('/form1')
def form1():
    return render_template("form1.html")

@app.route('/form2',methods=["POST"])
def form2():
    name=request.form.get("name")
    password=request.form.get("password")
    emailid=request.form.get("emailid")
    phoneNo=request.form.get("phonenumber")
    dob=request.form.get("birthday")
    return render_template("hello.html",name=name,password=password,mailid=emailid,phone=phoneNo,DOB=dob)

# @app.route('/')
# def Nav1():
#     return render_template("index1.html")

# @app.route('/URL1')
# def Nav2():
#     return render_template("demo.html")


    



