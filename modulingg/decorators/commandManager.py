class CommandManager:
    command_list = []
    
    @classmethod
    def add(cls, command):
        cls.command_list.append(command)
    
    @classmethod
    def get_commands(cls):
        return cls.command_list

def commandManager(function):
    function_name = function.__name__.replace('do_', '')
    CommandManager.add(function_name)
    return function
