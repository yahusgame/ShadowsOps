from colorama import Fore, init
init(autoreset=True, convert=True)

def success(msg: str) -> str:
    return Fore.GREEN + msg

def error(msg: str) -> str:
    return Fore.RED + msg

def info(msg: str) -> str:
    return Fore.CYAN + msg

def warning(msg: str) -> str:
    return Fore.YELLOW + msg
