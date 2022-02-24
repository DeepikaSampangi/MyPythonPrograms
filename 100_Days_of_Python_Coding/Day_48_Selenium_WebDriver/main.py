from selenium import webdriver

chrome_driver_path = "./chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
url="https://www.python.org/"
driver.get(url)

headline = driver.find_element("dive-into-python")
print(headline.text)

driver.close()