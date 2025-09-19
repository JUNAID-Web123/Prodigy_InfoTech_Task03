import os
import csv
if not os.path.exists("test_results.csv"):
    with open("test_results.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Username", "Password", "Expected Result", "Actual Result"])


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
def save_result(username, password, expected, actual):
    with open("test_results.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password, expected, actual])

def run_test(username, password, expected):
    # Setup Chrome browser properly with Service
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get("https://www.saucedemo.com/")

    # Enter username and password
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)

    # Check results
    if expected == "success":
        if "inventory" in driver.current_url:
            print("✅ Test Passed: Valid Login")
        else:
            print("❌ Test Failed: Valid Login should succeed")
    else:
        try:
            error_message = driver.find_element(By.CSS_SELECTOR, "h3").text
            print(f"✅ Test Passed: Error shown - {error_message}")
        except:
            print("❌ Test Failed: Error not shown")

    driver.quit()


# Run different test cases
run_test("standard_user", "secret_sauce", "success")   # Valid credentials
run_test("wrong_user", "secret_sauce", "fail")        # Invalid username
run_test("standard_user", "wrong_pass", "fail")       # Invalid password
run_test("", "", "fail")                              # Empty fields
