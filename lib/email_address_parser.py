import re

class EmailAddressParser:
    def __init__(self, string):
        self.string = string

    
    def parse(self):
        pattern = r"\b[a-zA-Z](?:\w*|\w*\.\w+)@(?:\w+(?:\.\w+)*\w*)\.[a-zA-Z]+\b"
        regex = re.compile(pattern)
        return sorted(set(regex.findall(self.string)))
        

if __name__ == "__main__":
    this = EmailAddressParser("talk@talk.com john.jones@flatironschool.com alexa@amazon.com")
    output = this.parse()
    print(output)