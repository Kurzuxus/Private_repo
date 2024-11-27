from concurrent.futures import ThreadPoolExecutor
from seleniumbase import Driver
import sys
import mysql.connector
from time import sleep
from selenium.webdriver.common.by import By

sys.argv.append('-n')


def fetch():
    query = "SELECT * FROM users.data_users;"
    with mysql.connector.connect(
            host='localhost',
            user='root',
            password='Badkik88',
            database='users'
        ) as conn:
            with conn.cursor(dictionary=True) as cursor:
                cursor.execute(query)
                return cursor.fetchall()


def launch_driver(email,password):
        try:
            driver = Driver(uc=True,proxy='baroudisidahmed18_gmail_com-country-any:imkq58t93g@gate.nodemaven.com:8080')
            url = "https://portal.ustraveldocs.com/"
            driver.uc_open_with_reconnect(url, 5)
            driver.uc_gui_click_captcha()

            sleep(2)

            Name = driver.find_element(By.CLASS_NAME, 'stylizedInput1')
            Password = driver.find_element(By.ID, 'loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:password')
            Check = driver.find_element(By.NAME, 'loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:j_id167')
            Login = driver.find_element(By.ID, 'loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:loginButton')
            Name.send_keys(email)
            Password.send_keys(password)
            Check.uc_click()
            Login.uc_click()

            sleep(2)
        finally:
            driver.quit()

filtered=fetch()[10:18]

with ThreadPoolExecutor(max_workers=len(filtered)) as executor:
    for account in filtered:
        executor.submit(launch_driver,account['email'],account['password'])

