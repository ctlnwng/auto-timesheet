import config
from splinter import Browser

browser = Browser()
# browser.visit('https://my.northeastern.edu/welcome')
# browser.click_link_by_text('Go To Login')

# browser.fill('username', username)
# browser.fill('password', password)
# browser.find_by_name('submit').click()

browser.visit('https://studentemployment.neu.edu/JobXHome.aspx')


browser.find_by_css('#ctl00_nav_seEmployees').mouse_over()
browser.click_link_by_text('My Timesheets')

browser.fill('Skin$ctl08$LoginNameText', config.username)
browser.fill('Skin$ctl08$LoginPasswordText', config.password)

browser.find_by_name('Skin$ctl08$ctl14').click()
browser.click_link_by_text(config.jobTitle)

browser.find_link_by_text('Go to time sheet').first.click()









# browser.fill('q', 'splinter - python acceptance testing for web applications')
# browser.find_by_name('btnK').click()

# if browser.is_text_present('splinter.readthedocs.io'):
#     print ("Yes, the official website was found!")
# else:
#     print ("No, it wasn't found... We need to improve our SEO techniques")
