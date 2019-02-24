from infi.systray import SysTrayIcon
import json
import os
import time
import socket
import urllib
import sys
from selenium import webdriver


def login_now(usernamea, passworda):
    driver = webdriver.Chrome()
    try:
        driver.get("https://172.22.2.6/connect/PortalMain")
        driver.implicitly_wait(10)

    except():
        sys.exit(0)
        print("Error logging in")
    username = driver.find_element_by_id("LoginUserPassword_auth_username")
    username.clear()
    password = driver.find_element_by_id("LoginUserPassword_auth_password")
    password.clear()
    username.send_keys(usernamea)
    password.send_keys(passworda)
    driver.find_element_by_id("UserCheck_Login_Button").click()
    print("Logged In.")
    time.sleep(2)
    driver.close()


def open_file(systray):
    os.system("config\cred.json")


def check_filed():
    config = json.loads(open('config/cred.json').read())
    if config['username'] != "ENTER USERNAME HERE":
        return True
    else:
        return False


def is_connected(hostname):
  try:
    host = socket.gethostbyname(hostname)
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False


def google_check():
    try:
        url = "https://www.google.com"
        urllib.urlopen(url)
        return True
    except:
        return False



# if(check_filed()):
#     menu_options = (("Enter Credentials", None, open_file),)
# else:
menu_options = (("Enter Credentials", None, open_file),)
systray = SysTrayIcon("icon.ico", "LNM Login Assistant", menu_options)
systray.start()

while True:
    config = json.loads(open('config/cred.json').read())
    print(config['username'] + "\n")
    print(str(google_check()) + "\n")
    print(str(is_connected("172.22.2.130")) + "\n")
    g_check = google_check()
    l_check = is_connected("172.22.2.130")
    c_check = check_filed()
    if l_check and g_check:
        time.sleep(10)
    elif l_check and c_check:
        login_now(config['username'], config['password'])
    else:
        time.sleep(1)