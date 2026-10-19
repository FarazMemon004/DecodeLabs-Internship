
# Project 1: Rule-Based AI Chatbot
# DecodeLabs - Artificial Intelligence
# Batch 2026

print("=" * 45)
print("       WELCOME TO AI CHATBOT")
print("          Powered by DecodeLabs")
print("=" * 45)

print("\nBot: Hello! I am your AI chatbot.")
print("Bot: Type 'help' to see what I can do.")
print("Bot: Type 'bye' or 'exit' to end the chat.")

# Continuous conversation loop
while True:

    # Get input from the user
    user_input = input("\nYou: ").strip().lower()

    # Handle empty input
    if user_input == "":
        print("Bot: Please type something so I can respond.")

    # Handle greetings
    elif user_input in ["hi", "hello", "hey", "assalam o alaikum"]:
        print("Bot: Hello! How are you today?")

    # Handle user's well-being
    elif user_input in ["how are you", "how are you?"]:
        print("Bot: I am doing great! Thanks for asking.")

    # Handle the user's name
    elif user_input == "what is your name":
        print("Bot: I am a Rule-Based AI Chatbot.")

    # Handle identity questions
    elif user_input in ["who are you", "who are you?"]:
        print("Bot: I am a simple chatbot created using Python.")

    # Handle AI-related questions
    elif user_input in ["what is ai", "what is ai?"]:
        print("Bot: AI stands for Artificial Intelligence.")
        print("Bot: It enables machines to perform tasks that")
        print("     normally require human intelligence.")

    # Handle questions about the project
    elif user_input in ["what is your purpose", "your purpose"]:
        print("Bot: My purpose is to demonstrate basic AI logic")
        print("     using predefined rules and conditions.")

    # Handle thanks
    elif user_input in ["thanks", "thank you", "thankyou"]:
        print("Bot: You're welcome!")

    # Handle help command
    elif user_input == "help":
        print("\nBot: Here are some things you can ask me:")
        print("- Hello / Hi")
        print("- How are you?")
        print("- What is your name?")
        print("- Who are you?")
        print("- What is AI?")
        print("- What is your purpose?")
        print("- Thank you")
        print("- Bye / Exit")

    # Handle exit commands
    elif user_input in ["bye", "goodbye", "exit", "quit"]:
        print("Bot: Goodbye! It was nice talking to you.")
        print("Bot: Thank you for using my chatbot.")
        break

    # Handle unrecognized input
    else:
        print("Bot: Sorry, I don't understand that yet.")
        print("Bot: Type 'help' to see what I can answer.")

print("\nChatbot session ended.")
