from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

# Create a WebDriver instance (assuming you have set up your WebDriver executable path)
driver = webdriver.Chrome()

# Navigate to the desired URL
url = "https://cup-580fe3.webflow.io/diagnosis/biospy"  # Replace this with the URL you want to test
driver.get(url)

# Find all the links on the webpage
links = driver.find_elements(By.TAG_NAME, "a")

# Iterate through each link and validate it
for link in links:
    href = link.get_attribute("href")
    if href and href.startswith("http"):  # Check if the link starts with "http" (ignores anchors and other types of links)
        response = requests.head(href)
        if response.status_code == 200:
            print(f"Link {href} is working fine!")
        else:
            print(f"Link {href} is broken! Status code: {response.status_code}")

# Close the WebDriver
driver.quit()
