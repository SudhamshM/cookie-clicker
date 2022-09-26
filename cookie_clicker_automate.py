from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import os

browser = webdriver.Edge('path\\to\\msedgedriver.exe')
browser.get('https://orteil.dashnet.org/cookieclicker')
browser.maximize_window()
WebDriverWait(browser, 3)
sleep(5)
try:
    # selecting english language pop-up
    browser.find_element_by_xpath('//*[@id="langSelect-EN"]').click()
    sleep(3)
    # clicking "got it" for accepting cookies
    browser.find_element_by_xpath('/html/body/div[1]/div/a[1]').click()
except Exception:
    print("error, quitting...")
    browser.quit()
    os.system('cmd /k "taskkill /f /im msedgedriver.exe')
cookie_area = browser.find_element_by_id("bigCookie")
for number in range(150):
    cookie_count_area = str(browser.find_element_by_id('cookies').text)
    cookie_count = cookie_count_area.rsplit(" ")
    print(str(cookie_count[0]) + " cookies per second")
    buy_area_1 = browser.find_element_by_id('productPrice0')
    cursor_count = browser.find_element_by_id('productPrice0')
    buy_area_2 = browser.find_element_by_id('productPrice1')
    # baker_count = browser.find_element_by_id('productPrice1')
    if int(cookie_count[0]) >= int(buy_area_2.text):
        # if int(baker_count.text) > int(cursor_count.text):
        #     cookie_area.click()
        # else:
        browser.find_element_by_id('product1').click()
        cookie_area.click()
        cookie_area.click()
        cookie_area.click()
        print("The current cookie count here is", cookie_count[0])
    # elif int(cookie_count[0]) == int(buy_area_1.text):
    #     if int(cursor_count.text) > int(baker_count.text):
    #         cookie_area.click()
    #     else:
    #         buy_area_1.click()
    #     print("The current cookie count is", cookie_count[0])
    else:
        cookie_area.click()
        cookie_area.click()
        cookie_area.click()
        cookie_area.click()
# cookie_count_2 = browser.find_element_by_id('cookieGenerated').text
# print("The current cookie count is", cookie_count_2)

    
browser.quit()
os.system('cmd /k "taskkill /f /im msedgedriver.exe"')

