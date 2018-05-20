import config
from splinter import Browser
from selenium import webdriver

browser = Browser()
# browser.visit('https://my.northeastern.edu/welcome')
# browser.click_link_by_text('Go To Login')

# browser.fill('username', username)
# browser.fill('password', password)
# browser.find_by_name('submit').click()

browser.visit('https://studentemployment.neu.edu/tsx_studentjobs.aspx')

browser.fill('Skin$ctl08$LoginNameText', config.username)
browser.fill('Skin$ctl08$LoginPasswordText', config.password)

browser.find_by_name('Skin$ctl08$ctl14').click()
browser.click_link_by_text(config.jobTitle)

browser.find_link_by_text('Go to time sheet').first.click()

browser.visit('https://studentemployment.neu.edu/tsx_stumanagetimesheet.aspx?TsId=2984981')

def addShift(shift):
    browser.click_link_by_text('Add New Entry')
    browser.find_by_id('Skin_body_ctl01_WDL').find_by_css('option')[shift.day].click()
    browser.find_by_id('Skin_body_ctl01_StartDateTime1').select(shift.start)
    browser.find_by_id('Skin_body_ctl01_EndDateTime1').select(shift.end)
    browser.find_by_value('Add').first.click()

for shift in config.shifts:
    addShift(shift)






