from flask import Flask, redirect, url_for, render_template, request  #base for website
from flask_bootstrap import Bootstrap5  # design for website
import requests
import time

#creating app with css
app = Flask(__name__)
bootstrap = Bootstrap5(app)


#Will you be mine valentine? Question with effects like gif and music
@app.route("/")  #Main pytanie
def home():
    return render_template("index.html")


#TODO Co chcesz zrobić

@app.route("/date", methods=['GET', 'POST'])
def date():
    if request.method == "POST":
        if request.form.get('Cinema') == 'Cinema':
            print("Wybrał kino")
        elif request.form.get('Walk') == 'Walk':
            print("Wybrał spacer")
        elif request.form.get('Clay') == 'Clay':
            print("Wybrał modelinę")
        elif request.form.get('TFT') == 'TFT':
            print("Wybrał TFT")
        elif request.form.get('Lazy_Day') == 'Lazy_Day':
            print("Wybrał leniuchowanie")
        elif request.form.get('Proposition') == 'Proposition':
            hisChoice = request.form.get('anotherChoice')
            print(f"Wybrał: {hisChoice}")
        else:
            print("Error: Something is wrong")
        return render_template("index.html")
    elif request.method == 'GET':
        time.sleep(5)
        return render_template("date.html")


#TODO Co jemy

#TODO Co na deser

#TODO Wysyłanie odpowiedzi na maila

app.run()
