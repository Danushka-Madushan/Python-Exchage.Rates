from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import urllib.request
import msvcrt as stop
from sys import exit
import time
import sys
import os

cmd_request_1 = 'mode 70,10'
cmd_request_2 = 'color 2'
os.system(cmd_request_1)
os.system(cmd_request_2)

def print_s(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def print_f(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0)
    
def Connect(host='https://www.google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

if Connect():
    print_s(">> Connected!..\n>> Proseeding...")
    os.system("cls")
else:
    print_s(">> Connection Faild!..\n>> Please Check Your Connection & Try Again..\n>> Client Exiting...")
    exit()

url= Request("https://www.investing.com/currencies/usd-lkr", headers={'User-Agent': 'Mozilla/5.0'})
data = urlopen(url).read()
print(">> Running...")
soup = BeautifulSoup(data, features = "html5lib")
print_s(">> Done!\n\n")
t=soup.find('span',{'class':'arial_26 inlineblock pid-2151-last'})
print_f(">> (USD) Price : "),print_s(t.text + " (LKR)")
print("\n")
print_s(">>Press Anything For Exit!")
stop.getch()
