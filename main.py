import requests
import time
import concurrent.futures
import sys
import socket

#This tool is for simple port scanning
Target_url = sys.argv[1]

#For final result
result = " "

#Ls of ports
common_ports = [
    # common in Internet
    21,    # FTP (File Transfer Protocol)
    22,    # SSH (Secure Shell)
    23,    # Telnet
    25,    # SMTP (Simple Mail Transfer Protocol)
    53,    # DNS (Domain Name System)
    80,    # HTTP 
    110,   # POP3 (Email)
    123,   # NTP (Network Time Protocol)
    143,   # IMAP (Email)
    161,   # SNMP (Simple Network Management Protocol)
    443,   # HTTPS (SSL/TLS)
    465,   # SMTPS (SMTP )
    587,   # SMTP (send email)
    993,   # IMAPS (IMAP )
    995,   # POP3S (POP3 )

    #DB
    3306,  # MySQL Database
    5432,  # PostgreSQL
    6379,  # Redis
    27017, # MongoDB
    3389,  # RDP (Remote Desktop Protocol)
    5900,  # VNC (Virtual Network Computing)

    # common port in pentest / bug bounty
    139,   # NetBIOS (Windows file sharing)
    445,   # SMB (Server Message Block)
    2049,  # NFS (Network File System)
    5985,  # WinRM (Windows Remote Management)
    8080,  # Alternative HTTP
    8443,  # HTTPS alternative
    8888   # Web proxy / Dev services
]

open_ports = []


#Loop for every ports
#for x in common_ports:
def scan_port(port):
        #set up socket here
        debug = f"{Target_url}:{port}"
        print('scanning at:', debug)
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(5)
        URL = sock.connect_ex((Target_url,port))
        sock.close()
        if URL == 0:
            open_ports.append(port)
            #result += str(port) + ", "
            print('This website port is work bri: ', debug)
        

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=600) as executor:
            executor.map(scan_port, range(1,65535))

    if open_ports:
        print("\n Open Ports:", ", ".join(map(str, open_ports)))

    #print("These ports are work:" ,result)
    print("FInish Scanning!!!!")

if __name__ == "__main__":
      start_time = time.time()
      main()
      print("Time", (time.time() - start_time), " seconds")