import time
import urllib.request
import urllib.parse
import json

data = {
    "client_id": "1606107874",
    "client_secret": "dc58406953c628e820ad3aedfa70a4cf",
    "grant_type": "authorization_code",
    "code": "d8f58cc8846992b79f504de0057837c3",
    "redirect_uri": "http://www.rikuki.cn:8000/hello"
    }
headers = {"Content-Type": "application/json"}
url = "https://api.weibo.com/oauth2/access_token"
data = urllib.parse.urlencode(data)
data = data.encode('utf-8')
id_request = urllib.request.Request(url)
id_response = urllib.request.urlopen(id_request)



# from selenium import webdriver
# import os
# html = "https://weibo.com/jp"
# # chrome_options = webdriver.ChromeOptions()
# # chrome_options.add_argument('--no-sandbox')
# # chrome_options.add_argument('--headless')
# # chrome_options.add_argument('--disable-gpu')
# # chrome_options.add_argument(
#     # "user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'")
# path = os.getcwd() + "/chromedriver"
# browser = webdriver.Chrome(executable_path=path)
# browser.get(html)
#
# try:
#     btn = browser.find_element_by_class_name("W_btn_a")
#     name = browser.find_element_by_id("loginname")
#     print(name.get_attribute("class"))
#     password = browser.find_element_by_name("password")
#     name.send_keys("17755610607")
#     password.send_keys("yymm0607")
#     btn.click()
#     print("login")
# except Exception:
#     print("error!")
#
# browser.close()
