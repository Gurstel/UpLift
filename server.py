from flask import Flask, redirect, render_template, request, session
from questions import questions
from quotes import quotes
import random

app = Flask(__name__)
app.secret_key = "UpLiftAndAway"

@app.route('/')
@app.route('/login')
def loginPage():
    email = request.args.get("email")
    if email is not None:
        session["email"]=email
        return redirect("/questions/", code=302)
    return render_template("login.html")
    

@app.route('/home')
def homePage():
    print(session.get('traits'))
    traitStress = 'Long term stress' in session.get('traits', [])
    traitCovid = 'Lonely' in session.get('traits', [])
    print(traitCovid)
    return render_template("home.html", traitStress=traitStress, traitCovid=traitCovid)
    
@app.route('/questions/')
@app.route('/questions/<int:questionCategoryIndex>/<int:questionIndex>/<int:answerIndex>')
def questionsPage(questionCategoryIndex=None, questionIndex=None, answerIndex=None):
    print(session.get('traits'))
    if questionCategoryIndex is None:
        session["traits"] = []
        questionCategoryIndex = 0
        questionCategory = list(questions.keys())[questionCategoryIndex]
        questionIndex = 1
    else:
        #user answered a question, what's next
        questionCategory = list(questions.keys())[questionCategoryIndex]
        answer = questions[questionCategory][questionIndex]["answers"][answerIndex]
        if "nextQuestion" in answer:
            questionIndex = questions[questionCategory][questionIndex]["answers"][answerIndex]["nextQuestion"]
        else:
            session["traits"] = session["traits"] + [answer["trait"]]
            questionCategoryIndex += 1
            if questionCategoryIndex >= len(questions):
                return redirect("/home", code=302)
            questionCategory = list(questions.keys())[questionCategoryIndex]
            questionIndex = 1


    return render_template(
        "questions.html", 
        questionCategoryIndex=questionCategoryIndex, 
        questionCategory=questionCategory, 
        questionIndex = questionIndex, 
        question = questions[questionCategory][questionIndex]["question"], 
        answers = questions[questionCategory][questionIndex]["answers"]
    )

@app.route('/friends')
def friendPage():
    return render_template("friends.html")

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
    
