*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
Handle-Alert-Window
    open browser    https://testautomationpractice.blogspot.com/2018/09/automation-form.html    chrome
    maximize browser window
    click element   //button[text()='Click Me']
    sleep   4
    #handle alert  accept
    #handle alert    dismiss
    #handle alert    leave

    alert should be present     Press a button!
    #alert should not be present     Press a button!
