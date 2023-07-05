from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import os

# Creating a webdriver instance
driver = webdriver.Chrome()
# This instance will be used to log into LinkedIn

# Opening linkedIn's login page
driver.get("https://linkedin.com/uas/login")
 
# waiting for the page to load
time.sleep(5)
 
# entering username
username = driver.find_element(By.ID, "username")
 
# In case of an error, try changing the element
# tag used here.
 
# Enter Your Email Address
username.send_keys("movieredeemer0@gmail.com") 
 
# entering password
pword = driver.find_element(By.ID, "password")
# In case of an error, try changing the element
# tag used here.
 
# Enter Your Password
pword.send_keys("letsgetthis2023")       
 
# Clicking on the log in button
# Format (syntax) of writing XPath -->
# //tagname[@attribute='value']
driver.find_element(By.XPATH, "//button[@type='submit']").click()
# In case of an error, try changing the
# XPath used here.

# Opening Kunal's Profile
# paste the URL of Kunal's profile here
profile_url = "https://www.linkedin.com/in/kunalshah1/"
 
driver.get(profile_url)        # this will open the link
start = time.time()
 
# will be used in the while loop
initialScroll = 0
finalScroll = 1000
 
while True:
    driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
    # this command scrolls the window starting from
    # the pixel value stored in the initialScroll
    # variable to the pixel value stored at the
    # finalScroll variable
    initialScroll = finalScroll
    finalScroll += 1000
 
    # we will stop the script for 3 seconds so that
    # the data can load
    time.sleep(3)
    # You can change it as per your needs and internet speed
 
    end = time.time()
 
    # We will scroll for 20 seconds.
    # You can change it as per your needs and internet speed
    if round(end - start) > 20:
        break


src = driver.page_source
 
# Now using beautiful soup
soup = BeautifulSoup(src, 'lxml')

