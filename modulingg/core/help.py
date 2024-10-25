from modulingg.controllers.config import CONFIGURATION, CommandsDictionary, CommandsDictionaryHelp
from modulingg.decorators.commandManager import CommandManager

BROADCAST_MESSAGE = "📦 Modulingg Helper :) | You are running version {} \n\n\tYou can see all commands available here.\n"
BROADCAST_MESSAGE_COMMAND = "📦 Modulingg Helper :) | Command {} \n\n\t {} \n"

class Help:
    def __init__(self, command=None):
        commandList = CommandManager.get_commands()
        if command and command in commandList:
            commandHelp = CommandsDictionaryHelp.read_config()
            print(BROADCAST_MESSAGE_COMMAND.format(command,commandHelp[command]))
        else:
            print(BROADCAST_MESSAGE.format(CONFIGURATION['modulingg_version']))
            self._returnCommands(commandList)
        
    def _returnCommands(self, commands_list):
        commands_dict = CommandsDictionary().read_config()
        for command in commands_list:
            print(f'\t{command}: {commands_dict[command]}')
        print('\n\n')