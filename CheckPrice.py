from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from SendMail import sendmail

name = input("Please enter your Booking.com username:")
pwd = input("Please enter your Booking.com password: ")
to_mail = input("Please tell me your Email address: ")


driver = webdriver.Chrome('C:/Users/ybkh5/Desktop/chromedriver_win32/chromedriver.exe')
driver.get("https://www.booking.com/hotel/tw/caesar-park-banqiao.zh-tw.html?aid=304142;label=gen173nr-1FCAEoggJCAlhYSDNYBGjnAYgBAZgBMMIBCndpbmRvd3MgMTDIAQzYAQHoAQH4AQySAgF5qAID;sid=f4ec5e720c86465fb50309c853d5c2ac&checkin=2018-11-01&checkout=2018-11-02")
driver.find_element_by_id('current_account').click()
username = driver.find_element_by_name('username')
username.send_keys(name)

password = driver.find_element_by_name('password')
password.send_keys(pwd)
password.send_keys(Keys.ENTER)

driver.refresh()
hotel_name = driver.find_element_by_class_name('hp__hotel-name')
hotel_name = hotel_name.text
price = driver.find_element_by_xpath('//*[@id="hprt-form"]/table/tbody/tr[3]/td[2]/div/div[2]/span')
price = price.text
print("The Price of "+ hotel_name + " is: " + price)

sendmail(to_mail,hotel_name,price)
driver.quit()
