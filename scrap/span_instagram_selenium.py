from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time, urllib.request
from lib2to3.pgen2 import driver
from selenium.webdriver.support import expected_conditions as EC
import requests
from selenium.webdriver.chrome.options import Options
from lib2to3.pgen2 import driver
import csv
import random




options = Options()
options.add_argument("--incognito")  # incognito
driver = webdriver.Chrome()
driver = webdriver.Chrome(options=options)
driver.get("https://www.instagram.com/")

time.sleep(random.randint(15,30))

# driver.find_element(By.LINK_TEXT,'Allow all cookies').click()
#
# time.sleep(10)
#login
time.sleep(random.randint(20,35))
username = driver.find_element(By.CSS_SELECTOR,"input[name='username']")
password = driver.find_element(By.CSS_SELECTOR,"input[name='password']")
username.clear()
password.clear()
username.send_keys("username")
password.send_keys("password")
login = driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()


# <button class="_a9-- _ap36 _a9_0" tabindex="0">Allow all cookies</button>

#save your login info?
# time.sleep(10)
# notnow = driver.find_element(By.XPATH,"//button[contains(text(), 'Not Now')]").click()
# #turn on notif
# time.sleep(10)
# notnow2 = driver.find_element(By.XPATH,"//button[contains(text(), 'Not Now')]").click()

#searchbox


time.sleep(random.randint(12,40))
# class="x9f619 xxk0z11 xii2z7h x11xpdln x19c4wfv xvy4d1p"

# notnow2 = driver.find_element(By.CLASS_NAME,"x9f619 x3nfvp2 x1lq5wgf xgqcy7u x30kzoy x9jhf4c xr9ek0c xjpr12u xo237n4 x6pnmvc x7nr27j x12dmmrz x80pfx3 x159b3zp xl4qmuc xxqof28 xd18jyu xiuebna x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x178xt8z xm81vs4 xso031l xy80clv xzi3mdb x1w2lkzu xxbrewl xlu9dua").click()

driver.get("https://www.instagram.com/reel/C_s_aZ0PxBv/")


time.sleep(random.randint(12,40))
# class="x9f619 xxk0z11 xii2z7h x11xpdln x19c4wfv xvy4d1p"

# notnow2 = driver.find_element(By.CLASS_NAME,"x9f619 x3nfvp2 x1lq5wgf xgqcy7u x30kzoy x9jhf4c xr9ek0c xjpr12u xo237n4 x6pnmvc x7nr27j x12dmmrz x80pfx3 x159b3zp xl4qmuc xxqof28 xd18jyu xiuebna x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x178xt8z xm81vs4 xso031l xy80clv xzi3mdb x1w2lkzu xxbrewl xlu9dua").click()

driver.get("https://www.instagram.com/bonyadfarhangzendegi/")

time.sleep(random.randint(13,34))
#

driver.get("https://www.instagram.com/reel/DBMmOncoi52/")
time.sleep(random.randint(19,45))
# driver.get("https://www.instagram.com/reel/C-boRrNvs4B/?utm_source=ig_web_copy_link")

driver.execute_script("document.body.style.overflow = 'hidden';")

# پیدا کردن بخش اسکرول با استفاده از کلاس‌های CSS
# comment_section = driver.find_element(By.CSS_SELECTOR, "div.x5yr21d.xw2csxc.xlodjw0f.xln2onr6")

comment_section = driver.find_element(By.XPATH, "//div[contains(@class, 'x5yr21d') and contains(@class, 'xw2csxc')]")

time.sleep(random.randint(19,30))
# اسکرول در بخش کامنت‌ها
for _ in range(3):  # تعداد دفعات اسکرول
    driver.execute_script("arguments[0].scrollTop   = arguments[0].scrollHeight", comment_section)
    time.sleep(random.randint(15,30))  # صبر برای بارگذاری کامنت‌های جدید

# پیدا کردن کامنت‌ها با استفاده از کلاس دقیق
captien = driver.find_elements(By.XPATH, "//span[contains(@class, 'x193iq5w') and contains(@class, 'x1fj9vlw') and contains(@class, 'x1vvkbs')]")  # انتخاب کامنت‌ها با کلاس دقیق

