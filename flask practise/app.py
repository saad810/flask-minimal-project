from flask import Flask, render_template
# forms
from forms.signup import RegisterForm;
app = Flask(__name__)
app.config['SECRET_KEY'] = "2a12ca1bfdce4f47e62f65b2f6bec1b8"

@app.route("/")
def home():
    name = "name is Reyyan ikram"
    return render_template('index.html' , var = name)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    return render_template('signupp.html', form = form )


if __name__ == '__main__':
    app.run(debug=True)
