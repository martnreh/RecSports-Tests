import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

PATH = "/Users/martin/Desktop/Athletics-Tests/chromedriver/chromedriver"
pageAddress = "http://localhost:4200"

#HU101
class MenuPrincipalTest(unittest.TestCase):
    
    #credentials
    adminPass = "admin"
    adminLog =  "admin"

    userPass = "somepass"
    userLog = "A00824394"

    trainerPass = "entrenador"
    trainerLog = "entrenador"

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)
    
    def test_menuAdmin(self):
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

        assert driver.find_element(By.XPATH, "//*[@id='bar-card']/div")
        print("🟢 ADMIN Stats OK")
        assert driver.find_element(By.XPATH, "//*[@id='donut-card']")
        print("🟢 ADMIN Aforo OK")
        assert driver.find_element(By.XPATH, "/html/body/app-root/div/app-home/div/div/nz-content/div/div[2]/div[1]/app-news")
        print("🟢 ADMIN Anuncios OK")
        assert driver.find_element(By.XPATH, "/html/body/app-root/div/app-home/div/div/nz-content/div/div[2]/div[3]")
        print("🟢 ADMIN Deportes OK")


    def test_menuUser(self):
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

        assert driver.find_element(By.XPATH, "//*[@id='bar-card']/div")    
        print("🟢 USER Stats OK")
        assert driver.find_element(By.XPATH, "//*[@id='donut-card']")
        print("🟢 USER Aforo OK")
        assert driver.find_element(By.XPATH, "/html/body/app-root/div/app-home/div/div/nz-content/div/div[2]/div[1]/app-news")
        print("🟢 USER Anuncios OK")
        assert driver.find_element(By.XPATH, "/html/body/app-root/div/app-home/div/div/nz-content/div/div[2]/div[3]")
        print("🟢 USER Deportes OK")
    

    def test_menuTrainer(self):
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

        assert driver.find_element(By.XPATH, "//*[@id='bar-card']/div")
        print("🟢 TRAINER Stats OK")
        assert driver.find_element(By.XPATH, "//*[@id='donut-card']")
        print("🟢 TRAINER Aforo OK")
        assert driver.find_element(By.XPATH, "/html/body/app-root/div/app-home-entrenador/div/div/nz-content/div/div[2]/div[1]/div/button")
        print("🟢 TRAINER IN OK")
        assert driver.find_element(By.XPATH, "/html/body/app-root/div/app-home-entrenador/div/div/nz-content/div/div[2]/div[3]/div")
        print("🟢 TRAINER OUT OK")



        

    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main() 