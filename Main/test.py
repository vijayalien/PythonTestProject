from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://admin-demo.nopcommerce.com/login")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@class='email valid']").clear()
driver.find_element(By.XPATH, "//input[@class='email valid']").send_keys("admin@yourstore.com")

driver.find_element(By.ID, "Password").clear()
driver.find_element(By.ID, "Password").send_keys("admin")

driver.find_element(By.XPATH, "//button[@type='submit']").click()

print(driver.title)
