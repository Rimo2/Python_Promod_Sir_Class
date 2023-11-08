import logging
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize logging
logging.basicConfig(filename='link_checker.log', level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')

# Initialize the Chrome browser driver (you can use other browsers as well)
driver = webdriver.Chrome()

# Open the URL of your web app
web_app_url = "https://cup-580fe3.webflow.io/cancer-information/cancer-information-overview"
driver.get(web_app_url)

# Find and check all links on the page
links = driver.find_elements(By.TAG_NAME, "a")

broken_links = []  # List to store broken links
all_links = []
for link in links:
    link_url = link.get_attribute("href")
    link_text = link.text
    all_links.append(link_url)

    # Ignore the link with text 'Give Feedback'
    if link_text.strip() == 'Give Feedback':
        logging.info(f"Ignoring link '{link_url}' with text '{link_text}' (Give Feedback).")
        continue

    # Perform necessary checks or validations on the link URL
    # For example, you can check if the link is not empty and doesn't contain JavaScript:void(0)
    if link_url and "javascript:void(0)" not in link_url:
        # You can add more sophisticated checks as per your requirements
        try:
            # Attempt to click the link to ensure it's working (optional)
            link.click()
            logging.info(f"Link '{link_url}' is working.")
        except Exception as e:
            logging.error(f"Link '{link_url}' is broken. Error: {e}")
            broken_links.append(link_url)

# Close the browser after checking links
driver.quit()

# Generate a summary report
if broken_links:
    logging.info(
        f"\nSummary: {len(broken_links)} broken link(s) found. List of broken links: {', '.join(broken_links)}")
else:
    logging.info("No broken links found.")

