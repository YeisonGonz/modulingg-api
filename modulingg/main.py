from .core.CLI import CLI

try:
    CLI().cmdloop()
except KeyboardInterrupt:
    print("Goodbye...")
    