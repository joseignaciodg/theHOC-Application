from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType

import datetime
import time
import signal

# Code will stop executing after 720 seconds == 10 mins.
signal.alarm(720)

now = datetime.datetime.now()
current_time = now.strftime("%H:%M / %A")
 # %A is to get the name of the Day!
justtime = now.strftime("%H:%M")

#  Code to allow access for Microphone, Camera and notifications
# 0 is disable and 1 is allow.
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument('--no-sandbox')
opt.add_argument('--headless')

#opt.add_argument('window-size=1920x1080');

# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1,
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 1,
"profile.default_content_setting_values.notifications": 1
})

#time conditions
now = datetime.datetime.now()
current_time = now.strftime("%H:%M / %A")
justtime = now.strftime("%H:%M")
print (current_time)

# directing to the link to be visited; The program first logs into gmail for al>
def gmail_login():
    print ("A")
    driver.get("https://accounts.google.com/ServiceLogin?service=mail&passive=t>
    print ("B")
    driver.find_element_by_id("Email").send_keys("therealhocaui@gmail.com")
    print ("C")
    # Next Button:
    driver.find_element_by_id("next").click()
    print ("D")
    # Password:
    password = "MILAN20212022"
    paswd = driver.find_element_by_id("password")
        print ("E")
    paswd.send_keys(password)
    print ("F")
    # Next button:
    #driver.find_element_by_id("identifierNext").click()
    #driver.find_element_by_name("passwordNext").click()
    #driver.find_element_by_link_text('Next')
    paswd.send_keys(Keys.ENTER)
    print ("G")
    # Opening Meet:
    driver.get(sub)
    print ("H")
    #driver.refresh()
    print ("I")

    # Turning off video
    #driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[9]/div[3>
    print ("J")


    # Join class
    #driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3>
    #driver.find_element_by_id("Join").click()
    #driver.find_element_by_xpath("//*[@id= 'yDmH0d']/c-wiz/div/div/div[9]/div[>
    #driver.find_element_by_xpath("//button[text()='Ask to join']").click()
    #driver.find_element_by_css_selector('uArJ5e UQuaGc Y5sE8d uyXBBb xKiqt M9B>
    #driver.find_element_by_id("").click()
    #driver.find_element_by_xpath('//button[normalize-space()="Join Meeting"]')
    #driver.find_element_by_css_selector('div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt>
    driver.find_element_by_xpath("//span[contains(text(), 'join')]").click()
    print("K")


#sub is the class id with the meet link. sub changes with the time accoriding t>
#sub = "https://meet.google.com/ztd-efbb-jup"
sub = "https://meet.google.com/hit-vusv-wcf"

driver = webdriver.Chrome(options=opt, executable_path=r'../../../usr/bin/chrom>

print ("ANTES")

gmail_login()

print ("DESPUES")



