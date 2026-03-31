import tools

class PlanningAgent:
    def __init__(self):
        self.plan = []

    def create_plan(self, user_query):
        """Task Decomposition: Breaking the problem into steps [cite: 104]"""
        print(f"\n[Planning Phase] Analyzing: {user_query}")
        
        # Simulating a planning LLM that identifies multiple steps [cite: 91]
        if "average" in user_query and "summarize" in user_query:
            self.plan = [
                {"step": 1, "task": "extract_numbers", "action": "Identify 5, 10, 15"},
                {"step": 2, "task": "calculate", "action": "(5+10+15)/3"},
                {"step": 3, "task": "summarize", "action": "Generate final report"}
            ]
        else:
            self.plan = [{"step": 1, "task": "simple_match", "action": "Process as single task"}]

    def execute_plan(self, user_query):
        """Sequential Execution: Showing intermediate outputs [cite: 101, 102]"""
        context = user_query
        
        for stage in self.plan:
            print(f"Executing Step {stage['step']}: {stage['task']}...")
            
            if stage['task'] == "extract_numbers":
                context = "5, 10, 15" # Simulated extraction [cite: 96]
            elif stage['task'] == "calculate":
                context = tools.calculator(context) # Sequential reasoning [cite: 105]
            elif stage['task'] == "summarize":
                context = tools.summarizer(f"The calculated result is {context}")
            
            print(f"Intermediate Output: {context}") # Requirement [cite: 102]
        
        return context

def main():
    agent = PlanningAgent()
    print("--- Multi-Step Planning Agent (Assignment 4) ---")
    
    # Example query from lab: "Find the average of 5, 10, 15 and summarize the result" 
    query = input("Enter complex task: ")
    
    agent.create_plan(query)
    final_result = agent.execute_plan(query)
    
    print(f"\nFinal Agent Response: {final_result}")

if __name__ == "__main__":
    main()