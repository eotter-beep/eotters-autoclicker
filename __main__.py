import tkinter as tk
import os
import pyautogui
import time
root = tk.Tk()
root.title("eotter's autoclicker.")
def start():
    while True:
        pyautogui.click()  # left click
        time.sleep(interval)
def set_interval():
    global interval
    interval = float(interval_input.get()) / 1000
    start()
interval = os.system("cat autoclicker.sh | grep interval | cut -d' ' -f2")
label = tk.Label(root, text="Set milliseconds", )
interval_input = tk.Entry(root)
interval_input.pack()
interval_input.bind('<Return>', lambda e: set_interval())
label.pack()

root.mainloop()

"""
interval = 0.001  # time between clicks in seconds

while True:
    pyautogui.click()  # left click
    time.sleep(interval)
"""