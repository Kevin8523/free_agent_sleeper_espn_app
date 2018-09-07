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

# Error Reading
import sys
import os

# Keep User Pass Hidden
import getpass

# Config file
import yaml

###################################################
# Load config file and seperate for convenience
###################################################
# dir_path = os.path.dirname(os.path.realpath(__file__))
# os.chdir('/Users/kevin8523/Desktop/Github/waiver_espn_app')
with open('test_config.yaml', 'rt') as f:
    config = yaml.load(f)
    
espn_config = config['espn_config']
driver_path_config = config['driver_path_config']
add_player_config = config['add_player_config']
drop_position_config = config['drop_position_config']

###################################################
# Input ESPN User Information
###################################################
# For best results put information in config.yaml
my_username = '{username}'.format(**espn_config) # username
my_password = '{pw}'.format(**espn_config) # pw
my_league = '{league}'.format(**espn_config)
# my_username = input("Please input ESPN username: ")
# my_password = getpass.getpass('Password:')
# my_league = input("Please input ESPN league: ")


###################################################
# Dictionary for ESPN roster free agent drop
###################################################
position = {
        'QB': '6',
        'RB1': '7',
        'RB2': '8',
        'WR1': '9',
        'WR2': '10',
        'TE': '11',
        'FLEX': '12',
        'D/ST': '13',
        'K': '14',
        'BENCH1': '17',
        'BENCH2': '18',
        'BENCH3': '19',
        'BENCH4': '20',
        'BENCH5': '21'
        }


###################################################
# Script to Run Program 
###################################################
# Path of the driver you installed
path = '{filepath}'.format(**driver_path_config)
filename = '{file}'.format(**driver_path_config)
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
free_agent.send_keys('{add_player}'.format(**add_player_config))
browser.find_element_by_id('lastNameSubmit').click()
time.sleep(8)

# Selects the + to add a player
add_player = browser.find_element_by_class_name('addButton')
add_player.click()

# Selects the player to remove
# Input Options: 
# QB,RB1,RB2,WR1,WR2,TE,FLEX,D/ST,K,BENCH1,BENCH2,BENCH3,BENCH4,BENCH5
# BENCH1 is the first bench player from the top, BENCH5 is the bottom most bench player
position_input = '{position_drop}'.format(**drop_position_config)

drop_player_position = position[position_input]
drop_player_xpath ='/html/body/div[2]/table/tbody/tr/td/div[3]/div/div/div/div[4]/div/div/div/div[3]/form/table[2]/tbody/tr/td/table/tbody/tr['+ drop_player_position +']/td[1]/input'
remove_player = browser.find_element_by_xpath(drop_player_xpath)
remove_player.click()

# Submit Roster
browser.find_element_by_xpath('/html/body/div[2]/table/tbody/tr/td/div[3]/div/div/div/div[4]/div/div/div/div[3]/form/div/input[1]').click()

# Confirm submit
browser.find_element_by_xpath('/html/body/div[2]/table/tbody/tr/td/div[3]/div/div/div/div[4]/div/div/div/form/div/input[1]').click()


"""
# Next Steps 
2. Check if player is available to add
6. Write function to loop over
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