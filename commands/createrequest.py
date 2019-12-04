import command_system


def createrequest():
    message = 'I create request'
    return message, ''

createrequest_command = command_system.Command()

createrequest_command.keys = ['create request', 'создать заявку', 'прими заявку', 'прими жалобу', 'у меня проблема', 'создай заявку', 'помоги мне']
createrequest_command.description = 'Приму жалобу, создам заявку'
createrequest_command.process = Createrequest
