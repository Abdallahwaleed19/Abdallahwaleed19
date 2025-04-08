from socket import *
from tkinter import *
from threading import *

def handle_client(client_socket , address):
    log_text.insert(END, f"{address} connected\n")
    try : 
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            message  = data.decode().strip().lower()
            log_text.insert(END, f" Recived : {message}\n")
            if message == "hi" :
                response = "hi , How can i help you ? "
            elif message == "hello" :
                response = "hello , How can i help you ? "
            elif message == "how are you" :
                response = "I am fine , how about you ?"
            elif message == "i am fine" :
                response = "That's good to hear , how can i help you ?"
            else :
                response = "I'm sorry , I don't understand your question."
            client_socket.send(response.encode())
    except ConnectionResetError :
        log_text.insert(END, f"{address} disconnected\n")
    finally:
        client_socket.close()
        log_text.insert(END, f"{address} disconnected\n")

def start_server():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(("127.0.0.1", 12345))
    server_socket.listen(5)
    log_text.insert(END, "Server started\n")
    while True:
        client_socket, address = server_socket.accept() 
        client_thread = Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()

def start_server_thread():
    server_thread = Thread(target=start_server)
    server_thread.start()
root = Tk()
root.title(" Socket Server")
root.geometry("400x400")
start_button = Button(root, text="Start Server", command=start_server_thread)
start_button.pack(pady=20)
log_text = Text(root)
log_text.pack()
root.mainloop()