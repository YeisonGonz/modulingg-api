from modulingg.controllers.config import CommandsDictionary, CommandsDictionaryHelp, DynamicConfig
from modulingg.decorators.commandManager import CommandManager

BROADCAST_MESSAGE = "📦 Modulingg Helper :) | You are running version {} \n\n\tYou can see all commands available here.\n"
BROADCAST_MESSAGE_COMMAND = "📦 Modulingg Helper :) | Command {} \n\n\t {} \n"

config = DynamicConfig()
class Help:
    def __init__(self, command=None):
        commandList = CommandManager.get_commands()
        if command and command in commandList:
            commandHelp = CommandsDictionaryHelp.read_config()
            print(BROADCAST_MESSAGE_COMMAND.format(command,commandHelp[command]))
        else:
            print(BROADCAST_MESSAGE.format(config.get('modulingg_version')))
            self._returnCommands(commandList)
        
    def _returnCommands(self, commands_list):
        try:
            commands_dict = CommandsDictionary().read_config()
            for command in commands_list:
                print(f'\t{command}: {commands_dict[command]}')
            print('\n\n')
        except FileNotFoundError:
            print('Error: Unable to find the configuration file.')
        except KeyError:
            print('Error: To find command help')