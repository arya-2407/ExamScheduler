from selenium import webdriver

url = 'https://heat.csc.uvic.ca/coview/course/2024091/CSC370?unp=t'

# Use a headless browser to run in the background
options = webdriver.ChromeOptions()
options.headless = True

# Adjust the path to your Chrome driver
driver = webdriver.Chrome(options=options)
driver.get(url)

# Extract the page source
html = driver.page_source
print(html)


driver.quit()
