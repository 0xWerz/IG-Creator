from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import utils
from selenium import *
from fake_useragent import UserAgent
import argparse
from colorama import Fore
y = Fore.LIGHTYELLOW_EX
b = Fore.LIGHTBLUE_EX
w = Fore.LIGHTWHITE_EX
r = Fore.RED
g = Fore.GREEN
parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("--firefox", action="store_true", help="Use Firefox - geckodriver")
group.add_argument("--chrome", action="store_true", help = "Use Chrome - chromedriver")
args = parser.parse_args()
try:
        rounds = int(input(f'{y}[{b}?{y}]{g} how many accounts: '))

except:
        print(f'\n{r}[{b}!{r}]{r} Type a correct integer')
        exit()
for i in range(rounds):
        ua = UserAgent()
        userAgent = ua.random
        if args.firefox:
                try:
                        firefox_driver_path = str(input(f'{y}[{b}?{y}]{g} A firefox driver path: '))

                        profile = webdriver.FirefoxProfile()
                        profile.set_preference("general.useragent.ovrride", userAgent)    
                        driver = webdriver.Firefox(firefox_profile=profile, executable_path=f'{firefox_driver_path}') # Put chrome driver path here!
                except:
                        print(f'\n{r}[{b}!{r}]{r} Set your firefox driver')
                        break
        #Chrome driver: 

        if args.chrome:
                try:
                        chrome_driver_path = str(input(f'{y}[{b}?{y}]{g} A chrome driver path: '))
                        from selenium.webdriver.chrome.options import Options
                        options = Options()
                        options.add_argument(f'user-agent={userAgent}')
                        driver = webdriver.Chrome(f'{chrome_driver_path}') # Put chrome driver path here!
                except:
                        print(f'\n{r}[{b}!{r}]{r} Set a valid path')
                        break       
        driver.get('https://www.instagram.com/accounts/emailsignup')
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])
        driver.get("https://10minutesemail.net/")
        mail_address = driver.find_element_by_id('tempEmailAddress').get_attribute('value')
        while mail_address == "Please wait...":
                mail_address = driver.find_element_by_id('tempEmailAddress').get_attribute('value')
        else:
                mail_address = mail_address
        driver.switch_to.window(driver.window_handles[0])

        # Accepting cookies window
        try:
                cookie = driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
        except:
                pass
        name = utils.username()

        # Fill email
        sleep(0.5)
        email_field = driver.find_element_by_name('emailOrPhone')
        email_field.send_keys(mail_address)
        print('email: ' + mail_address)
        
        # fill full name

        fullname_field = driver.find_element_by_name('fullName')
        fullname_field.send_keys(utils.generatingName())
        print('Full name: '+ utils.generatingName())
        #fill username
        username_field = driver.find_element_by_name('username')
        username_field.send_keys(name)


        print('username: ' + name)

        # Fill password 

        password_field = driver.find_element_by_name('password')
        password_field.send_keys(utils.generatePassword())  # You can determine another password here.
        password = utils.generatePassword()
        sumbit = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/form/div[7]/div/button"))).click()
        print('password: ' + password)


        unavail_mess = ["A user with that username already exists.", "This username isn't available. Please try another."]
        sleep(1.2)
        # New username if unavailable
        try :
                unavailable_user = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div[1]/div[2]/form/div[8]/p').text
                if unavailable_user in unavail_mess: 

                        print('username unavailable. Generating a new username...')
                        username_clear = driver.find_element_by_name('username').clear()
                        sleep(1)
                        username_field.send_keys(name,Keys.ENTER)
                        driver.find_element_by_xpath('/html/body/div[1]/div/div/section/main/div/div/div[1]/div[2]/form/div[7]/div/button').click()
                else :

                        break
        except:

                pass
        

        # Birthdate values 
        sleep(1.2)
        print('')
        driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[1]/select/option[4]"))).click()

        driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[2]/select/option[10]"))).click()

        driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select").click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[4]/div/div/span/span[3]/select/option[27]"))).click()

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='react-root']/section/main/div/div/div[1]/div/div[6]/button"))).click()
        sleep(0.5)

        
        # Requesting the verification code

        print("Waiting for the verification code...")
        driver.switch_to.window(driver.window_handles[1])
        sleep(13)

        invalid_code = ['If you receive any email, it will be shown in here!']
        while driver.find_element_by_xpath('/html/body/main/div[3]/div/div[1]/div/div[2]/div/table/tbody/tr/td[2]').text in invalid_code:
                code = driver.find_element_by_xpath('/html/body/main/div[3]/div/div[1]/div/div[2]/div/table/tbody/tr/td[2]').text                
        else:
                code = code[:6]
                print("Confirmation Code is: "+ code)

        driver.switch_to.window(driver.window_handles[0])

        # Security code  
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
                        sleep(3)
                else:
                        print('Account created information stored on a credentials.txt ')
        except:
                pass
        with open('credentials/credentials.txt','a') as f:
                f.write(f"""Email: {mail_address}\nUsername: {name}\nPassword:{password}\n  -----------""")