import os
import time
import sys
# ------------------------------------------------
try:
    import requests as req
except:
    os.system('pip install requests')
#--------------------------------------------
try:
    from colorama import Fore, init
except:
    os.system('pip install colorama')
#--------------------------------------------
try:
    from colored import fg, bg, attr
except:
    os.system('pip install colored')
#--------------------------------------------
os.system('clear')
init(autoreset=True)
class color:
    red = '\033[31m'
    green = '\033[32m'
    blue = '\033[36m'
    pink = '\033[35m'
    orang = '\033[34m'         
    white = '\033[00m'
def logo():
    print(f''' 
    {Fore.RED} 
    ========================={Fore.GREEN} S A N ========================={Fore.YELLOW}
                          _         __ _         _         
                  ____  _| |__ ___ / _(_)_ _  __| |___ _ _ 
                (_-< || | '_ \___|  _| | ' \/ _` / -_) '_|
                /__/\_,_|_.__/   |_| |_|_||_\__,_\___|_|  
                                           
    {Fore.RED}
    ========================={Fore.GREEN} S A N =========================
{Fore.RED}''')


logo()





print(Fore.WHITE+'['+Fore.RED+'#'+Fore.WHITE+'] Enter target url ex: www.google.com or google.com')

target_url = input('TARGET [URL] '+Fore.RED+'>_'+Fore.GREEN+' ')

print(Fore.RESET+'')

if len(target_url) < 5:
    print('['+Fore.RED+'!'+Fore.WHITE+']'+Fore.YELLOW+' target in very short ! check and try again')
    time.sleep(3.0)
    sys.exit()
else:
    pass

if 'http://' or 'https://' in target_url:
    pass


if 'http://' or 'https://' not in target_url:
    target_url = 'http://'+target_url


test = req.get(target_url)

time.sleep(5)

if test.status_code == 200:
    pass

else:
    print(Fore.RED+'cant connect to target '+Fore.WHITE+'> '+Fore.YELLOW+''+target_url)
    sys.exit()




print('['+Fore.GREEN+'*'+Fore.WHITE+'] TARGET >>> '+Fore.GREEN+''+target_url)

links = open('link.txt', 'r').read().split()

for link in links:
    try:
        url = (target_url+'/'+link)
        get_req = req.get(url, timeout=5)
    except KeyboardInterrupt:
        print('Bye !')
        time.sleep(3)
        sys.exit()
    #get_req.status_code = int(get_req.status_code)

    sisad = 399
    charsad = 400
    charnono = 499

    try:
        if get_req.status_code < sisad:
            print('['+Fore.GREEN+'OK'+Fore.WHITE+'] founded a page - URL > %s%s {} %s'.format(url) % (fg('black'), bg('green'), attr('reset')))

        if get_req.status_code > charsad:
            print('['+Fore.RED+'NOT'+Fore.WHITE+'] cant found page - URL > %s%s {} %s'.format(url) % (fg('black'), bg('red'), attr('reset')))
    
        if get_req.status_code > charnono:
            print('['+Fore.YELLOW+'Server-ERROR'+Fore.WHITE+'] SERVER ERROR - URL > %s%s {} %s'.format(url) % (fg('white'), bg('yellow'), attr('reset')))
    
    except KeyboardInterrupt:
        print('Bye !')
        time.sleep(3)
        sys.exit()
