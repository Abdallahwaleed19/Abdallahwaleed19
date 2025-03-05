# from socket import * 
# s = socket(AF_INET,SOCK_STREAM) 
# host ='127.0.0.1'
# port = 12345
# s.connect((host, port)) 
# print(s.recv(1024)) 
# s.close()

# from socket import *
# try : 
#     s = socket(AF_INET , SOCK_STREAM)
#     host = '127.0.0.1'
#     port = 7002
#     s.connect((host,port))
#     while True :
#         y = input("Client : ")
#         s.send(y.encode('utf_8'))
#         x = s.recv(2048)
#         print("Server : " , x.decode('utf_8'))
#     s.close()
# except error as e : 
#     print(e)
# except KeyboardInterrupt:
#     print("Chat is Finsihed")

