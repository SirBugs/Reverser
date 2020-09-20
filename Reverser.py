#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Coded By SirBugs
#Don't Change copyright Mother Fucker
#Egyptian Coderz

import os
import time
import random
import requests
import colorama
from colorama import Fore
from colorama import init
init(autoreset=True)
from multiprocessing.pool import ThreadPool

YELLOW = Fore.YELLOW
RED    = Fore.RED
GREEN  = Fore.GREEN

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

print YELLOW + "\t  ____                                   "; time.sleep(0.1)
print YELLOW + "\t |  _ \ _____   _____ _ __ ___  ___ _ __ "; time.sleep(0.1)
print YELLOW + "\t | |_) / _ \ \ / / _ \ '__/ __|/ _ \ '__|"; time.sleep(0.1)
print YELLOW + "\t |  _ <  __/\ V /  __/ |  \__ \  __/ |   "; time.sleep(0.1)
print YELLOW + "\t |_| \_\___| \_/ \___|_|  |___/\___|_|   "; time.sleep(0.1)
print YELLOW + "\t {}@{}Facebook: {}fb/SirBugs".format(RED, YELLOW, RED); time.sleep(0.1)
print YELLOW + "\t\t {}@{}Telegram: {}SirBugs".format(RED, YELLOW, RED); time.sleep(0.1)
print YELLOW + "\t\t\t {}@{}ICQ: {}SirBugs\n".format(RED, YELLOW, RED); time.sleep(0.1)
print YELLOW + '\t ============================================================='; time.sleep(0.1)
print YELLOW + '\t =============================================================\n'

GRAPPED = 0

def REV(domain):

    global GRAPPED
    
    session = requests.Session()
    
    headers = {
        "Accept": "text/html, /; q=0.01",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://hackertarget.com",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://hackertarget.com/reverse-ip-lookup/",
        "Cookie": "_ga=GA1.2.552357818.1600531649; _gid=GA1.2.938729293.1600531649; _gat=1",
    }

    data = 'theinput={}&thetest=reverseiplookup&name_of_nonce_field=9b87730135&_wp_http_referer=%2Freverse-ip-lookup%2F'.format(domain)

    while 1:

        proxy = random.choice(proxies)
        session.proxies = {
            "http":"socks4://%s" % proxy,
            'https':"socks4://%s" % proxy,
        }

        try:
            r    = session.post('https://hackertarget.com/reverse-ip-lookup/', headers=headers, data=data, timeout=3)
        except:
            pass
        else:
            src  = r.content
            # // print(src)
            Grapped = 0
            try:
                Reversed = src.split('<pre id="formResponse">')[1].split('</pre>')[0].lower()
                file = open('Grapped.txt', 'a+')
                file.write(Reversed+'\n')
                file.close()
                # // print(Reversed)
                for site in Reversed.split('\n'):
                    Grapped+=1
                if Grapped == 0:
                    pass
                else:
                    GRAPPED+=Grapped
                    print '\t {}--| Totally Grapped --> [{}{}{}] [{}{}{}]'.format(YELLOW, RED, domain, YELLOW, RED, Grapped, YELLOW)
                    os.system("title "+ "[+] Bugs Reverser - Grapped: {}".format(GRAPPED))
                    Grapped = 0
                    break
            except:
                pass

Sites = raw_input('\t {}--| {}Enter Your Sites List : '.format(YELLOW, RED))
proxies_path = raw_input('\t {}--| {}Enter Your Proxies List : '.format(YELLOW, RED))
proxies = open(proxies_path, 'r').read().split('\n')
print YELLOW + '\n\t =============================================================\n'

# // REV('')

try:
    if __name__ == '__main__':
        Coupons = open(Sites, 'r').read().split('\n')
        pool = ThreadPool(20)
        for _ in pool.imap_unordered(REV, Coupons):
            pass
except:
    pass
