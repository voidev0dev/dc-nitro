from nitrogenerator import *
import threading
from colorama import Fore

if __name__ == "__main__":
    treads = []
    for i in range(20):
        t = threading.Thread(target=main, args=(i,))
        treads.append(t)
        time.sleep(0.07)
        print(Fore.YELLOW+"Setting up threads...")
        
        if len(treads) >= 20:
            for i in treads:
                i.start()