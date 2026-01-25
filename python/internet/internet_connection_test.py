import os
import time
import threading
from datetime import datetime

def check_internet_connection(ip, timeout=2000):
    response = os.system(f"ping -n 1 -w {timeout} {ip} > nul 2>&1")
    return response == 0


def ping_async(ip, error_log):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    connected = check_internet_connection(ip)
    status = "연결 성공" if connected else "연결 실패"
    log_msg = f"[{timestamp}]: {ip}, {status}\n"
    if not connected:
        print(f"\033[91m[{timestamp}]: {ip}, {status}\033[0m")
        with open(error_log, "a", encoding="utf-8") as error_log_file:
            error_log_file.write(log_msg)
    else:
        print(f"[{timestamp}]: {ip}, {status}")


def main():
    error_log_file = "internet_error.log"
    local_ip = "192.168.0.1"
    wan_ip = "8.8.8.8"
    
    while True:        
        thread1 = threading.Thread(target=ping_async, args=(local_ip, error_log_file))
        thread2 = threading.Thread(target=ping_async, args=(wan_ip, error_log_file))
        
        thread1.start()
        thread2.start()
        
        time.sleep(0.5)

    time.sleep(3.5)


if __name__ == "__main__":
    main()
