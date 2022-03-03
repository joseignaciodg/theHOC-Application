from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains

from pyvirtualdisplay import Display

import time

display = Display(visible=0, size=(800, 600))
display.start()

#  Code to allow access for Microphone, Camera and notifications
# 0 is disable and 1 is allow.
opt = Options()

#opt.add_argument('--headless')
opt.add_argument('--no-sandbox')
opt.add_argument('--disable-dev-shm-usage')

#opt.add_argument("--disable-infobars")
#opt.add_argument("--start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument('--remote-debugging-port=9222')
opt.add_argument("--disable-gpu")

opt.add_experimental_option("detach", True)

#global driver

# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1, 
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 0, 
"profile.default_content_setting_values.notifications": 0
})

#EJECUCION DEL CODIGO

link = "https://workshopx.app/r/therealhocaui_pepito_234576"

print ('ANTES')
driver = webdriver.Chrome(options=opt, executable_path=r'/usr/bin/chromedriver')

driver.get(link)
driver.implicitly_wait(30000)

print ('DESPUES')
