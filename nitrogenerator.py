import requests
from bs4 import BeautifulSoup
import string
import random
from colorama import Fore
import time

def main(e=None):
    def time_count():
        while True:
            unf_time = time.localtime()
            form_time = time.strftime("%H:%M:%S", unf_time)
            time.sleep(1)
            print(f"{Fore.BLUE}[{form_time}]")
    
    def generate_random_string(length):
        characters = string.ascii_letters + string.digits
        return ''.join(Fore.RED+random.choice(characters) for _ in range(length))


    def find_div_by_class(url, class_name):
        try:
            response = requests.get(url)
            html_content = response.text
            
        except requests.exceptions.RequestException as e:
            print(f"Error {e}")
            return None

        time.sleep(5)
        soup = BeautifulSoup(html_content, 'html.parser')
        div = soup.find('div')
        
        return div
    
    while True:
        random_text = generate_random_string(random.randint(23, 25))
        print(random_text)
            
        url = "https://promos.discord.gg/" + random_text
        class_name = "errorBody_e75adc"

        found_div = find_div_by_class(url, class_name)

        if found_div:
            pass
            
        else:
            print(f"{Fore.GREEN}{url}")
            break
    
    
if __name__ == "__main__":
    main()