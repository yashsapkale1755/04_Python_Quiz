🎯 Interactive Terminal Quiz Application

A light, interactive, command-line Python quiz application designed to test intermediate Python engineering concepts. Built with modular code architecture, defensive input handling, and runtime randomization.


🌟 Key Features

Data Integrity & Protection: Uses .copy() on source datasets to ensure raw quiz data remains pristine across sessions.

Dynamic Randomization: Leverages Python’s random.shuffle() to deliver a randomized sequence of questions every time the script runs.

Robust Input Sanitization: Implements .strip().upper() on user inputs to prevent false failures caused by extra spaces or lowercase letters.

Enumerated Output Formatting: Dynamically builds progress indicators (Question 1 of 5) using enumerate(..., start=1).

State Management: Accurately tracks user score throughout the execution lifecycle and outputs summary stats upon completion.


🛠️ Built With
Language: Python 3.x

Core Libraries: random (Standard Library)



🚀📋 Code Architecture Overview


├── QUIZ_DATA          # List of dictionaries holding raw questions, options, and answers
└── run_quiz()         # Core execution engine
    ├── Deep copy dataset
    ├── Shuffle items
    ├── Loop & capture user input (.strip().upper())
    ├── Evaluate responses & update score state
    └── Display final summary
