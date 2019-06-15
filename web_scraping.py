import selenium.webdriver as webdriver
import time
from bs4 import BeautifulSoup
import re

#Веб-скраппинг. В данном модуле реализованы функции добычи данных без применения API методов, а через анализ HTML страницы
#Функции по тегам цепляются за данные и достают их. Аналог сбора данных в сети, если нет возможности воспользоваться API. Работает через Selenium,
#Bs4 и firefox webdriver

def ScrollAllPage():            #пролистывает страницу вниз
    SCROLL_PAUSE_TIME = 0.5
    last_height = browser.execute_script("return document.body.scrollHeight")
    while True:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

def LoginVK(log1, pass1):    #авторизация вк
    html = "https://vk.com/"
    browser.get(html)
    login = browser.find_element_by_id('index_email')
    login.send_keys(str(log1))
    passw = browser.find_element_by_id('index_pass')
    passw.send_keys(str(pass1))
    browser.find_element_by_id('index_login_button').click()
    time.sleep(5)

def GetFriends(id):      #получить данные о друзьях пользователя
    browser.get("https://vk.com/friends?id=" + str(id) + "&section=all")
    ScrollAllPage()
    bsObj = BeautifulSoup(browser.page_source, "lxml")
    nameList = bsObj.findAll("div", {"class": "friends_field friends_field_title"})
    idList = bsObj.findAll("div", {"id": re.compile("friends_user_row[0-9]*")})
    fio = []
    id = []
    for i in idList:
        s = i["id"]
        s = s[16: len(s)]
        id.append(s)
    for i in nameList:
        fio.append(i.get_text())
    return (fio, id)

def GetMembers(id):                #получить данные о подписчиках пользователя
    browser.get("https://vk.com/search?c[section]=people&c[group]="+str(id))
    ScrollAllPage()
    bsObj = BeautifulSoup(browser.page_source, "lxml")
    nameList = bsObj.findAll("div", {"class": "labeled name"})
    idList = bsObj.findAll("button", {"id": re.compile("search_sub[0-9]*")})
    fio = []
    id = []
    for i in idList:
        s = i["id"]
        s = s[10: len(s)]
        id.append(s)
    for i in nameList:
        fio.append(i.get_text())
    return (fio, id)

def OpenFirefox(log1, pass1):             #открытие браузера, обычно делается в скрытом режиме, но в данном случае для теста браузер не скрыт
    global browser
    browser = webdriver.Firefox()
    LoginVK(log1, pass1)