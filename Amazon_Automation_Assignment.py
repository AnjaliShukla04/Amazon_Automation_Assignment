from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the Chrome driver options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(
    service=Service(r'C:\Users\Test\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'), options=options)

# Step 1: Search for a random product
driver.get('http://www.amazon.in')
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="twotabsearchtextbox"]')))

searchbar = driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
searchbar.send_keys('Flibbertygibbet 3000')
searchbar.send_keys(Keys.ENTER)

time.sleep(5)

try:
    no_results_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "No results found")]'))
    )
    print("Verified: No results found for 'Flibbertygibbet 3000'.")
except:
    print("Results were found for 'Flibbertygibbet 3000'.")

# Wait for the search results to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.sg-col-20-of-24')))

# Clear the search bar
searchbar = driver.find_element(By.XPATH, '//*[@id="twotabsearchtextbox"]')
searchbar.clear()

# Step 2: Search for "Laptop"
searchbar.send_keys('Laptop')
searchbar.send_keys(Keys.ENTER)

# Wait for the search results to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.sg-col-20-of-24')))

mainpage = driver.find_element(By.CSS_SELECTOR, 'div.sg-col-20-of-24')

# Get a list of product elements
listofproducts = mainpage.find_elements(By.CSS_SELECTOR, 'div.s-include-content-margin')

# Iterate over the list of product elements
for item in listofproducts:
    try:
        title_element = item.find_element(By.CSS_SELECTOR, 'span.a-size-medium')
        title_element.click()  # Click on the product title
        break  # Exit after clicking the first product
    except Exception as e:
        print(f"Error finding title in item: {e}")
        continue

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])

# Add to cart
addtocart = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="add-to-cart-button"]')))
addtocart.click()

# Wait for the cart confirmation
time.sleep(2)

# Click on "Go to Cart"
go_to_cart = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="sw-gtc"]')))
go_to_cart.click()

# Wait for the cart page to load
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Shopping Cart")]')))

# Click on the "Qty: 1" dropdown menu
try:
    quantity_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//span[@class="a-button a-button-dropdown quantity"]')))
    quantity_dropdown.click()
    quantity2 = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@id="quantity_2"]')))
    quantity2.click()

    # Select the quantity 2
    quantity_dropdown.send_keys(Keys.ARROW_DOWN)  # Go down to the second option (2)
    quantity_dropdown.send_keys(Keys.ENTER)
except Exception as e:
    print("Failed to increase quantity:", e)

# Wait for a moment to ensure the quantity update
time.sleep(5)

# Remove the product from the cart
try:
    remove_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@value="Delete"]')))
    remove_button.click()
except Exception as e:
    print("Failed to remove the product from the cart:", e)
time.sleep(5)

# Close the driver
driver.quit()
