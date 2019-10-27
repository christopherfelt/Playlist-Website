from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox(executable_path="geckodriver.exe")
# driver.get("https://www.youtube.com/watch?v=B7ooR2GF--I&feature=youtu.be")
driver.get("https://www.youtube.com/watch?v=95sdvU5T-Lk&feature=youtu.be")


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# driver.find_element_by_css_selector('.more-button style-scope')

element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="more"]'))
)

action = ActionChains(driver)
action.move_to_element(element)
action.click()
action.perform()
