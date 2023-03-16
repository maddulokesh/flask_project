from flask import Flask,render_template,request,session,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,login_manager,LoginManager
from flask_login import login_required,current_user


local_server= True
app = Flask(__name__)
app.secret_key='loyallaughing'


login_manager=LoginManager(app)
login_manager.login_view='login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/farmers'
db=SQLAlchemy(app)


class User(UserMixin,db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50))
    email=db.Column(db.String(50),unique=True)
    password=db.Column(db.String(1000))
    
class Buy(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50))
    email=db.Column(db.String(50))
    productname=db.Column(db.String(50))
    productquantity=db.Column(db.String(50))
    
class Sell(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(50))
    email=db.Column(db.String(50))
    productname=db.Column(db.String(50))
    productquantity=db.Column(db.String(50))
    

@app.route('/')
def index(): 
    return render_template('index.html')


@app.route('/signup',methods=['POST','GET'])
def signup():
    if request.method == "POST":
        username=request.form.get('username')
        email=request.form.get('email')
        password=request.form.get('password')
        print(username,email,password)
        user=User.query.filter_by(email=email).first()
        if user:
            flash("Email Already Exist","warning")
            return render_template('/signup.html')
        encpassword=generate_password_hash(password)
        newuser=User(username=username,email=email,password=encpassword)
        db.session.add(newuser)
        db.session.commit()
        flash("Signup Succes Please Login","success")
        return render_template('login.html')


    return render_template('signup.html')

@app.route('/buy',methods=['POST','GET'])
def buy():
    if request.method == "POST":
        username=request.form.get('username')
        email=request.form.get('email')
        productname=request.form.get('productname')
        productquantity=request.form.get('productquantity')
        neworder=Buy(username=username,email=email,productname=productname,productquantity=productquantity)
        db.session.add(neworder)
        db.session.commit()
        flash("Product Successfully Ordered","success")
        return render_template('buy.html')

          

    return render_template('buy.html')

@app.route('/sell',methods=['POST','GET'])
def sell():
    if request.method == "POST":
        username=request.form.get('username')
        email=request.form.get('email')
        productname=request.form.get('productname')
        productquantity=request.form.get('productquantity')
        neworder=Sell(username=username,email=email,productname=productname,productquantity=productquantity)
        db.session.add(neworder)
        db.session.commit()
        flash("Product Successfully Placed","success")
        return render_template('sell.html')

          

    return render_template('sell.html')

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == "POST":
        email=request.form.get('email')
        password=request.form.get('password')
        user=User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password,password):
            login_user(user)
            flash("Login Success","primary")
            return redirect(url_for('index'))
        else:
            flash("invalid credentials","warning")
            return render_template('login.html')    

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logout SuccessFul","warning")
    return redirect(url_for('login'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/suggestion')
def suggestion():
    return render_template('suggestion.html')

app.run(debug=True)    