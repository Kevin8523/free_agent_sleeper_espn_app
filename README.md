# ESPN Fantasy Football Free Agency Program

## Overview
This script is a tool to add/drop players once the waiver wire process ends to prevent from using your waiver priority. Since the waiver usually ends in the middle of the night, this script will allow you to get first priority and to run when the waiver opens. 
- This script does not schedule the task, you will either need to set up a task scheduler of some sort
- This was written on MACOS so some minor configurations may be required for WINDOWS 

## Requirements Before Running Script
- Packages Needed: BeautifulSoup, selenium, os, sys
- Install webdriver for your internet browser, this program for Firefox (http://learn-automation.com/firefox-browser-on-mac-using-selenium-webdriver/)

## Use config.yaml to add in all the information needed: Script Requirement
- ESPN username: Username@gmail.com
- ESPN Password: password_here
- League ID URL: http://games.espn.com/ffl/leagueoffice?leagueId=LEAGUE_ID_NUMBER_WILL_BE_HERE

## To Do:
0. Check if player is available to add
1. Select on + to add 
2. Check if player is still on your roster
3. Select on player to drop
4. Submit Roster
5. Confirm
6. Write function to loop over
7. Make a yaml file to add user/pw/league and remove from this script 
8. Make a log file
9. Schedule a Airflow job
10. Test to add on AWS 
