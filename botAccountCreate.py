from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import accountInfoGenerator as account
from selenium import webdriver
from time import sleep
from fake_useragent import UserAgent
import argparse
import requests


while True:




        # ---------------------------------------------------------------
                # running the browser


        parser = argparse.ArgumentParser()
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument("--firefox", action="store_true", help="Use Firefox - geckodriver")
        group.add_argument("--chrome", action="store_true", help = "Use Chrome - chromedriver")

        args = parser.parse_args()
        ua = UserAgent()
        userAgent = ua.random
        #print(userAgent)
        # for firefox driver : 
        if args.firefox:

                profile = webdriver.FirefoxProfile()
                profile.set_preference("general.useragent.ovrride", userAgent)    
                driver = webdriver.Firefox(firefox_profile=profile, executable_path=r"your gecko driver path here")
                
        #for chrome driver : 

        if args.chrome:
                from selenium.webdriver.chrome.options import Options
                options = Options()
                options.add_argument(f'user-agent={userAgent}')
                driver= webdriver.Chrome('your chrome driver')
        driver.get('https://www.instagram.com/accounts/emailsignup')
                # importing the box information 

        box_url = 'https://10minutesemail.net/getInbox'
        address_url = 'https://10minutesemail.net/getEmailAddress'
        main_page = 'https://10minutesemail.net'

        # main request
        main_page_req = requests.post(main_page)


        address_request = requests.post(address_url,cookies=main_page_req.cookies)


        address_data = address_request.json()

                # the email address string
        mail_address = str(address_data['address'])

                # recovery code string
        reco_key = str(address_data['recover_key'])
        print('recovery key: ' + reco_key)
        

        sleep(2)
        # accepting cookies window
        try:
                cookie = driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
        except:

                pass
        sleep(3)
        name = account.username()

        # fill email

        email_field = driver.find_element_by_name('emailOrPhone')
        fake_email = mail_address
        email_field.send_keys(fake_email)
        print('email: ' + fake_email)

        # fill full

        fullname_field = driver.find_element_by_name('fullName')
        fullname_field.send_keys(account.generatingName())
        print('Full name: '+ account.generatingName())
        #fill username
        username_field = driver.find_element_by_name('username')
        username_field.send_keys(name)


        print('username: ' + name)

        # Fill password value

        password_field = driver.find_element_by_name('password')
        password_field.send_keys(account.generatePassword())  # You can determine another password here.
        passwd = account.generatePassword()
        sumbit = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/form/div[7]/div/button"))).click()
        print('password: ' + passwd)


        unavail_mess = "This username isn't available. Please try another."
        sleep(1.2)
        # generating a new username if unavailable

        try :
                unavailable_user = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div/form/div[8]/p').text
                if unavailable_user == unavail_mess : 

        
                        print('generating a new username..')
                        username_clear = driver.find_element_by_name('username').clear()
                        sleep(1)
                        username_field.send_keys(name,Keys.ENTER)

                else :
                        pass
        except :
        
                pass
        

        # fill the birthdate values 
        sleep(1.2)
        print('')
        driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[4]"))).click()

        driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[10]"))).click()

        driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[27]"))).click()

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[6]/button"))).click()
        sleep(3)


        #  getting the verification code 


                # email box request

        box_req = requests.post(box_url, cookies=main_page_req.cookies).json()
        print('waiting for the code..')
        while box_req == []:

                box_req = requests.post(box_url, cookies=main_page_req.cookies).json()
                sleep(10)
        else:

                print("the code received!\n-everything saved in the backups file")
                dic_conv = box_req[0]

                #print(type(code))
                code_mess = dic_conv['subject']
                code = code_mess[0:6]
                print('insta code:'+ code)





        # fill instagram security code  
        driver.find_element_by_name('email_confirmation_code').send_keys(code, Keys.ENTER)
        sleep(5)

        try:






                not_valid = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[4]/div')
                if not_valid.text == 'That code isn\'t valid. You can request a new one.' :

                
                        sleep(1)
                        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[1]/div[2]/div/button').click()
                        sleep(5)
                        confInput = driver.find_element_by_name('email_confirmation_code')
                        confInput.send_keys(Keys.CONTROL + "a")
                        confInput.send_keys(Keys.DELETE)
                        confInput.send_keys(code, Keys.ENTER)
        except:         sleep(3)
                pass

        driver.close()
