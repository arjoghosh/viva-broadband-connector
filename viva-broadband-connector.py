# Author : Arjo Ghosh আর্য্য ঘোষ

import requests
a = requests.get('http://10.10.0.1/indexmain.php')
x=input("Enter username : ")
x=x.strip()
y=input("Enter password : ")
y=y.strip()
params = {'txtUserID': x, 'provider': 'smartguard', 'txtPassword':y, 'website_name':'',
          'MM_insert':'frmLogon', 'Submit':'Sign In'}
r = requests.post("http://10.10.0.1/make_me_login.php", data=params,cookies=a.cookies)
q=requests.get("http://10.10.0.1/signin.php?web_name=",cookies=a.cookies)
t=requests.get("http://10.10.0.1/clientmain.php",cookies=a.cookies)
if t.status_code==200:
    print('Your Internet connection is configured properly.')
else:
   print('Something went wrong. Please try again later.')
