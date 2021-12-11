import pyautogui
import time
import threading

def clicker():
    time.sleep(7)
    while True:
        pyautogui.click()

def main():
    thread_list = []
    for thread in range(4):
        thread_process = threading.Thread(target=clicker)
        thread_list.append(thread_process)
        thread_list[thread].start()


        # t2 = threading.Thread(target=clicker)
        # t3 = threading.Thread(target=clicker)
        # t4 = threading.Thread(target=clicker)
        # t5 = threading.Thread(target=clicker)

        # t1.start()
        # t2.start()
        # t3.start()
        # t4.start()
        # t5.start()

if __name__ == "__main__":
    main()