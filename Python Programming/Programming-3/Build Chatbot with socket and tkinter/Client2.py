from socket import *
from tkinter import *
from threading import *
client_socket = None  
def send_message():
    global client_socket  
    message = message_entry.get()
    if message.strip():
        client_socket.send(message.encode())
        log_text.insert(END, f":User  {message}\n")
        message_entry.delete(0, END)
        data = client_socket.recv(1024)
        log_text.insert(END, f"Server: {data.decode()}\n")

def start_client2():
    global client_socket  
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 12345))
    log_text.insert(END, "Client started\n")
    send_button.config(state=NORMAL)
    close_button.config(state=NORMAL)

def close_client2():
    global client_socket 
    try:
        client_socket.close()
        log_text.insert(END, "Client closed\n")
    except OSError:
        log_text.insert(END, "Client already closed\n")
    send_button.config(state=DISABLED)
    close_button.config(state=DISABLED)

root = Tk()
root.title("Client 2")
root.geometry("400x400")
log_frame = Frame(root)
log_frame.pack()
log_text = Text(log_frame , height=20 , width=50)
log_text.pack(side=LEFT , fill=BOTH , expand=True)
Scrollbar1 = Scrollbar(log_frame , orient=VERTICAL , command=log_text.yview)
Scrollbar1.pack(side=RIGHT , fill=Y)
log_text.config(yscrollcommand=Scrollbar1.set)
message_entry = Entry(root , width=50)  
message_entry.pack()
send_button = Button(root , text="Send" , command=send_message , state=DISABLED)
send_button.pack()
start_button = Button(root , text="Start Client" , command=start_client2)
start_button.pack()
close_button = Button (root , text="Close Client" , command=close_client2 , state=DISABLED)
close_button.pack()
root.mainloop()