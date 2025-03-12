from tkinter import *
from tkinter import scrolledtext

def send_message():
    user_message = entry.get()
    if user_message.strip():
        chat_area.insert(END, "Abdallah: " + user_message + "\n", "user")
        entry.delete(0, END)
        bot_response = get_bot_response(user_message)
        chat_area.insert(END, "Chat Bot: " + bot_response + "\n", "bot")
        chat_area.see(END)  # scroll to the end of the chat area

def get_bot_response(message):
    responses = {
        "hi": "Hi Abdallah ! How are You ? ",
        "i am fine and you too ?": "I am Fine too ",
        "do you want any thing ?": "No , Thanks abdallah"
    }
    return responses.get(message.lower(), "Hi Abdallah , I am busy now call me later !")

window = Tk()
window.title("Whatsapp")
window.geometry("400x500")
window.configure(bg="#2ecc71")  # green background

chat_area = scrolledtext.ScrolledText(window, wrap=WORD, width=50, height=20, bg="#ecf0f1", fg="#2c3e50")
chat_area.pack(pady=10)
chat_area.tag_config("user", foreground="#1abc9c")  # green
chat_area.tag_config("bot", foreground="#3498db")  # blue

entry = Entry(window, width=40, bg="#ecf0f1", fg="#2c3e50")
entry.pack(pady=5)

send_button = Button(window, text="Send", bg="#1abc9c", fg="#2c3e50", command=send_message)
send_button.pack()

window.mainloop()