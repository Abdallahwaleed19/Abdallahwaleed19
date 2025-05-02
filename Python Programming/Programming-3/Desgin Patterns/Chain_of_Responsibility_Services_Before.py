class SupportRequest:
    def __init__(self, level, description):
        self.level = level  
        self.description = description

def handle_request(request):
    if request.level == 1:
        print("The request is being handled by the first level support team")
    elif request.level == 2:
        print("The request is being handled by the second level support team")
    elif request.level == 3:
        print("The request is being handled by the third level support team")
    else:
        print("The request cannot be handled by any support team")


requests = [
    SupportRequest(1, "problem with login"),
    SupportRequest(2, "server connection issue"),
    SupportRequest(3, "technical support needed"),
    SupportRequest(4, "unknown issue"),
]

for request in requests:
    handle_request(request)

