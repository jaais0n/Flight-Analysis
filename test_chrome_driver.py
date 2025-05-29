from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    print("Setting up Chrome driver...")
    # webdriver_manager automatically downloads and matches your Chrome version
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def main():
    driver = setup_driver()
    driver.get("https://www.google.com")
    print("Opened Google. Title:", driver.title)
    driver.quit()

if __name__ == "__main__":
    main()
