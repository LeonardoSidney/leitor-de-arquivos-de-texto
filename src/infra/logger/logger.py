class Logger:
    def __init__(self, language="pt_BR"):
        self.language = language

    def info(self, message, *args):
        enumMessage = message.value[self.language]
        formatedMessage = f"INFO: >> {enumMessage.format(*args)}"
        print(formatedMessage)

    def error (self, message, *args):
        enumMessage = message.value[self.language]
        formatedMessage = f"ERROR: >> {enumMessage.format(*args)}"
        print(formatedMessage)
