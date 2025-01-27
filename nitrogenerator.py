import requests
from bs4 import BeautifulSoup
import string
import random
from colorama import Fore

def main(e=None):
    def generate_random_string(length):
        characters = string.ascii_letters + string.digits
        return ''.join(Fore.RED+random.choice(characters) for _ in range(length))


    def find_div_by_class(url, class_name):
        try:
            response = requests.get(url)
            response.raise_for_status()
            html_content = response.text
        except requests.exceptions.RequestException as e:
            print(f"Error {e}")
            return None

        soup = BeautifulSoup(html_content, 'html.parser')
        div = soup.find('div')
        
        return div

    while True:
        random_text = generate_random_string(random.randint(20, 30))
        print(random_text)
            
        url = "https://promos.discord.gg/" + random_text
        class_name = "errorBody_e75adc"

        found_div = find_div_by_class(url, class_name)

        if found_div:
            None
        else:
            print(f"{Fore.GREEN}ну всё прога работает")
            print(Fore.GREEN+url)
            break
        
if __name__ == "__main__":
    main()