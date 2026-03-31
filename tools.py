import datetime

def calculator(expression):
    """Performs mathematical calculations[cite: 50]."""
    try:
        # Simple extraction logic
        clean_expr = "".join(filter(lambda x: x in "0123456789+-*/(). ", expression))
        return f"Result: {eval(clean_expr)}"
    except:
        return "Error in calculation."

def get_weather(city):
    """Mock weather tool[cite: 51]."""
    return f"The weather in {city} is currently 22°C and sunny."

def summarizer(text):
    """Simple text summarizer[cite: 52]."""
    sentences = text.split('.')
    return f"Summary: {sentences[0]}..." if len(sentences) > 1 else f"Summary: {text}"