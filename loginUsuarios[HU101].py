import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

PATH = "/Users/martin/Desktop/Athletics-Tests/chromedriver/chromedriver"
pageAddress = "http://localhost:4200"

#HU101
class LoginPageTest(unittest.TestCase):
    
    #credentials
    adminPass = "admin"
    adminLog =  "admin"

    userPass = "somepass"
    userLog = "A00824394"

    trainerPass = "entrenador"
    trainerLog = "entrenador"

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)
    
    def test_adminLogin(self):
        driver = self.driver

        #Page Loads Correctly
        driver.get(pageAddress + "/login")
        self.assertIn("Athletic", driver.title)

        #Page Elements 
        loginField = driver.find_element(By.XPATH, "//*[@id='mat-input-0']")
        passField = driver.find_element(By.XPATH, "//*[@id='mat-input-1']")

        loginButton = driver.find_element(By.XPATH, "/html/body/app-root/div/app-login/mat-sidenav-container/mat-sidenav-content/div/div/form/div[3]/button")

        #Fields Input 
        loginField.click()
        loginField.send_keys(self.adminLog)

        passField.click()
        passField.send_keys(self.adminPass)

        loginButton.click()

        #Login Page Loaded Correctly and the User is Admin
        try:
            elem = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-sidebar/mat-sidenav-container/mat-sidenav-content/mat-toolbar/div/div/button/span[2]/div/div")) #This is a dummy element
            )
        finally:
            self.assertEqual(driver.find_element(By.XPATH, "/html/body/app-root/app-sidebar/mat-sidenav-container/mat-sidenav-content/mat-toolbar/div/div/button/span[2]/div/div").text, "admin")

    def test_userLogin(self):
        driver = self.driver

        #Page Loads Correctly
        driver.get(pageAddress + "/login")
        self.assertIn("Athletic", driver.title)

        #Page Elements 
        loginField = driver.find_element(By.XPATH, "//*[@id='mat-input-0']")
        passField = driver.find_element(By.XPATH, "//*[@id='mat-input-1']")

        loginButton = driver.find_element(By.XPATH, "/html/body/app-root/div/app-login/mat-sidenav-container/mat-sidenav-content/div/div/form/div[3]/button")

        #Fields Input 
        loginField.click()
        loginField.send_keys(self.userLog)

        passField.click()
        passField.send_keys(self.userPass)

        loginButton.click()

        #Login Page Loaded Correctly and the User is Admin
        try:
            elem = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-sidebar/mat-sidenav-container/mat-sidenav-content/mat-toolbar/div/div/button/span[2]/div/div")) #This is a dummy element
            )
        finally:
            self.assertEqual(driver.find_element(By.XPATH, "/html/body/app-root/app-sidebar/mat-sidenav-container/mat-sidenav-content/mat-toolbar/div/div/button/span[2]/div/div").text, "A00824394")      

    def test_trainerLogin(self):
        driver = self.driver

        #Page Loads Correctly
        driver.get(pageAddress + "/login")
        self.assertIn("Athletic", driver.title)

        #Page Elements 
        loginField = driver.find_element(By.XPATH, "//*[@id='mat-input-0']")
        passField = driver.find_element(By.XPATH, "//*[@id='mat-input-1']")

        loginButton = driver.find_element(By.XPATH, "/html/body/app-root/div/app-login/mat-sidenav-container/mat-sidenav-content/div/div/form/div[3]/button")

        #Fields Input 
        loginField.click()
        loginField.send_keys(self.trainerLog)

        passField.click()
        passField.send_keys(self.trainerPass)

        loginButton.click()

        #Login Page Loaded Correctly and the User is Admin
        try:
            elem = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-sidebar/mat-sidenav-container/mat-sidenav-content/mat-toolbar/div/div/button/span[2]/div/div")) #This is a dummy element
            )
        finally:
            self.assertEqual(driver.find_element(By.XPATH, "/html/body/app-root/app-sidebar/mat-sidenav-container/mat-sidenav-content/mat-toolbar/div/div/button/span[2]/div/div").text, "entrenador")

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main() 