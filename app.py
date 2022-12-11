from flask import Flask, render_template, url_for, redirect
from form import LoginForm, LoginForm1
app = Flask(__name__)

app.config['SECRET_KEY'] = '57bf24e23df89d5eab59adc875b50b76'

@app.route("/")
@app.route("/home")
def home():
    return render_template('fake_login/home.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'JohnDoe' and form.password.data == 'Ih812changing!':
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