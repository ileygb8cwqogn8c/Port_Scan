import threading
import socket
from colorama import Fore, Back, Style, init
banner = rf'''{Fore.GREEN}
  _____           _    _____                 
 |  __ \         | |  / ____|                
 | |__) |__  _ __| |_| (___   ___ __ _ _ __  
 |  ___/ _ \| '__| __|\___ \ / __/ _` | '_ \ 
 | |  | (_) | |  | |_ ____) | (_| (_| | | | |
 |_|   \___/|_|   \__|_____/ \___\__,_|_| |_|
                               codedBy: foxeditor  
''' 
print(banner)                                        
init()
print(rf"{Fore.RED}Enter IP:")
ip = input()

def portscan(port): 

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)

    try:
    	conn = s.connect((ip, port))
    	print(rf"{Fore.GREEN}Port: {port} is open")
    	conn.close()
    except:
    	pass
ports = [20, 21, 22, 23, 25, 38, 43, 80, 109, 110, 115, 118, 119, 143,
194, 220, 443, 445, 540, 585, 591, 1112, 1433, 1443, 3128, 3197, 3306, 3389, 4000, 
4333, 5100, 5432, 6669, 8000, 8080, 8443, 9014, 9200]

for port in ports:
    t = threading.Thread(target=portscan, kwargs={'port': port}).start()
    
