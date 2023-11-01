# Created by th7 2023/11/01
import socket
import requests
import base64

username = ""
pwd = ""

password = base64.b64decode(pwd).decode('ascii')

try:
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect(('8.8.8.8',80))
    ip = s.getsockname()[0]
except:
    print("无法获取局域网ip 请检查网络设置")
    exit(1)
finally:
    s.close()

login_url = "http://218.195.105.234:801/eportal/portal/login?callback=dr1004&login_method=1&user_account=,0,"+username+"&user_password="+password+"&wlan_user_ip="+ip+"&wlan_user_ipv6=&wlan_user_mac=000000000000&wlan_ac_ip=&wlan_ac_name=&jsVersion=4.1.3&terminal_type=1&lang=zh-cn&lang=zh&v=9797"

try:
    req = requests.get(url=login_url,timeout=3.0).text
except requests.ReadTimeout:
    print("连接超时 请检查代理设置")
    exit(1)

if("认证成功" in req or "已经在线" in req):
    print("认证成功 当前局域网IP: "+ip)
else:
    print("认证失败")