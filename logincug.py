#coding:utf-8

from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import sys
sys.path.append("/Library/Python/2.7/site-packages/pytesser")
import pytesser

driver = webdriver.Chrome()
driver.get("https://portal.cug.edu.cn/zfca/login?service=http%3A%2F%2Fportal.cug.edu.cn%2Fportal.do")

# i = 0
# while 1:
#     i = i+1
#     try:
elem_user = driver.find_element_by_name("username")
elem_pwd = driver.find_element_by_name("password")
elem_captcha = driver.find_element_by_name("j_captcha_response")
driver.get_screenshot_as_file('captcha.jpg')

rangle=(1669,494,1807,541) #写成我们需要截取的位置坐标
i = Image.open("/Users/wangmian/PycharmProjects/selenium/captcha.jpg") #打开截图
realcaptcha = i.crop(rangle)  #使用Image的crop函数，从截图中再次截取我们需要的区域
realcaptcha.save("/Users/wangmian/PycharmProjects/selenium/realcaptcha.png")
code = pytesser.image_file_to_string('/Users/wangmian/PycharmProjects/selenium/realcaptcha.png')

#
#
#
elem_user.send_keys("20141001146")
elem_pwd.send_keys("******")
time.sleep(0.5)
elem_captcha.send_keys(code)

elem_pwd.send_keys(Keys.RETURN)
time.sleep(5)
driver.close()
driver.quit()

