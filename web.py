from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def get_trending_topics(driver, username, password):
    driver.get("https://twitter.com/login")
    time.sleep(3)

    # Login to Twitter
    username_input = driver.find_element(By.NAME, "session[username_or_email]")
    password_input = driver.find_element(By.NAME, "session[password]")

    username_input.send_keys(username)
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)

    # Navigate to home page
    driver.get("https://twitter.com/home")
    time.sleep(5)

    # Scrape the trending topics
    trends = driver.find_elements(By.XPATH,
                                  "//section[@aria-labelledby='accessible-list-0']//span[contains(@class, 'css-901oao')]")
    trending_topics = [trend.text for trend in trends[:5]]

    return trending_topics


# Example usage:
driver = webdriver.Chrome()
username = "your_twitter_username"
password = "your_twitter_password"
trending_topics = get_trending_topics(driver, username, password)
print(trending_topics)
driver.quit()
