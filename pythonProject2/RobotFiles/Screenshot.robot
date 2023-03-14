*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
Screenshot
    open browser    https://www.flipkart.com/   chrome
    maximize browser window

    capture element screenshot  xpath://*[@id="container"]/div/div[1]/div[1]/div[2]/div[1]/div/a[1]/img        C:\Users\vijay\PycharmProjects\pythonProject2\RobotFiles
    capture page screenshot     Logo.png
    close browser