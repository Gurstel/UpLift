from flask import Flask, redirect, render_template, request, session
from questions import questions
from quotes import quotes
import random

app = Flask(__name__)
app.secret_key = "UpLiftAndAway"

# Set up login endpoint
@app.route('/')
@app.route('/login')
def loginPage():
    # Save email to user session when form is submitted and redirect to questions
    email = request.args.get("email")   
    if email is not None:
        session["email"]=email
        return redirect("/questions/", code=302)

    # Render login page
    return render_template("login.html")
    
# Set up home endpoint
@app.route('/home')
def homePage():
    # Render home page passing user traits
    traitStress = 'Long term stress' in session.get('traits', [])
    traitCovid = 'Lonely' in session.get('traits', [])
    return render_template("home.html", traitStress=traitStress, traitCovid=traitCovid)

# Set up questions endpoint
@app.route('/questions/')
@app.route('/questions/<int:questionCategoryIndex>/<int:questionIndex>/<int:answerIndex>')
def questionsPage(questionCategoryIndex=None, questionIndex=None, answerIndex=None):
    if questionCategoryIndex is None:
        # Initialize question variables when user first arrives
        session["traits"] = []
        questionCategoryIndex = 0
        questionCategory = list(questions.keys())[questionCategoryIndex]
        questionIndex = 1
    else:
        # Handle user's answer to a question
        questionCategory = list(questions.keys())[questionCategoryIndex]
        answer = questions[questionCategory][questionIndex]["answers"][answerIndex]
        if "nextQuestion" in answer:
            # If category has another question move to it
            questionIndex = questions[questionCategory][questionIndex]["answers"][answerIndex]["nextQuestion"]
        else:
            # Reached the end of a category, set the appropriate trait in the user session
            session["traits"] = session["traits"] + [answer["trait"]]

            # Check if there are other categories remaining.  If so go to next category, otherwise redirect home
            questionCategoryIndex += 1
            if questionCategoryIndex >= len(questions):
                return redirect("/home", code=302)
            questionCategory = list(questions.keys())[questionCategoryIndex]
            questionIndex = 1

    # Render the questions page
    return render_template(
        "questions.html", 
        questionCategoryIndex=questionCategoryIndex, 
        questionCategory=questionCategory, 
        questionIndex = questionIndex, 
        question = questions[questionCategory][questionIndex]["question"], 
        answers = questions[questionCategory][questionIndex]["answers"]
    )

# Set up friends endpoint
@app.route('/friends')
def friendPage():
    # Initiliaze friends list in user session
    if 'friends' not in session:
        session['friends'] = []

    # Handle adding a friend to the user session
    friendUsername = request.args.get('friendUsername')
    if friendUsername is not None:
        session['friends'] = session['friends'] + [friendUsername]

    
    if len(session['friends']) == 0:
        fmessage = "Add your first friend!"
    else:
        fmessage = "Here are your friends:" 

    # Render friends page
    return render_template(
        "friends.html",
        fmessage = fmessage,
        friends = session['friends']
    )

# Set up quotes endpoint
@app.route('/quotes')
def quotePage():
    # Pick a random quote
    quotenumber = (random.randint(0,61))
    specquote = quotes[quotenumber]
    session["quotes"]= specquote

    # Render quotes page
    return render_template(
        "quotes.html",
        quotes = session["quotes"]
    )

# Set up settings endpoint
@app.route('/settings')
def settingsPage():
    # Render settings page
    return render_template("settings.html")

if __name__ == "__main__":
    # Start the server
    app.run(port=8000, debug=True)
    
