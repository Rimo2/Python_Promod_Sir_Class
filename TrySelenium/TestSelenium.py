import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException

# Initialize logging
logging.basicConfig(filename='link_checker.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# Initialize the Chrome browser driver (you can use other browsers as well)
driver = webdriver.Chrome()

# Open the URL of your web app
web_app_url = "https://cup-580fe3.webflow.io/cancer-information/what-is-cancer"
driver.get(web_app_url)

# Find and collect all unique links on the page in a set
unique_links = set()
links = driver.find_elements(By.TAG_NAME,'a')
for link in links:
    try:
        # Refresh the element to avoid StaleElementReferenceException
        link = driver.find_element(By.TAG_NAME, "a")
        link_url = link.get_attribute("href")
        if link_url:
            unique_links.add(link_url)  # Add the link URL to the set
    except StaleElementReferenceException:
        # Handle StaleElementReferenceException by locating the element again
        logging.warning("StaleElementReferenceException occurred. Retrying...")
        link = driver.find_element(By.TAG_NAME, "a")
        link_url = link.get_attribute("href")
        if link_url:
            unique_links.add(link_url)  # Add the link URL to the set

# Close the browser after collecting links
driver.quit()

# Now, unique_links set contains all the unique URLs found on the web page
print("Set of unique links on the page:")
print(unique_links)
