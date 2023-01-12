from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # this is for the adaptor for chrome
from selenium.webdriver.common.by import By  # to look for something by,,,,
from selenium.webdriver.common.keys import Keys  # such as enter and tab
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
TWITTER_USER = ""  # insert your username and password
TWITTER_PASS = ""
TWITTER_URL = "https://twitter.com/"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = 0
        self.up = 0
        self.chrome_path = Service(CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.chrome_path)

    def get_internet_speed(self):
        url = "https://www.speedtest.net/"  # this is the web that checks the speed
        self.driver.get(url)
        self.driver.find_element(By.CSS_SELECTOR, '.start-button span.start-text').click()
        time.sleep(120)
        print("it worked now we need to get the data from here")
        self.down = float(self.driver.find_element(By.XPATH,
                                                   '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
        self.up = float(self.driver.find_element(By.XPATH,
                                                 '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
        return self.down, self.up

    def login_twitter(self):
        self.driver.get(TWITTER_URL)
        login_page = self.driver.current_window_handle
        time.sleep(10)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span').click()
        time.sleep(10)
        # switching to the login popup tab
        # for handle in self.driver.window_handles:
        #     if handle != login_page:
        #         login_fill = handle
        # time.sleep(20)
        # self.driver.switch_to.window(login_fill)
        user = self.driver.find_element(By.XPATH,
                                        '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        user.send_keys(TWITTER_USER)
        user.send_keys(Keys.ENTER)
        # for handle in self.driver.window_handles:
        #     if handle != login_page or handle != login_fill:
        #         fill_pass = handle
        # self.driver.switch_to.window(fill_pass)
        time.sleep(20)
        passwd = self.driver.find_element(By.XPATH,
                                          '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        passwd.send_keys(TWITTER_PASS)
        passwd.send_keys(Keys.ENTER)

    def send_tweet(self, mess):
        time.sleep(10)
        tweet = self.driver.find_element(By.XPATH,
                                         '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(mess)
        self.driver.find_element(By.XPATH,
                                 '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()
        self.driver.quit()


twitt_internet = InternetSpeedTwitterBot()
down_speed, up_speed = twitt_internet.get_internet_speed()
if down_speed < PROMISED_DOWN or up_speed < PROMISED_UP:
    time.sleep(10)
    twitt_internet.login_twitter()
    message = f"Hey Hot, why is my internet speed {down_speed}down/{up_speed}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}/up???"
    twitt_internet.send_tweet(message)
