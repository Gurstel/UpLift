from collections import OrderedDict

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
            },
            {
                "answer": "My community",
                "nextQuestion": 8
            }
        ]

    },
    3: {
        "question": "What about your week would you highlight?",
        "answers": [
            {
                    "answer": "Stresses and problems",
                    "nextQuestion": 9
            },
            {
                "answer": "High moments of the week",
                "nextQuestion": 10
            }
        ]
    },
    4: {
        "question": "What is your social life like right now?"
    }
}

