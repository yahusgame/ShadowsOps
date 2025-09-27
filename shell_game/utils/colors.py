from colorama import Fore, Style, init
init(autoreset=True, convert=True)

def success(msg: str) -> str:
    return Fore.GREEN + Style.BRIGHT + "✅ " + msg

def error(msg: str) -> str:
    return Fore.RED + Style.BRIGHT + "❌ " + msg

def info(msg: str) -> str:
    return Fore.CYAN + "ℹ️ " + msg

def warning(msg: str) -> str:
    return Fore.YELLOW + "⚠️ " + msg

def hint(msg: str) -> str:
    return Fore.BLUE + "💡 " + msg

def mentor(msg: str) -> str:
    return Fore.MAGENTA + Style.BRIGHT + msg

def hacker(msg: str) -> str:
    return Fore.RED + Style.BRIGHT + msg

def prompt(msg: str) -> str:
    return Fore.WHITE + Style.BRIGHT + msg
