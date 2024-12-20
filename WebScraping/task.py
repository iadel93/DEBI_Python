from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import os

def download_images(search_query, num_images):
    # Set up the Chrome WebDriver
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Run in headless mode (no GUI)
    driver = webdriver.Chrome(options=options)

    # Create a directory to save images
    if not os.path.exists(search_query):
        os.makedirs(search_query)

    # Construct the search URL and navigate to it
    search_url = f"https://www.google.com/search?hl=en&tbm=isch&q={search_query}"
    driver.get(search_url)

    # Wait for images to load
    time.sleep(2)

    # Find image elements on the page
    image_elements = driver.find_elements(By.CLASS_NAME, 'rg_i')
    print(image_elements)
    count = 0
    for img in image_elements:
        try:
            img.click()  # Click on the thumbnail to open the full image
            time.sleep(1)  # Wait for the full image to load
            
            # Locate the full-size image element and get its URL
            full_img_element = driver.find_element(By.CLASS_NAME, 'n3VNCb')
            img_url = full_img_element.get_attribute("src")

            # Download the image if it's a valid URL
            if img_url.startswith('http'):
                response = requests.get(img_url)
                if response.status_code == 200:
                    with open(os.path.join(search_query, f'image_{count + 1}.jpg'), 'wb') as file:
                        file.write(response.content)
                        count += 1

            # Stop after downloading the specified number of images
            if count >= num_images:
                break

        except Exception as e:
            print(f"An error occurred: {e}")

    driver.quit()  # Close the browser

# Example usage: Download 5 images of "cats"
download_images("cats", 5)
