#!/usr/bin/python3

import os
import subprocess
import requests
import datetime
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROME_BIN = "/usr/bin/chromium"
CHROME_DRIVER = os.path.expanduser("/usr/bin/chromedriver")

options = Options()
options.binary_location = CHROME_BIN
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--test-type')
options.add_argument('--headless')
options.add_argument('--window-size=1280,3000')

driver = webdriver.Chrome(CHROME_DRIVER, options=options)
driver.get(os.environ["URL_FIRST"])

driver.find_element_by_link_text(os.environ["LINK_TEXT"]).click();

driver.find_element_by_class_name(os.environ["BUTTON_CLASS"]).click();

driver.save_screenshot("/usr/src/ss.png")

driver.quit()

time.sleep(20)

files = {'file': open("/usr/src/ss.png", 'rb')}

param = {
    'token': os.environ["SLACK_TOKEN"], 
    'channels': "#hai",
    'filename': "screenshot",
    'initial_comment': datetime.date.today(),
    'title': "hai"
}

requests.post(url="https://slack.com/api/files.upload",params=param, files=files)

os.remove("/usr/src/ss.png")