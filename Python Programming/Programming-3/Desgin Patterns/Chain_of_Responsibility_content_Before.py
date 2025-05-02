class Content:
    def __init__(self, text):
        self.text = text

def filter_content(content):
    if "spam" in content.text:
        print("spam detected")
    elif "adult" in content.text:
        print("adult detected")
    elif "violence" in content.text:
        print("violence detected")
    else:
        print("content is clean")


contents = [
    Content("This is a clean content"),
    Content("This is a spam content"),
    Content("This is an adult content"),
    Content("This is a violence content"),
]

for content in contents:
    filter_content(content)

