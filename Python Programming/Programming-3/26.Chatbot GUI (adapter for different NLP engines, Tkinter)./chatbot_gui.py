import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk

class ChatbotGUI:
    def __init__(self, adapter):
        self.adapter = adapter
        self.window = tk.Tk()
        self.window.title("Chatbot")
        self.window.geometry("600x400")
        
        # Create main frame
        self.main_frame = ttk.Frame(self.window, padding="10")
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Create chat display
        self.chat_display = scrolledtext.ScrolledText(
            self.main_frame,
            wrap=tk.WORD,
            width=50,
            height=20,
            font=("Arial", 10)
        )
        self.chat_display.grid(row=0, column=0, columnspan=2, sticky="nsew")
        self.chat_display.config(state=tk.DISABLED)
        
        # Create input field
        self.input_field = ttk.Entry(self.main_frame, width=40)
        self.input_field.grid(row=1, column=0, sticky="ew")
        self.input_field.bind("<Return>", self.process_input)
        
        # Create send button
        self.send_button = ttk.Button(
            self.main_frame,
            text="Send",
            command=self.process_input
        )
        self.send_button.grid(row=1, column=1, sticky="e")
        
        # Configure grid weights
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)
        
        # Display welcome message
        self.display_message("Bot", "Hello! How can I help you today?")

    def run(self):
        self.window.mainloop()

    def process_input(self, event=None):
        user_input = self.input_field.get().strip()
        if not user_input:
            return
            
        self.display_message("You", user_input)
        self.input_field.delete(0, tk.END)
        
        response = self.adapter.get_response(user_input)
        self.display_message("Bot", response)

    def display_message(self, sender: str, message: str):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, f"{sender}: {message}\n")
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)
