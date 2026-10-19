# 🤖 Rule-Based AI Chatbot

A simple **Rule-Based AI Chatbot** developed in Python as part of **Artificial Intelligence — Project 1** for DecodeLabs Industrial Training Kit, Batch 2026.

The chatbot simulates basic human conversation using predefined responses, conditional statements, and a continuous conversation loop.

## 📌 Project Overview

This project demonstrates the fundamentals of Artificial Intelligence through rule-based decision-making. The chatbot receives user input, checks it against predefined conditions, and generates an appropriate response.

The project focuses on programming logic and control flow rather than machine learning or deep learning.

## 🎯 Objectives

- Understand the fundamentals of rule-based AI.
- Implement conditional logic using `if`, `elif`, and `else`.
- Handle user input and generate predefined responses.
- Maintain continuous interaction using a `while` loop.
- Implement exit commands to terminate the conversation.

## ✨ Features

- 👋 Greeting detection
- 💬 Basic conversational responses
- 🤖 AI-related question handling
- 🙏 Thank-you response handling
- ❓ Built-in help command
- 🔄 Continuous conversation loop
- 🚪 Multiple exit commands
- ⚠️ Handling of empty and unrecognized inputs

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Concepts:** Conditional Statements, Loops, String Manipulation, User Input
- **Libraries:** Python Standard Library only

No external packages are required.

## 📂 Project Structure

```text
Rule-Based-AI-Chatbot/
│
├── main.py    # Main chatbot implementation
└── README.md        # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/FarazMemon004/Task1-Artifical-Intelligence
```

### 2. Navigate to the Project Directory

```bash
cd Rule-Based-AI-Chatbot
```

### 3. Run the Chatbot

Make sure Python 3 is installed, then execute:

```bash
python main.py
```

On some systems, you may need to use:

```bash
python3 main.py
```

## 💻 Example Interaction

```text
WELCOME TO AI CHATBOT
Powered by DecodeLabs

Bot: Hello! I am your AI chatbot.
Bot: Type 'help' to see what I can do.
Bot: Type 'bye' or 'exit' to end the chat.

You: hi
Bot: Hello! How are you today?

You: what is your name
Bot: I am a Rule-Based AI Chatbot.

You: what is ai
Bot: AI stands for Artificial Intelligence.
Bot: It enables machines to perform tasks that
     normally require human intelligence.

You: help
Bot: Here are some things you can ask me:
- Hello / Hi
- How are you?
- What is your name?
- Who are you?
- What is AI?
- What is your purpose?
- Thank you
- Bye / Exit

You: bye
Bot: Goodbye! It was nice talking to you.
Bot: Thank you for using my chatbot.

Chatbot session ended.
```

## 🧠 How It Works

1. **Input Processing:** Receives a message from the user and normalizes it using `strip()` and `lower()`.
2. **Rule Matching:** Uses `if`, `elif`, and `else` statements to identify recognized inputs.
3. **Response Generation:** Prints the predefined response associated with the matched rule.
4. **Continuous Interaction:** Uses `while True` to keep the conversation active.
5. **Termination:** Uses `break` when the user enters an exit command.

## 💬 Supported Commands

| Command | Purpose |
|---|---|
| `hi`, `hello`, `hey` | Start a greeting |
| `how are you` | Ask about the chatbot |
| `what is your name` | Ask the chatbot's name |
| `who are you` | Ask about its identity |
| `what is ai` | Learn a basic AI definition |
| `what is your purpose` | Ask about its purpose |
| `thanks`, `thank you` | Express thanks |
| `help` | Display supported commands |
| `bye`, `goodbye`, `exit`, `quit` | End the conversation |

## ⚠️ Limitations

- Responses are based on predefined rules.
- The chatbot does not learn from previous conversations.
- It cannot understand every possible sentence.
- It does not use machine learning or natural language processing models.
- New responses must be added manually to the program.

## 🚀 Future Improvements

- Add more conversational rules and responses.
- Support additional greetings and common questions.
- Improve input matching to handle variations in sentence structure.
- Add a graphical user interface using Tkinter.
- Store conversation history in a file.
- Explore natural language processing in a future project.

## 📚 Learning Outcomes

After completing this project, the developer gains practical experience with:

- Python programming fundamentals
- Conditional statements and decision-making
- Loops and program termination
- String processing and user input
- The basic concept of rule-based artificial intelligence

## 👨‍💻 Project Information

- **Project:** Artificial Intelligence — Project 1
- **Project Title:** Rule-Based AI Chatbot
- **Training Organization:** DecodeLabs
- **Batch:** 2026
- **Language:** Python

## 📄 License

This project is intended for educational and learning purposes. You may add an MIT License if you wish to allow others to use, modify, and distribute the code under its terms.

---

**Built with Python 🐍 as a first step toward understanding Artificial Intelligence.**
