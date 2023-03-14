*** Settings ***
Library  SeleniumLibrary


*** Test Cases ***
Handle_Alert
    open browser    https://testautomationpractice.blogspot.com/2018/09/automation-form.html%20%20%20%20chrome      chrome
    maximize browser window
    click element   //button[text()='Click Me']
    sleep   5
    handle alert    accept
    sleep   5
    # handle alert  dismiss
    # handle alert  leave

    #alert should be present
    #alert should be not present  Press a button!

