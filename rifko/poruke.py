from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

# Path to the chromedriver executable
driver_path = '/path/to/chromedriver'

# Path to the Google Chrome binary file
chrome_binary_path = '/path/to/chrome/binary'

# Phone number of the recipient (in international format)
phone_number = '+381628908616'

# Message to be sent
message = 'Hello from Python!'

# Specify the path to the Chrome binary file
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = chrome_binary_path

# Create the webdriver instance with the specified options
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Go to WhatsApp Web
driver.get('https://web.whatsapp.com/')

# Wait for the user to scan the QR code with their phone
input('Press Enter after scanning QR code...')

# Find the search bar and type the recipient's phone number
search_bar = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
search_bar.send_keys(phone_number)
search_bar.send_keys(Keys.ENTER)

# Wait for the chat to load
time.sleep(5)

# Find the message input field and type the message
message_input = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')
message_input.send_keys(message)
message_input.send_keys(Keys.ENTER)

# Wait for the message to be sent
time.sleep(5)

# Close the browser
driver.quit()