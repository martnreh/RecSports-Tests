import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

PATH = "/Users/martin/Desktop/Athletics-Tests/chromedriver/chromedriver"
pageAddress = "http://localhost:4200"

#HU101
class aforoGimnasioTest(unittest.TestCase):
    
    #credentials
    userLog = "A01234567"
    userPass = "hola"

    def setUp(self):
        self.driver = webdriver.Chrome(PATH)
    
 
    def test_barraSuperiorUser(self):
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
            EC.presence_of_element_located((By.XPATH, "//*[@id='donut-card']"))
            )
        finally:
            aforoActual = driver.find_element(By.XPATH, "//*[@id='donut-card']/div/app-donut-chart/div[2]/div[1]").text

            result_array = str(aforoActual).split('/')
            aforoActual = int(result_array[0])
            print(aforoActual)

            assert aforoActual > 0 




    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main() 