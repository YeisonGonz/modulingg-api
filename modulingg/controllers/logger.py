colors = {
    'ERROR': '\033[91m', # RED
    'INFO': '\033[92m', # GREEN
    'WARNING': '\033[93m', # YELLOW
    'BLUE': '\033[94m', # BLUE
    'MAGENTA': '\033[95m', # MAGENTA
    'CYAN': '\033[96m', # CYAN
    'RESET': '\033[0m'# RESET COLOR
}
BROADCAST_MESSAGE = "📦 Modulingg API Endpoints | You can see all Endpoints for '{}'\n"
def log_message(category, message):
    if category in colors:
        print(f"{colors[category]}{category}{colors['RESET']}: {message}{colors['RESET']}")
    
def endpoints_print(allEndpoints,module):
    print(BROADCAST_MESSAGE.format(module))
    for endpoint in allEndpoints:
        print(f"\t ⚪ 🚀 {endpoint}")
    