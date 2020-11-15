from collections import OrderedDict

# Create a map from categories to questions
questions = OrderedDict()

questions["conversation"] = {
    1: {
        "question": "What type of conservation are you looking to have?",
        "answers": [
            {
                    "answer": "Deep, personal conversations to make close connections",
                    "nextQuestion": 2
            },
            {
                "answer": "Light conversations about your week to elevate your mood",
                "nextQuestion": 3
            },
            {
                "answer": "Social building and confidence conversations to make friends",
                "nextQuestion": 4
            }
        ]
    },
    2: {
        "question": "Out of this list, what is the most important topic that you would talk about?",
        "answers": [
            {
                    "answer": "Myself",
                    "nextQuestion": 5
            },
            {
                "answer": "My family / friends",
                "nextQuestion": 6
            },
            {
                "answer": "My work / school",
                "nextQuestion": 7
            }
        ]

    },
    3: {
        "question": "What about your week would you highlight?",
        "answers": [
            {
                    "answer": "Stresses and problems",
                    "trait": "Short term stress"
                    
            },
            {
                    "answer": "High Moments of the wekk",
                    "trait": "optimisitc Happiness"
            }
        ]
    },
    4: {
        "question": "What is your social life like right now?",
        "answers": [
            {
                    "answer": "A lot of friends, but none of them close",
                    "trait": "Looking for close conversations"
            },
             {
                    "answer": "Few close friends that I can rely and confide in, but want to create new ones",
                    "trait": "Looking for close conversations"
            },
            {
                    "answer": "Not many friends/people to talk to",
                    "trait": "Introverted and looking for connections"
            },
        ]
    },
    5: {
        "question": "What about yourself would you talk about?",
        "answers": [
            {
                    "answer": "Stresses and problems",
                    "trait": "Long term stress"
            },
             {
                    "answer": "Outlok and insights",
                    "trait": "Seeks Advice"
            },
        ]
    },
    6: {
        "question": "What about your family  would you talk about?",
        "answers": [
            {
                    "answer": "Stresses and problems",
                    "trait": "Long term stress"
            },
             {
                    "answer": "How you help each other out",
                    "trait": "Gives Advice"
            },
        ]
    },
    7: {
        "question": "What about your work would you talk about?",
        "answers": [
            {
                    "answer": "What and how the job is",
                    "trait": "In the moment"
            },
             {
                    "answer": "What and how you want the job to be",
                    "trait": "Looks forward"
            },
        ]
    }
}

questions["corona"] = {
    1: {
        "question": "Have you been affected by Corona Virus?",
        "answers": [
            {
                    "answer": "Yes",
                    "nextQuestion": 2
            },
            {
                "answer": "No",
                "trait": "No COVID"
            },
        ]
    },
    2: {
        "question": "How has it affected your life?",
        "answers": [
            {
                "answer": "Sickened or killed a loved one",
                "trait": "Needs Corona Relief"
            },
            {
                "answer": "Makes me less social",
                "trait": "Lonely"
            }
        ]
    }
}


