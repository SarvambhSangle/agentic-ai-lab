import tools

# --- Decision Logic (Tool Selection) ---
def tool_picker(user_input):
    query = user_input.lower()
    
    # Decide which tool to use based on input [cite: 55]
    if "calculate" in query:
        return tools.calculator(query)
    
    elif "weather" in query:
        # Simple extraction: assumes user says "weather in [City]"
        city = query.split("in")[-1].strip() if "in" in query else "your area"
        return tools.get_weather(city)
    
    elif "summarize" in query:
        # Simple extraction: assumes user says "summarize: [Text]"
        content = query.split("summarize:")[-1].strip() if "summarize:" in query else query
        return tools.summarizer(content)
    
    else:
        return "I don't have a tool for that yet. Try 'calculate', 'weather', or 'summarize'."

# --- Input Handler ---
def main():
    print("--- Tool-Using Agent Active (Type 'exit' to quit) ---")
    while True:
        user_query = input("You: ")
        if user_query.lower() == 'exit':
            break
        
        response = tool_picker(user_query)
        print(f"Agent: {response}")

if __name__ == "__main__":
    main()