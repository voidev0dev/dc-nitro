from nitrogenerator import *
import threading

if __name__ == "__main__":
    for i in range(20):
        t = threading.Thread(target=main, args=(i,)).start()