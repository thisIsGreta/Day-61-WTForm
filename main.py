from flask import Flask, render_template, request
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf import FlaskForm, RecaptchaField
from flask_bootstrap import Bootstrap

SECRET_KEY = "gretaaa"
app = Flask(__name__)
app.config.from_object(__name__)
bootstrap = Bootstrap(app)


class CommentForm(FlaskForm):
    email = StringField(label="Email", validators=[Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = CommentForm(request.form)
    if request.method == 'POST' and form.validate():
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=form)


if __name__ == '__main__':
    app.run(debug=True)