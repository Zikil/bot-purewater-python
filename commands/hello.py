import command_system


def hello():
    message = 'Hello, friend!\nI am new bot'
    return message, ''

hello_command = command_system.Command()

hello_command.keys = ['hello', 'hi', 'привет', 'здравствуй', 'здравствуйте']
hello_command.description = 'Поприветствую тебя'
hello_command.process = Hello
