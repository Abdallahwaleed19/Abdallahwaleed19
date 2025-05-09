from chatbot_gui import ChatbotGUI
from adapters.simple_nlp_adapter import SimpleNLPAdapter

def main():
    adapter = SimpleNLPAdapter()
    gui = ChatbotGUI(adapter)
    gui.run()

if __name__ == "__main__":
    main()
