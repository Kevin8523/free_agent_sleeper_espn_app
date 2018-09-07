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

# Searches Player by Name
browser.get(my_league)
browser.find_element_by_xpath('//*[@id="games-tabs"]/li[3]/a').click() # Goes to the games-tab and click on the 3rd tab

# Add Free Agent
free_agent = browser.find_element_by_id('lastNameInput')
free_agent.send_keys('Kai Forbath')
browser.find_element_by_id('lastNameSubmit').click()
time.sleep(8)

# Selects the + to add a player
add_player = browser.find_element_by_class_name('addButton')
add_player.click()

# Selects the player to remove
# Remove player based on position
# 6-14 are QB - K >> 6 = QB, 3 = RB, 14 = K
# 17-21 are Bench: 17 = 1st bench, 18 = 2nd bench player
# Add an index to have numbers correspond to each position
drop_player_position = '21'
drop_player_xpath ='/html/body/div[2]/table/tbody/tr/td/div[3]/div/div/div/div[4]/div/div/div/div[3]/form/table[2]/tbody/tr/td/table/tbody/tr['+ drop_player_position +']/td[1]/input'
remove_player = browser.find_element_by_xpath(drop_player_xpath)
remove_player.click()

# Submit Roster
browser.find_element_by_xpath('/html/body/div[2]/table/tbody/tr/td/div[3]/div/div/div/div[4]/div/div/div/div[3]/form/div/input[1]').click()

# Confirm submit
# uncomment below to have it run completely
browser.find_element_by_xpath('/html/body/div[2]/table/tbody/tr/td/div[3]/div/div/div/div[4]/div/div/div/form/div/input[1]').click()
