import unittest

from faker import Faker
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.relative_locator import locate_with
import Helper as H
import HtmlTestRunner

fake = Faker()


class Chrome_tests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # check Home link clickability on the top of the screen
    def test_home_link(self):
        driver = self.driver
        driver.get(H.main_url)
        driver.maximize_window()
        wait = WebDriverWait(driver, 20)

        # click 'Home' link
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='_1zyfI'][contains(.,'Home')]"))).click()
        WebDriverWait(driver, 3)

        # assert 'Home' title
        self.assertIn('Home', driver.title)
        print("Page has", driver.title + " as Page title")

        H.delay()

        # check specific element on the page
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "// span[contains(., 'LET CALIFORNIA MARKETING "
                                                             "GROW YOUR BUSINECS')]")))
            print("The Home page is present")
        except TimeoutException:
            print("Loading took too much time!")

        # back in the browser
        driver.back()

    def tearDown(self):
        self.driver.quit()

    # check Blog link clickability on the top of the screen
    def test_blogworking_link(self):
        driver = self.driver
        driver.get(H.main_url)
        driver.maximize_window()
        wait = WebDriverWait(driver, 20)

        # check specific element on the page
        self.assertIn('California Marcketing', driver.title)
        print("Page has", driver.title + " as Page title")

        H.delay()

        # Check that an image is present on the of a page and visible
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH,
                                                         "//img[@src='https://static.wixstatic.com/media/f914f1_f418ab6895dc482d89dc460c5b7d675b~mv2.png/v1/fill/w_120,h_120,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/iot_sq.png']")))
            print("The image Is present")
        except TimeoutException:
            print("Loading took too much time!")

        # click 'Blog link'
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class='_1zyfI'][contains(.,'Blog')]"))).click()
        WebDriverWait(driver, 20)

        # check specific element on the page
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(.,'All Posts')]")))
            print("The All Pasts link Is present")
        except TimeoutException:
            print("Loading took too much time!")

        # back in the browser
        driver.back()

    def tearDown(self):
        self.driver.quit()

    # check Shop link clickability on the top of the screen
    def test_shopworking_link(self):
        driver = self.driver
        driver.get(H.main_url)
        driver.maximize_window()
        wait = WebDriverWait(driver, 20)

        # click 'Shop' link
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class ='_1zyfI'][contains(., 'Shop')]"))).click()
        WebDriverWait(driver, 3)

        # assert 'Shop' title
        self.assertIn('Shop', driver.title)
        print("Page has", driver.title + " as Page title")

        H.delay()

        # check specific element on the page
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//h3[contains(.,'Product 1')]")))
            print("The 'Shop' page is present")
        except TimeoutException:
            print("Loading took too much time!")

        # back in the browser
        driver.back()

    def tearDown(self):
        self.driver.quit()

    # check Servises link clickability on the top of the screen
    def test_servises_link(self):
        driver = self.driver
        driver.get(H.main_url)
        driver.maximize_window()
        wait = WebDriverWait(driver, 20)

        # click 'Shop' link
        wait.until(EC.element_to_be_clickable((By.XPATH, "//p[@class ='_1zyfI'][contains(., 'Servises')]"))).click()
        WebDriverWait(driver, 3)

        # assert 'Shop' title
        self.assertIn('Servises', driver.title)
        print("Page has", driver.title + " as Page title")

        H.delay()

        # check specific element on the page
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, "//h1[contains(.,'Our Services')]")))
            print("The Servises page is present")
        except TimeoutException:
            print("Loading took too much time!")

        # back in the browser
        driver.back()

    def tearDown(self):
        self.driver.quit()

    # check working Subscribe Form functionality
    def test_subscribe_form(self):
        driver = self.driver
        driver.get(H.main_url)
        driver.maximize_window()

        # set up wait time
        wait = WebDriverWait(driver, 20)

        # assert 'Ca Marketing' title
        self.assertIn('California Marcketing', driver.title)
        print("Page has", driver.title + " as Page title")

        H.delay()

        # find 'Subscription form'
        form = wait.until(
            EC.visibility_of_element_located((By.XPATH, "(//span[contains(@class,'color_15')])[14]"))).text
        if form == "Subscribe Form":
            print("'Subscription form' was found")
        else:
            print("Cant find 'Subscription form'")

        H.delay()

        # put Email Address
        try:
            driver.find_element(By.XPATH, "//input[@id='input_comp-ksocylga1']").send_keys(fake.email())
            print("The email was put")
        except TimeoutException:
            print("The email wasn't put")

        # wait for  'Submit' button
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@aria-disabled='false'][contains(., 'Submit')]")))
        print("Submit button is present")

        # click on Submit button
        try:
            driver.find_element(By.XPATH, "//button[@aria-disabled='false'][contains(., 'Submit')]").click()
            print("The subscribe form was sent")
        except TimeoutException:
            print("The subscribe form wasn't sent")

        H.delay()

    def tearDown(self):
        self.driver.quit()

    # check "Get in touch" link functionality:
    def test_get_in_touchLink(self):
        driver = self.driver
        driver.get(H.main_url)
        self.driver.maximize_window()

        # set up wait time
        wait = WebDriverWait(driver, 20)

        # assert 'Ca Marketing' title
        self.assertIn('California Marcketing', driver.title)
        print("Page has", driver.title + " as Page title")

        H.delay()

        # check Get in touch link clicability
        try:
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "wQYUw"))).click()
            print("Get in touch link is clickable")
        except TimeoutException:
            print("Somthing went wrong")

        # check the button text is correct
        button_text = driver.find_element(By.CLASS_NAME, "wQYUw").text
        if button_text == "Get In Touch":
            print("Get in Touch' link text is correct")
        else:
            print("Incorrect link text")

        H.delay()

        # check that site email address is correct
        email = driver.find_element(By.XPATH, "//span[contains(.,'Get In Touch')]")
        email.get_attribute("href")

        H.delay()

        # print on page email and supposed email
        print(email)
        print(H.main_email)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))