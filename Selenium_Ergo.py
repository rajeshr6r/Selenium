# -*- coding: utf-8 -*-
"""
Created on Fri May 17 08:38:50 2019

@author: Rajesh_Raj
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

# Using Chrome to access web
Chromedriver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
#actions
ChromeActions = ActionChains(Chromedriver)
Chromedriver.implicitly_wait(30)
Chromedriver.maximize_window()
#Open the website 
Chromedriver.get('https://www.hdfcergo.com/car-insurance')
Chromedriver.implicitly_wait(5) # wait for 5
Chromedriver.find_element_by_link_text('Continue without Vehicle Number / New Vehicle').click() # as this opens a new window blody hell move to it
Chromedriver.implicitly_wait(5) # wait for 5
another_window = list(set(Chromedriver.window_handles) - {Chromedriver.current_window_handle})[0]
Chromedriver.switch_to.window(another_window)
Chromedriver.implicitly_wait(5) # wait for 5
elem=Chromedriver.find_element_by_name('Maruti') # the brand name here
elem.click()
elem=Chromedriver.find_element_by_name('ALTO') # the model
elem.click()
elem=Chromedriver.find_element_by_name('1.1 LXI') # the sub model
elem.click()
elem=Chromedriver.find_element_by_name('2016') # manufacturing year 
elem.click()
elem=Chromedriver.find_element_by_id('modalRegistrationMonth') # modalRegistrationMonth
month_elems=elem.find_elements_by_class_name('RegistrationMonth') # get into a list of months within the modal popup
for el_month in month_elems:
    targetmonth=el_month.get_attribute('value')
    if targetmonth=='1': # January
        el_month.click()
        break
#City Of Registration
elem=Chromedriver.find_element_by_name('KA-02 - Bengaluru') #   
elem.click()
#TypeOfNewPolicy
elem=Chromedriver.find_element_by_id('Comprehensive') #   
elem.click()
#TypeOfPreviousPolicy
elem=Chromedriver.find_element_by_id('Comprehensive') #   
elem.click()
#PreviousPolicyStatus
elem=Chromedriver.find_element_by_id('NotExpired') #   
elem.click()
#NCB
ncb_options=Chromedriver.find_elements_by_id('ClaimLastTaken') #   
for option in ncb_options:
    targetoption=option.get_attribute('value')    
    if targetoption=='True': # NCB Yes        
        option.su # Input 
        break
    





elem.click()

action.moveToElement(elem).click().build().perform()

act.click(elementValue).build().perform();

"""
soup=BeautifulSoup(Chromedriver.page_source)
for link in soup.find_all('div'):
    print (link.get('class',None))
"""
