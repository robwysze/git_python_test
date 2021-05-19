class Phrase:
    def __init__(self):
        self.name = "PyTest"

    def hello_phrase(self):
        return "Hello {name}".format(name=self.name)

    def set_name(self, name):
        self.name = name
