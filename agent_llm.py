import sys
sys.path.append('../day1')
import tools

def simulated_llm_decision(user_query):
    """
    Simulates an LLM 'thinking' and selecting a tool based on context
    rather than just simple keyword matching.
    """
    print(f"--- LLM is processing query: '{user_query}' ---")
    
    # In a real LLM, this would be a prompt: 
    # "Given these tools (Calculator, Weather, Summarizer), which one fits: {user_query}?"
    
    query = user_query.lower()
    
    if any(word in query for word in ["plus", "minus", "times", "divided", "calculate", "math"]):
        return "calculator"
    elif any(word in query for word in ["temperature", "outside", "weather", "rain"]):
        return "weather"
    elif any(word in query for word in ["shorten", "tl;dr", "summarize", "gist"]):
        return "summarizer"
    else:
        return "unknown"

def main():
    print("--- LLM-Integrated Agent (Assignment 3) ---")
    while True:
        user_input = input("\nUser Query: ")
        if user_input.lower() == 'exit': break
        
        # 1. LLM Decides (Decision Logic) [cite: 71]
        selected_tool = simulated_llm_decision(user_input)
        
        # 2. Execution & Logging [cite: 72, 78]
        print(f"LOG: [Selected Tool: {selected_tool}]") 
        
        if selected_tool == "calculator":
            result = tools.calculator(user_input)
        elif selected_tool == "weather":
            # Extracting city name
            city = user_input.split("in")[-1].strip() if "in" in user_input else "London"
            result = tools.get_weather(city)
        elif selected_tool == "summarizer":
            result = tools.summarizer(user_input)
        else:
            result = "The LLM could not determine a tool for this request."
            
        # 3. Return Response [cite: 73]
        print(f"Agent Response: {result}")

if __name__ == "__main__":
    main()