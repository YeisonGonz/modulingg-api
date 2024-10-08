colors = {
    'ERROR': '\033[91m', # RED
    'INFO': '\033[92m', # GREEN
    'WARNING': '\033[93m', # YELLOW
    'BLUE': '\033[94m', # BLUE
    'MAGENTA': '\033[95m', # MAGENTA
    'CYAN': '\033[96m', # CYAN
    'RESET': '\033[0m'# RESET COLOR
}

def log_message(category, message):
    if category in colors:
        print(f"{colors[category]}{category}{colors['RESET']}: {message}{colors['RESET']}")
    
