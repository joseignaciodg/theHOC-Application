from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains

import datetime
import time
import signal

# Code will stop executing after 720 seconds == 10 mins.
signal.alarm(720)

#  Code to allow access for Microphone, Camera and notifications
# 0 is disable and 1 is allow.
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument('--no-sandbox')
opt.add_argument("--headless")
opt.add_argument("--disable-dev-shm-usage")

# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1, 
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 0, 
"profile.default_content_setting_values.notifications": 0
})

#time conditions
now = datetime.datetime.now()
current_time = now.strftime("%H:%M / %A")
justtime = now.strftime("%H:%M")
print (current_time)
    
# directing to the link to be visited; The program first logs into gmail for all around access of google services.
def gmail_login():

    # Opening Jitsi Meet:
    driver.get(sub)

    driver.find_element_by_class_name('field ').send_keys('HOC')

    driver.find_element_by_class_name('prejoin-preview-dropdown-container').click()

# ----------- EJECUCION DEL CODIGO ----------

sub = "https://meet.jit.si/therealhocaui_userconnected_20303031"

print ('ANTES')

driver = webdriver.Chrome(options=opt, executable_path=r'chromedriver') 

gmail_login()    

print ('DESPUES')
