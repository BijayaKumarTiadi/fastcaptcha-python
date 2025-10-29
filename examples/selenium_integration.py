"""
Example: Selenium Integration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This example demonstrates how to integrate FastCaptcha with Selenium for
automated web scraping and form submission.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fastcaptcha import FastCaptcha
import time

def solve_captcha_with_selenium():
    """
    Example function showing how to solve a CAPTCHA during Selenium automation.
    """
    
    # Initialize FastCaptcha solver
    api_key = "your-api-key-here"  # Replace with your actual API key
    solver = FastCaptcha(api_key=api_key)
    
    # Initialize Selenium WebDriver
    driver = webdriver.Chrome()  # or webdriver.Firefox(), etc.
    
    try:
        # Navigate to page with CAPTCHA
        print("Navigating to page...")
        driver.get("https://example.com/login")  # Replace with actual URL
        
        # Wait for CAPTCHA image to load
        wait = WebDriverWait(driver, 10)
        captcha_element = wait.until(
            EC.presence_of_element_located((By.ID, "captcha-image"))
        )
        
        # Option 1: Download CAPTCHA image and solve
        print("Downloading CAPTCHA image...")
        captcha_src = captcha_element.get_attribute("src")
        
        if captcha_src.startswith("data:"):
            # Base64 encoded image
            base64_data = captcha_src.split(",")[1]
            result = solver.solve_base64(base64_data)
        else:
            # URL image
            result = solver.solve_url(captcha_src)
        
        print(f"CAPTCHA solved: {result}")
        
        # Enter the CAPTCHA solution
        captcha_input = driver.find_element(By.ID, "captcha-input")
        captcha_input.clear()
        captcha_input.send_keys(result)
        
        # Fill other form fields
        username_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")
        
        username_input.send_keys("your_username")
        password_input.send_keys("your_password")
        
        # Submit the form
        submit_button = driver.find_element(By.ID, "submit-button")
        submit_button.click()
        
        # Wait for login success
        time.sleep(2)
        print("✓ Form submitted successfully!")
        
    except Exception as e:
        print(f"✗ Error: {e}")
        
    finally:
        # Cleanup
        solver.close()
        driver.quit()


def solve_captcha_screenshot():
    """
    Alternative method: Take a screenshot of the CAPTCHA element.
    """
    
    api_key = "your-api-key-here"
    solver = FastCaptcha(api_key=api_key)
    driver = webdriver.Chrome()
    
    try:
        driver.get("https://example.com/login")
        
        # Find CAPTCHA element
        captcha_element = driver.find_element(By.ID, "captcha-image")
        
        # Take screenshot of CAPTCHA element
        captcha_element.screenshot("captcha_screenshot.png")
        
        # Solve from file
        result = solver.solve("captcha_screenshot.png")
        print(f"CAPTCHA solved: {result}")
        
        # Enter solution
        captcha_input = driver.find_element(By.ID, "captcha-input")
        captcha_input.send_keys(result)
        
    finally:
        solver.close()
        driver.quit()


if __name__ == "__main__":
    print("Example 1: Solve CAPTCHA from src attribute")
    print("=" * 50)
    solve_captcha_with_selenium()
    
    print("\n\nExample 2: Solve CAPTCHA from screenshot")
    print("=" * 50)
    solve_captcha_screenshot()
