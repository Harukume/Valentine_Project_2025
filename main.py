from flask import Flask, redirect, url_for, render_template  #base for website
from flask_bootstrap import Bootstrap5  # design for website


#creating app with css
app = Flask(__name__)
bootstrap = Bootstrap5(app)

#TODO Czy będziesz moją walentynką
@app.route("/")  #Main pytanie
def hello_world():
    return render_template("index.html")


#TODO Co chcesz zrobić

#TODO Co jemy

#TODO Co na deser

#TODO Wysyłanie odpowiedzi na maila

app.run()
