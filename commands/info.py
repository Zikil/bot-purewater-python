import command_system


def info():
    message = ''
    for c in command_system.command_list:
        message += c.keys[0] + ' - ' + c.description + '\n'
    return message, ''


info_command = command_system.Command()

info_command.keys = ['help', 'помоги', 'помощь']
info_command.description = 'Покажу список команд'
info_command.process = Info
