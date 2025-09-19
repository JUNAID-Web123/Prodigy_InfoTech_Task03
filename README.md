Selenium Login Test Automation

This project demonstrates automated login testing for the SauceDemo website using Python, Selenium, and Chrome WebDriver. It runs multiple test cases with different username-password combinations, checks whether login succeeds or fails, and stores the results in a CSV file.

Features
Automates login process on SauceDemo.

Tests multiple cases including valid, invalid, and empty credentials.

Prints test result status (✅ Pass / ❌ Fail) in the terminal.

Saves results into a CSV file (test_results.csv) with the following fields:

Username

Password

Expected Result

Actual Result

Requirements
Python 3.8 or later

Google Chrome browser installed

Required Python libraries:

selenium

webdriver-manager

Installation
Clone or download the project code.

Navigate to the project folder.

Install dependencies:

bash
pip install selenium webdriver-manager
Usage
Run the script:

bash
python login_test.py
The tests will execute automatically:

Opens the Chrome browser.

Attempts login with different credentials.

Prints pass/fail results in the terminal.

Saves test results into test_results.csv.

Test Cases Implemented
Valid Credentials → standard_user / secret_sauce

Invalid Username → wrong_user / secret_sauce

Invalid Password → standard_user / wrong_pass

Empty Fields → /

Output
Console Example:

text
✅ Test Passed: Valid Login
✅ Test Passed: Error shown - Epic sadface: Username and password do not match any user in this service
❌ Test Failed: Valid Login should succeed
test_results.csv Example:

Username	Password	Expected Result	Actual Result
standard_user	secret_sauce	success	success
wrong_user	secret_sauce	fail	fail
standard_user	wrong_pass	fail	fail
fail	fail
Notes
The script opens a new browser window for each test case.

You can add more test cases by modifying the run_test() calls at the bottom.

If ChromeDriver version issues occur, ensure your Google Chrome is up to date.
