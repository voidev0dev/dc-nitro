from nitrogenerator import *
import threading

if __name__ == "__main__":
    threads = []
    for i in range(5):
        t = threading.Thread(target=main, args=(i,)).start()
        threads.append(t)