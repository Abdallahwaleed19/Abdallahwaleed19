from .base_adapter import NLPAdapter

class SimpleNLPAdapter(NLPAdapter):
    def __init__(self):
        self.greetings = ["hi", "hello", "hey", "greetings"]
        self.farewells = ["bye", "goodbye", "see you", "farewell"]

    def get_response(self, user_input: str) -> str:
        user_input = user_input.lower()
        
        # Check for greetings
        if any(greeting in user_input for greeting in self.greetings):
            return "Hello! How can I help you today?"
        
        # Check for farewells
        if any(farewell in user_input for farewell in self.farewells):
            return "Goodbye! Have a great day!"
        
        # Check for questions
        if any(q in user_input for q in ["what", "how", "why", "when", "where", "who"]):
            return "That's an interesting question. Let me think about it..."
        
        # Default response
        return "I understand you said: " + user_input 