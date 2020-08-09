from instaUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Instagram:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("")
        time.sleep(2)

        usernameInput = self.browser.find_element_by_xpath()
        passwordInput = self.browser.find_element_by_xpath()

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def getFollewers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")

        follewersLink = self.browser.find_element_by_xpath()
        follewersLink.click()



insta = Instagram(username, password)
insta.signIn()
insta.getFollewers()







