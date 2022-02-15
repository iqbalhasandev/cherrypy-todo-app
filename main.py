from threading import Thread
import subprocess

server = Thread(target=subprocess.run, args=(["python", "cherry_server.py"],))
browser = Thread(target=subprocess.run, args=(["python", "browser.py"],))

server.start()
browser.start()

server.join()
browser.join()