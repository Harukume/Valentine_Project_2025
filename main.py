from flask import Flask, redirect, url_for, render_template, request  #base for website
from flask_bootstrap import Bootstrap5  # design for website
import time

#creating app with css
app = Flask(__name__)
bootstrap = Bootstrap5(app)

#returned info
InfoToSend = {
    "TypeOfDate": "",
    "MainFood": "",
    "Dessert": "",
}


#Will you be mine valentine? Question with effects like gif and music
@app.route("/")  #Main pytanie
def home():
    return render_template("index.html")


#What do you want to do on Valentine day (Type of activity)

@app.route("/date", methods=['GET', 'POST'])
def date():
    date = ""
    if request.method == "POST":
        if request.form.get('Cinema') == 'Cinema':
            date = "Kino"
        elif request.form.get('Walk') == 'Walk':
            date = "Spacer"
        elif request.form.get('Clay') == 'Clay':
            date = "Modelina"
        elif request.form.get('TFT') == 'TFT':
            date = "TFT"
        elif request.form.get('Lazy_Day') == 'Lazy_Day':
            date = "Leniuchowanie"
        elif request.form.get('Proposition') == 'Proposition':
            date = request.form.get('anotherChoice')
        else:
            print("Error: Something is wrong")
        print(f"Wybrał: {date}")
        InfoToSend["TypeOfDate"] = date
        return redirect(url_for('food'))

    elif request.method == 'GET':
        time.sleep(5)
        return render_template("date.html")

#What do you want to eat on Valentine's Day?
@app.route("/food", methods=["GET", "POST"])
def food():
    food = ""
    if request.method == "POST":
        if request.form.get('Burger') == 'Burger':
            food = "Burger"
        elif request.form.get('Chinese_Food') == 'Chinese_Food':
            food = "Chińczyk"
        elif request.form.get('Pizza') == 'Pizza':
            food = "Pizza"
        elif request.form.get('Indian_Food') == 'Indian_Food':
            food = "Indian_Food"
        elif request.form.get('Proposition') == 'Proposition':
            food = request.form.get('anotherChoice')
        else:
            print("Error: Something is wrong")
        print(f"Wybrał: {food}")
        InfoToSend["MainFood"] = food
        return redirect(url_for('dessert'))

    elif request.method == 'GET':
        return render_template("food.html")

#TODO Co na deser
@app.route("/dessert")
def dessert():
    return render_template("dessert.html")
#TODO Wysyłanie odpowiedzi na maila

app.run(debug=True)
