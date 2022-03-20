from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


PROMISED_DOWN = 150
PROMISED_UP = 150
chrome_driver_path = Service("/Users/harryform/Documents/Development/chromedriver")
TWITTER_EMAIL = "pythonproject862@gmail.com"
TWITTER_PASSWORD = "gooberbutt1"
TWITTER_USERNAME = "pythonp99638201"
TWITTER_MESSAGE = "That's a big ole ooey"


class InternetSpeedTwitterBot:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=chrome_driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        time.sleep(3)
        go_button = self.driver.find_element(By.CLASS_NAME, "start-text")
        go_button.click()

        download_speed = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        upload_speed = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        time.sleep(60)

        result = {
            download_speed
        }

    def tweet_at_provider(self):
        # open twitter homepage
        self.driver.get("https://twitter.com/home")
        time.sleep(3)
        # type in email to login
        email_login = self.driver.find_element(By.NAME, "text")
        email_login.click()
        time.sleep(2)
        email_login.send_keys(TWITTER_EMAIL)
        time.sleep(2)
        email_login.send_keys(Keys.ENTER)
        time.sleep(2)
        # type in username so twitter will chill out
        username_entry = self.driver.find_element(By.NAME, "text")
        username_entry.send_keys(TWITTER_USERNAME)
        time.sleep(2)
        username_entry.send_keys(Keys.ENTER)
        # type in password
        time.sleep(2)
        password_entry = self.driver.find_element(By.NAME, "password")
        password_entry.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password_entry.send_keys(Keys.ENTER)
        # type that tweet
        time.sleep(5)
        tweet_message = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div")
        tweet_message.click()
        time.sleep(2)
        tweet_message.send_keys(TWITTER_MESSAGE)
        time.sleep(2)
        # send the tweet
        send_it = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span")
        send_it.click()


bot = InternetSpeedTwitterBot(chrome_driver_path)
current_speeds = bot.get_internet_speed()

down = float(current_speeds['download_speed'])



bot.tweet_at_provider()


