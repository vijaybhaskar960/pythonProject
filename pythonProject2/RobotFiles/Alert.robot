*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
AlertHandle
    open browser    https://testautomationpractice.blogspot.com/    chrome
    maximize browser window
    click element   xpath://button[normalize-space()='Click Me']    # open alert
    sleep   5
    #handle alert    accept
    #handle alert    dismiss
    handle alert    leave
    alert should be present     Press a button!
    alert should not be present     Press a button!


