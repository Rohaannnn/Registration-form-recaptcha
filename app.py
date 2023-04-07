from flask import Flask, render_template, request, flash
from flask_recaptcha import ReCaptcha
from flask_wtf import RecaptchaField, FlaskForm
from wtforms import TextAreaField, PasswordField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config["SECRET_KEY"] = "rohaannn11223344"

app.config["RECAPTCHA_PUBLIC_KEY"] = "6LciJakjAAAAAGXcJO3n0SyG8HFUjw5rkLFKKdvS"
app.config["RECAPTCHA_PRIVATE_KEY"] = "6LciJakjAAAAAGvL0XwU6P6k56p03HVOKNKu5jna"


class widgets(FlaskForm):
    recaptcha = RecaptchaField()
    email= TextAreaField('email', validators=[DataRequired()])
    password= PasswordField('password', validators=[DataRequired()])


@app.route('/')
def hello_world():
    form=widgets()
    if request.method == "GET":
        return render_template("index.html",form=form)


    

if __name__ == "__main__":
   app.run(debug=True)