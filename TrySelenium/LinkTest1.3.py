from selenium import webdriver
from selenium.webdriver.common.by import By
import requests

# Create a WebDriver instance (assuming you have set up your WebDriver executable path)
driver = webdriver.Chrome()

# Navigate to the desired URL
url = "https://cup-580fe3.webflow.io/cancer-information/cancer-information-overview"  # Replace this with the URL you want to test
driver.get(url)

# Find all the links on the webpage

links = driver.find_elements(By.TAG_NAME, "a")

# Function to check if a link is working or broken
def check_link(link):
    href = link.get_attribute("href")
    if href and href.startswith("http"):  # Check if the link starts with "http" (ignores anchors and other types of links)
        response = requests.head(href, allow_redirects=True)
        if response.status_code == 200:
            print(f"Link {href} is working fine!")
        else:
            print(f"Link {href} is broken! Status code: {response.status_code}")
            # Print additional information about the broken link
            print(f"Text: {link.text}")
            print(f"Attributes: {link.get_attribute('outerHTML')}")
            print(f"Location: {link.location}")
            print(f"Size: {link.size}")
            print(f"Tag Name: {link.tag_name}")
            print(f"Class: {link.get_attribute('class')}")
            print(f"ID: {link.get_attribute('id')}")
            print(f"Name: {link.get_attribute('name')}")
            # You can add more attributes as needed

# Check each link on the webpage
for link in links:
    check_link(link)

# Close the WebDriver
driver.quit()
