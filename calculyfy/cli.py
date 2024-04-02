from colorama import Fore, Style

   
def check():
    print(Fore.GREEN + Style.BRIGHT + 'You Have CalculyFy Installed Already!')

def dist_info():
    version_num = '1.0'
    author = 'Byte Legends hub'
    channel = 'https://www.youtube.com/@bytelegendshub'
    print(Fore.BLUE + Style.BRIGHT + "CalculyFy-Math-Library")
    print(Fore.CYAN + Style.BRIGHT + f"ClaculyFy Version: {version_num}")
    print(Fore.YELLOW + Style.BRIGHT + f"Library Author: {author}")
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + f"My YouTube Channel: {channel}")