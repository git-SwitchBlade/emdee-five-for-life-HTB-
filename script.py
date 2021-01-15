#!/usr/bin/env python3
#This script is for scriptkiddies
#Use this script in HTB challenge hackthebox(emdee five for life) to get the flag


#Modules
import re
import requests as r
from bs4 import BeautifulSoup 
import hashlib
import time
import os

#BANNER
print("""
 ____  __  __  ____  ____  ____    ____  ____  _  _  ____    ____  _____  ____    __    ____  ____  ____ 
( ___)(  \/  )(  _ \( ___)( ___)  ( ___)(_  _)( \/ )( ___)  ( ___)(  _  )(  _ \  (  )  (_  _)( ___)( ___)
 )__)  )    (  )(_) ))__)  )__)    )__)  _)(_  \  /  )__)    )__)  )(_)(  )   /   )(__  _)(_  )__)  )__) 
(____)(_/\/\_)(____/(____)(____)  (__)  (____)  \/  (____)  (__)  (_____)(_)\_)  (____)(____)(__)  (____)

""")

print('[!] Run: ./script.py')
print('[!] This will likely fail do please re run the script!...')
time.sleep(3)
url = input('URL: ')
r = r.session()
get = r.get(url)

soup = BeautifulSoup(get.text, 'lxml')
MD5 = soup.h3.text

res = hashlib.md5(MD5.encode()).hexdigest()
data = dict(hash=res)

result = r.post(url, data=data)

if 'HTB' in result.text: 
    print('[+] Found!')
    time.sleep(5)
    print(result.text)
else:
    print('[!] Please run again the script')
    exit()