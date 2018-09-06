# -*- coding: utf-8 -*-
"""
Created on Sun Sept  2 14:30:26 2018
author: Kevin Huang
"""

###################################################
# Import Packages: 
###################################################
# Controlling the Browser - Webscrape for Websites with logins
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

# Reading Excel Spreadsheets
import openpyxl
import os

# Error Reading
import sys

# Keep User Pass Hidden
import getpass


###################################################
# Input ESPN User Information
###################################################
# For best results hardcode information and comment out the inputs
my_username = input("Please input ESPN username: ")
my_password = getpass.getpass('Password:')
my_league = input("Please input ESPN username: ")
# my_username = 'myusername@gmail.com' # Email or username
# my_password = 'my_password'
# my_league = 'http://games.espn.com/ffl/leagueoffice?leagueId=LEAGUE_ID_NUMBER_WILL_BE_HERE'


###################################################
# Script to Run Program 
###################################################
# Path of the driver you installed
path = '/Users/kevin8523/Desktop/Github/waiver_espn_app/'
filename = 'geckodriver'
firefox_path = f'{path}{filename}'

# Opens Firefox & goes to the Website (Must download chrome driver from the interwebs)
browser = webdriver.Firefox(executable_path = firefox_path)
browser.get('http://games.espn.go.com/ffl/signin')

# Waits for the login to pop-up and switches so you can find that frame
wait = WebDriverWait(browser, 1000)
wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "disneyid-iframe")))

# Add Username & Pw
username = browser.find_element_by_xpath("//input[@type='email']")
username.send_keys(my_username)
passwordElem = browser.find_element_by_xpath("//input[@type='password']")
passwordElem.send_keys(my_password)
elem = browser.find_element_by_xpath("//button[@type='submit']")
elem.click()

time.sleep(8)
browser.switch_to_default_content()

# Go to League Free Agency Page
browser.get(my_league)
browser.find_element_by_xpath('//*[@id="games-tabs"]/li[3]/a').click() # Goes to the games-tab and click on the 3rd tab

# Add Free Agent
free_agent = browser.find_element_by_id('lastNameInput')
free_agent.send_keys('Kai Forbath')
browser.find_element_by_id('lastNameSubmit').click()

add_player = browser.find_element_by_class_name('addButton')
add_player.click()

"""
# Next Steps 
0. Check if player is available to add
1. Select on + to add 
2. Check if player is still on your roster
3. Select on player to drop
4. Submit Roster
5. Confirm
6. Write function to loop over
7. Make a yaml file to add user/pw/league and remove from this script 
8. Make a log file
"""




###################################################
# Send Alert Email
###################################################
"""
1. Logic to only do Create request
2. Pull email and input text
3. Send
"""