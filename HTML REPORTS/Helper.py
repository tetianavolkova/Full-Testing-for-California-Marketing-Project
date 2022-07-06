import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException as WDE

# main_url
main_url = "https://qasvus.wixsite.com/ca-marketing"

# main_email
main_email = "mailto:qasv.us@gmail.com.com"


def delay():
    time.sleep(random.randint(1, 10))