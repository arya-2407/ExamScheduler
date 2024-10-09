from selenium import webdriver

url = 'https://heat.csc.uvic.ca/coview/course/2024091/CSC370?unp=t'

# Set up headless mode for Chrome with additional options
options = webdriver.ChromeOptions()
options.add_argument('--headless=new')  # Use the new headless mode if supported
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-extensions')
options.add_argument('--hide-scrollbars')
options.add_argument('--window-size=1920,1080')
options.add_argument('--disable-software-rasterizer')

driver = webdriver.Chrome(options=options)
driver.get(url)

# Extract the page source
html = driver.page_source
print(type(html))

driver.quit()

"""f=open("output.txt","a")
f.write(html)
f.close()"""