import selenium
from selenium import webdriver

print("Selenium version:", selenium.__version__)

chrome = webdriver.Chrome(executable_path="./chromedriver")

chrome.get("https://www.amazon.fr")

link = chrome.find_element_by_link_text("Voir tout")

link.click()