comments = driver.find_elements(By.XPATH, "//span[contains(@class, 'x1lliihq') and contains(@class, 'x1plvlek') and contains(@class, 'x1plvlek')]")  # انتخاب کامنت‌ها با کلاس دقیق
commenter = driver.find_elements(By.XPATH, "//span[contains(@class, '_ap3a _aaco _aacw _aacx _aad7 _aade') ]")  # انتخاب  comenter با کلاس دقیق
like = driver.find_elements(By.XPATH, "//span[contains(@class, 'x193iq5w')and contains(@class, 'x1fj9vlw')and contains(@class, 'x13faqbe')]")  # انتخاب  comenter با کلاس دقیق
Time = driver.find_elements(By.XPATH, "//span[contains(@class, 'x1p4m5qa')]")  # انتخاب  comenter با کلاس دقیق

print(comments)
print(100*'*')
print(commenter)
print(100*'*')

print(captien)
print(100*'*')

print(like)
print(100*'*')

print(Time)
time.sleep(random.randint(19,30))
for index, captiens  in enumerate(captien):
    text = captiens.text  # متن کامنت
    print(text)

time.sleep(random.randint(19,30))
for index, comment in enumerate(comments):
    text = comment.text  # متن کامنت
    print(text)

time.sleep(random.randint(19, 30))
for index, commenters in enumerate(commenter):
    text = commenters.text  # متن کامنت
    print(text)

time.sleep(random.randint(19, 30))
for index,  likes in enumerate(like):
    text = likes.text  # متن کامنت
    print(text)

time.sleep(random.randint(19, 30))
for index, Times in enumerate(Time):
    text = Times.text  # متن کامنت
    print(text)

time.sleep(random.randint(19,30))
# print(comments.text)

# with open('comment s.csv', mode='w', newline='', encoding='utf-8-sig') as file:
#     writer = csv.writer(file)
#     writer.writerow(["کامنت"])  # نوشتن عنوان ستون
#
#     for index, comment in enumerate(comments):
#         text = comment.get_attribute()  # متن کامنت
#         print(text)
#         writer.writerow([text])  # نوشتن هر کامنت در فایل CSV
#
# print("کامنت‌ها در فایل 'comments.csv' ذخیره شدند.")

driver.quit()









# end_of_scroll = driver.execute_script("return document.body.scrollHeight")
# while True:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(5)
#     my_scroll = driver.execute_script("return document.body.scrollHeight")
#     if my_scroll == end_of_scroll:
#         break
#     end_of_scroll = my_scroll


# searchbox = driver.find_element(By.LINK_TEXT,"input[placeholder='Search']")
# searchbox.clear()
# searchbox.send_keys("bonyadfarhangzendegi")
# time.sleep(5)
# searchbox.send_keys(Keys.ENTER)
# time.sleep(5)
# searchbox.send_keys(Keys.ENTER)


#
# time.sleep(20)
#
# #scroll
# scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
# match=False
# while(match==False):
#     last_count = scrolldown
#     time.sleep(3)
#     scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
#     if last_count==scrolldown:
#         match=True
#
# #posts
# posts = []
# links = driver.find_elements(By.TAG_NAME,'a')
# for link in links:
#     post = link.get_attribute('href')
#     if '/p/' in post:
#       posts.append(post)
#
# print(posts)
#
#
# #get videos and images
# download_url = ''
# for post in posts:
#  driver.get(post)
#  shortcode = driver.current_url.split("/")[-2]
#  time.sleep(7)
#  if driver.find_element_by_css_selector("img[style='object-fit: cover;']") is not None:
#   download_url = driver.find_element_by_css_selector("img[style='object-fit: cover;']").get_attribute('src')
#   urllib.request.urlretrieve( download_url, '{}.jpg'.format(shortcode))
#  else:
#   download_url = driver.find_element_by_css_selector("video[type='video/mp4']").get_attribute('src')
#   urllib.request.urlretrieve( download_url, '{}.mp4'.format(shortcode))
#  time.sleep(5)
