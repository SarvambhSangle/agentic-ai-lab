import datetime

# --- Action Execution Functions ---
def calculate_simple(query):
    # Basic extraction for "calculate 2+3"
    try:
        expression = query.replace("calculate", "").strip()
        result = eval(expression) # Simple rule-based math
        return f"Result: {result}"
    except:
        return "I couldn't calculate that. Please use format: calculate 2+3"

def get_date():
    return f"Today's date is: {datetime.date.today()}"

def get_greeting():
    return "Hello! I am your rule-based AI agent. How can I help you today?"

# --- Decision Logic (Keyword Matching) ---
def rule_based_decision(user_input):
    user_input = user_input.lower()
    
    if "calculate" in user_input:
        return calculate_simple(user_input)
    elif "date" in user_input:
        return get_date()
    elif "hello" in user_input or "hi" in user_input:
        return get_greeting()
    else:
        return "I'm sorry, I don't recognize that command."

# --- Input Handler ---
def main():
    print("--- Rule-Based Agent Active (Type 'exit' to quit) ---")
    while True:
        user_query = input("You: ")
        if user_query.lower() == 'exit':
            break
        
        # Process and Output
        response = rule_based_decision(user_query)
        print(f"Agent: {response}")

if __name__ == "__main__":
    main()