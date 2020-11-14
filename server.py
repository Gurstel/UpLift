from flask import Flask, render_template, request, session
from questions import questions
from quotes import quotes
import random

app = Flask(__name__)
app.secret_key = "UpLiftAndAway"


@app.route('/')
@app.route('/home')
def homePage():
    return render_template("home.html")
    
@app.route('/questions')
@app.route('/questions/<category>/<questionIndex>')
def questionsPage():
    if "questionCategory" not in session:
        session["questionCategory"] = list(questions.keys())[0]
        session["questionIndex"] = 1

    # if category:
        

    return render_template(
        "questions.html", 
        questionCategory=session["questionCategory"], 
        questionIndex = session["questionIndex"], 
        question = questions[session["questionCategory"]][session["questionIndex"]]["question"], 
        answers = questions[session["questionCategory"]][session["questionIndex"]]["answers"]
    )

@app.route('/friends')
def friendPage():
    if 'friends' not in session:
        session['friends'] = []

    friendUsername = request.args.get('friendUsername')
    if friendUsername is not None:
        # add the friend
        session['friends'] = session['friends'] + [friendUsername]


    if len(session['friends']) == 0:
        fmessage = "Add your first friend!"
    else:
        fmessage = "Here are your friends:" 

    # if button

    return render_template(
        "friends.html",
        fmessage = fmessage,
        friends = session['friends']
    )

@app.route('/quotes')
def quotePage():

    quotenumber = (random.randint(0,61))
    specquote = quotes[quotenumber]
    session["quotes"]= specquote


    return render_template(
        "quotes.html",
        quotes = session["quotes"]


        )

@app.route('/settings')
def settingsPage():
    return render_template("settings.html")

if __name__ == "__main__":
    app.run(port=8000, debug=True)
    
