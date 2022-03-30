import time
import pyautogui as pg
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import winsound
frequency = 2500
duration = 100

driver = webdriver.Chrome("C:\\Users\\eeshk\\Downloads\\chromedriver.exe")

driver.get("https://app.cowin.gov.in/")
driver.maximize_window()

driver.find_element(By.XPATH, value='//*[@id="login"]/div/form/ion-item[1]/ion-input/input').send_keys(9963149126)

driver.find_element(By.XPATH, value='//*[@id="login"]/div/form/ion-item[2]/ion-input/input').send_keys("Covin@123")

driver.find_element(By.XPATH, value='//*[@id="login"]/div/form/ion-button[1]').click()


def fun():

    pg.scroll(-10000)
    for i in range(1940, 2022):
        try:
            driver.find_element(By.XPATH,'//*[@id="main-content"]/app-vaccinate-beneficiary/ion-content/div/ion-grid/ion-row/ion-col/div/ion-row/ion-col/app-vaccine-benificiary-verify-otp/ion-grid/ion-row/ion-col[2]')
            pg.click(778, 475)
            pg.hotkey('ctrl', 'a')
            pg.write(str(i))
            pg.click(1002, 559)
            print(i)
            time.sleep(1)
        except:
            break



input()
time.sleep(2)

while True:
    try:
        driver.find_element(By.XPATH,'//*[@id="mat-tab-content-0-0"]/div/ion-grid/ion-row/ion-col/div/table/tbody/tr[1]').click()
    except:
        winsound.Beep(frequency, duration)
        print("unable to select user. Do it yourselfs")
        input("Then press enter")
    time.sleep(1)
    try:
        driver.find_element(By.XPATH,'//*[@id="main-content"]/app-vaccinate-beneficiary/ion-content/div/ion-grid/ion-row/ion-col/div/ion-row/ion-col/app-vaccine-benificiary-verify-otp/ion-grid/ion-row/ion-col[2]/div[3]/form/ion-row').click()
    except:
        winsound.Beep(frequency, duration)
        print("unable to press 'verify using other...'. Do it yourselfs")
        input("Then press enter")
    time.sleep(2)
    fun()


# dob at (778,475)
# verify at (1002,559)
# back at (18,54)
