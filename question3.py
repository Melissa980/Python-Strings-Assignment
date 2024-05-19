# Question 3 Task 1 

user_input = input("Enter your command: ")

def parse_command(user_input):
    commands = ["help", "issue", "contact support"]
    for command in commands:
        if command in user_input.lower():
            if command == "help":
                print("What can I help you with?")
            elif command == "issue":
                print("I can look into that issue for you.")
            elif command == "contact support":
                print("Please provide more details so I can help you contact support.")
            return
    print("Sorry, I didn't catch that. How can I assist you?")

parse_command(user_input)

# Question 3 Task 2
user_input2 = input("Describe the issue: ")

def categorize_issue(user_input):
    if "login" in user_input.lower():
        print("Issue category: Login")
    elif "performance" in user_input.lower():
        print("Issue category: Performance")
    elif "error" in user_input.lower():
        print("Issue category: Error")
    else:
        print("Issue category: Other")

categorize_issue(user_input2)

