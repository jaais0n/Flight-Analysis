import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

# Set up Brave browser driver
def setup_driver():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-notifications")

    # Path to Brave browser executable
    options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

    # Automatically get ChromeDriver that matches Brave/Chrome version
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    return driver

# Search flights on Google Flights
def search_flights(driver, from_city, to_city, depart_date):
    print(f"Searching flights from {from_city} to {to_city} on {depart_date}...")

    # Open Google Flights
    driver.get("https://www.google.com/travel/flights")

    # Wait for page to load
    time.sleep(5)

    # Select the origin
    from_input = driver.find_element(By.XPATH, "//input[@placeholder='Where from?']")
    from_input.click()
    time.sleep(1)
    from_input.send_keys(Keys.CONTROL + "a")
    from_input.send_keys(Keys.BACKSPACE)
    time.sleep(1)
    from_input.send_keys(from_city)
    time.sleep(2)
    from_input.send_keys(Keys.ENTER)

    # Select the destination
    to_input = driver.find_element(By.XPATH, "//input[@placeholder='Where to?']")
    to_input.click()
    time.sleep(1)
    to_input.send_keys(Keys.CONTROL + "a")
    to_input.send_keys(Keys.BACKSPACE)
    time.sleep(1)
    to_input.send_keys(to_city)
    time.sleep(2)
    to_input.send_keys(Keys.ENTER)

    # Set departure date
    date_button = driver.find_element(By.XPATH, "//div[@role='button' and @aria-label[contains(., 'Departure')]]")
    date_button.click()
    time.sleep(2)

    # Use keyboard input to enter date
    date_field = driver.find_element(By.XPATH, "//input[@aria-label='Departure date']")
    date_field.clear()
    date_field.send_keys(depart_date)
    time.sleep(2)
    date_field.send_keys(Keys.ENTER)

    # Wait for results to load
    time.sleep(8)

    # Extract flight prices
    prices = driver.find_elements(By.XPATH, "//div[@class='YMlIz FpEdX']")
    if not prices:
        print("No flight prices found.")
    else:
        print(f"\nTop {len(prices)} prices found:")
        for i, price in enumerate(prices[:10], 1):
            print(f"{i}. {price.text}")

# Main
def main():
    from_city = "Muscat"
    to_city = "Kochi"
    depart_date = "Jun 15, 2025"  # Format as shown on Google Flights

    try:
        driver = setup_driver()
        search_flights(driver, from_city, to_city, depart_date)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Closing browser.")
        driver.quit()

if __name__ == "__main__":
    main()
