
# Chatbot GUI Project

This is a Python-based chatbot GUI using Tkinter, supporting multiple NLP engines through an adapter pattern.

## Supported NLP Engines
- OpenAI GPT (ChatCompletion API)
- spaCy (basic NER example)
- Echo (simple testing)

## How to Use
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   python -m spacy download en_core_web_sm
   ```

2. Set your OpenAI API key:
   ```bash
   export OPENAI_API_KEY=your-api-key-here
   ```

3. Run the chatbot:
   ```bash
   python run_chatbot.py
   ```

4. In `run_chatbot.py`, comment/uncomment the adapter you want to use.
