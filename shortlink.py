import pyshorteners
from termcolor import colored
import time
from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def generate_short_link(original_url):
    s = pyshorteners.Shortener()
    short_url = s.tinyurl.short(original_url)
    return short_url

def print_colored_slow(text, color, delay=0.03):
    for char in text:
        print(colored(char, color), end='', flush=True)
        time.sleep(delay)
    print()

while True:
    original_url = input(colored("Inserisci l'URL da accorciare (scrivi 'exit' per uscire): ", 'green'))

    if original_url.lower() == 'exit':
        print_colored_slow("\nGrazie per aver utilizzato questo tool. Guarda altre utility su t.me/VikingTerminal", 'cyan')
        break

    if is_valid_url(original_url):
        print_colored_slow("\nURL originale:", 'cyan')
        print_colored_slow(original_url, 'blue')

        short_url = generate_short_link(original_url)
        print_colored_slow("Short URL:", 'cyan')
        print_colored_slow(short_url, 'blue')
        print()
    else:
        print_colored_slow("Errore: Inserisci un dominio valido.\n", 'red')
