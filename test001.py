from modulefinder import EXTENDED_ARG
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager

edge_driver = webdriver.Edge(EdgeChromiumDriverManager().install())
edge_driver.get("https://www.google.com")

import time
time.sleep(5)

edge_driver.close()