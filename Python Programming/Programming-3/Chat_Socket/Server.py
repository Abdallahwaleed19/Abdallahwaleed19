# from socket import *
# s = socket(AF_INET, SOCK_STREAM)
# print("Socket created successfully.")
# host = '127.0.0.1'
# port = 12345
# s.bind((host, port))
# print(f"Server bound to {host}:{port}")
# s.listen(5)
# print("Server is in listening mode.")
# while True:
#     print("Waiting for a connection...")
#     conn, addr = s.accept()
#     print(f"Connection from {addr}")
#     message = "Hello my Client"
#     conn.send(message.encode('utf-8'))  
#     print("Message sent to client.")
#     conn.close()
#     print("Connection closed.")


# from socket import *
# try : 
#     s = socket(AF_INET , SOCK_STREAM)
#     host = '127.0.0.1'
#     port = 7002
#     s.bind((host,port))
#     s.listen(5)
#     client , addr = s.accept()
#     print("Connection from " , addr[0])
#     while True:
#         x = client.recv(2048)
#         print("Client : " , x.decode('utf_8'))
#         y = input("Server : ")
#         client.send(y.encode('utf_8'))
#     s.close()
# except error as e :
#     print(e)
# except KeyboardInterrupt :
#     print("Chat is Finished")



