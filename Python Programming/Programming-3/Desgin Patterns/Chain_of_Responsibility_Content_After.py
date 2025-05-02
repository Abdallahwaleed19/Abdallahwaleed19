from abc import ABC, abstractmethod

class Content:
    def __init__(self, text):
        self.text = text

class Filter(ABC):
    def __init__(self):
        self.next_filter = None

    def set_next(self, filter):
        self.next_filter = filter
        return filter

    @abstractmethod
    def filter(self, content):
        pass

class SpamFilter(Filter):
    def filter(self, content):
        if "spam" in content.text:
            print("spam detected")
        elif self.next_filter:
            self.next_filter.filter(content)

class AdultFilter(Filter):
    def filter(self, content):
        if "adult" in content.text:
            print("adult detected")
        elif self.next_filter:
            self.next_filter.filter(content)

class ViolenceFilter(Filter):
    def filter(self, content):
        if "violence" in content.text:
            print("violence detected")
        elif self.next_filter:
            self.next_filter.filter(content)

class CleanFilter(Filter):
    def filter(self, content):
        print("content is clean")

# Create the filters
spam_filter1 = SpamFilter()
adult_filter1 = AdultFilter()
violence_filter1 = ViolenceFilter()
clean_filter1 = CleanFilter()

# Create the chain of responsibility
spam_filter1.set_next(adult_filter1).set_next(violence_filter1).set_next(clean_filter1)

# Process the contents
contents = [
    Content("This is a clean content"),
    Content("This is a spam content"),
    Content("This is an adult content"),
    Content("This is a violence content"),
]

for content in contents:
    spam_filter1.filter(content)