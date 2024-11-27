import time
from selenium.webdriver.common.by import By
from seleniumbase import Driver
import mysql.connector
from winotify import Notification, audio

Current_date = None

def Toasty():
    toast = Notification(
        app_id='Vissa Appointment',
        title='Visa Appointment Found',
        msg='A new appointment schedule has been detected',
        duration='long',
        icon=r'C:\Users\Lenovo\Desktop\Hope\images.png'
    )
    toast.add_actions(label='Enter Website', launch='https://portal.ustraveldocs.com/')
    toast.set_audio(audio.LoopingAlarm, loop=True)
    return toast

def fetch_users():
    """Fetch user data from the database."""
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

while True:
    try:
        results = fetch_users()
        for row in results:
            try:
                driver = Driver(uc=True)
                url = "https://portal.ustraveldocs.com/"
                driver.uc_open_with_reconnect(url, 5)
                driver.uc_gui_click_captcha()

                time.sleep(2)

                # Login process
                Name = driver.find_element(By.CLASS_NAME, 'stylizedInput1')
                Password = driver.find_element(By.ID, 'loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:password')
                Check = driver.find_element(By.NAME, 'loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:j_id167')
                Login = driver.find_element(By.ID, 'loginPage:SiteTemplate:siteLogin:loginComponent:loginForm:loginButton')
                Name.send_keys(row['email'])
                Password.send_keys(row['password'])
                Check.uc_click()
                Login.uc_click()

                Date = driver.find_element(By.CLASS_NAME, 'leftPanelText')
                new_date = Date.text.strip()

                if Current_date != new_date:
                    print(f"Updated Current_date: {new_date}")
                    Current_date = new_date
                    toast = Toasty()
                    toast.show()

                    
                else:
                    print(f"No change in Current_date: {Current_date}")

            except Exception as e:
                print(f"An error occurred during Selenium processing: {e}.")
                continue
            finally:
                driver.quit()
                time.sleep(90)


    except Exception as e:
        print(f"An error occurred while fetching users: {e}, no diddy doe.")

