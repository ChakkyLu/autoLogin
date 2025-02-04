#coding=UTF-8
import datetime

from selenium import webdriver
import os
import time


#------------自动登录函数------------------
def autologin(data):
    flower = 0
    html = "http://passport.66rpg.com/user/login.shtml?fromurl=http%3A%2F%2Fwww.66rpg.com%2Findex&auth_callback=%2F%2Fwww.66rpg.com%2Fsso%2Fauth_callback&app=www&sign=1a217af78f0cceb2464cb9e378c7ede5&login_type=0"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("user-agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'")
    browser = webdriver.Chrome(chrome_options=chrome_options,executable_path=os.getcwd()+"/chromedriver")
    browser.get(html)
    try:
        username = browser.find_element_by_id("username")
        pswd = browser.find_element_by_id("password")
        username.send_keys(data['username'])
        pswd.send_keys(data['password'])
        login_btn = browser.find_element_by_class_name("login_btn")
        login_btn.click()
        print("autoLogin ok")
    except Exception:
        time.sleep(2)
        print("cannot login")
        return flower

    time.sleep(0.5)

    try:
        home_url = browser.find_element_by_xpath("//div[@class='user_pics']/a").get_attribute('href')
        js = 'window.open("'+str(home_url)+'");'
        browser.execute_script(js)
        browser.switch_to_window(browser.window_handles[1])
        flower = browser.find_element_by_xpath("//dl/dd[6]/span[2]/span[1]")
        flower = int(flower.text)
    except Exception:
        print("cannot aceess mypage")
    browser.quit()
    return flower



def main(h, m, initial_flower, data):
    b = 1
    while True:
        while True:
            now = datetime.datetime.now()
            if now.hour == h and now.minute == m and b:
                flower = autologin(data)
                while flower - initial_flower != 3:
                    flower = autologin(data)
                print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), data['username'],"鲜花有 "+str(flower)+" 朵")
                initial_flower += 3
                b = 0
            if now.hour ==h and now.minute == m+2:
                b = 1;
                break


if __name__ == "__main__":

#--------------data---------------
    # username: 填写你自己的username
    # password：填写你的密码
    # initial_flower: 你的初始鲜花
#---------------------------------
    data = {
        'username': "USERNAME",
        'password': "PASSWORD"
    }

    initial_flower = 24
    flower = autologin(data)
    print(data['username'], "鲜花有 " + str(flower) + " 朵")

