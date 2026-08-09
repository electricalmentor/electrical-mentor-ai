# Motor Troubleshooting Scenarios


motor_scenarios = {

    "Motor Won't Start": {

        "title": "480V Conveyor Motor Will Not Start",

        "equipment": """
        480V Three Phase Motor
        Across-the-line Starter
        MCC Bucket
        120V Control Circuit
        """,

        "symptom": """
        Operator reports:

        The conveyor motor will not start.
        """,

        "difficulty": "Apprentice Level I",
            "questions": [
        {
            "question": "What should you do first?",
            "answers": [
                "Replace the motor",
                "Ask questions about the failure",
                "Megger the motor",
                "Replace the contactor"
            ],
            "correct": "Ask questions about the failure",
            "points": 5
        },
        {
            "question": "You arrive at the MCC. The breaker is ON. What should you check next?",
            "answers": [
                "Check incoming voltage",
                "Replace the motor",
                "Check the bearings",
                "Order a new VFD"
            ],
            "correct": "Check incoming voltage",
            "points": 5
        },
        {
            "question": "The control transformer has 120 VAC and the start button is good, but the contactor coil has 0 VAC. What is the likely problem?",
            "answers": [
                "Failed motor",
                "Open control circuit",
                "Bad bearings",
                "Wrong overload setting"
            ],
            "correct": "Open control circuit",
            "points": 10
        }
    ],

    },


    "Motor Trips Breaker": {

        "title": "480V Motor Trips Breaker",

        "equipment": """
        480V Three Phase Motor
        MCC Bucket
        Overload Protection
        """,

        "symptom": """
        Operator reports:

        Motor immediately trips the breaker when started.
        """,

            "difficulty": "Apprentice Level II",

    "questions": [
        {
            "question": "The motor immediately trips the breaker when started. What should you do first?",
            "answers": [
                "Replace the motor",
                "Ask what happened before the failure",
                "Reset the breaker repeatedly",
                "Replace the overload relay"
            ],
            "correct": "Ask what happened before the failure",
            "points": 5
        },
        {
            "question": "The breaker trips instantly every time the motor is started. What should you check next?",
            "answers": [
                "Check for a short circuit",
                "Replace the bearings",
                "Increase the breaker size",
                "Replace the motor immediately"
            ],
            "correct": "Check for a short circuit",
            "points": 5
        },
        {
            "question": "You megger the motor and find very low insulation resistance to ground. What does this indicate?",
            "answers": [
                "Normal motor condition",
                "Possible insulation failure",
                "Correct phase rotation",
                "A bad start button"
            ],
            "correct": "Possible insulation failure",
            "points": 10
        }
    ],

},

    },


    "Motor Runs Backwards": {

        "title": "Three Phase Motor Running Backwards",

        "equipment": """
        480V Three Phase Motor
        Motor Starter
        Disconnect
        """,

        "symptom": """
        Operator reports:

        Motor rotation is incorrect.
        """,

        "difficulty": "Apprentice Level I",

    },


    "Motor Overheats": {

        "title": "Motor Overheating",

        "equipment": """
        480V Three Phase Motor
        Overload Relay
        Mechanical Load
        """,

        "symptom": """
        Operator reports:

        Motor temperature is higher than normal.
        """,

        "difficulty": "Apprentice Level II",

    }

}# Motor Troubleshooting Scenarios

