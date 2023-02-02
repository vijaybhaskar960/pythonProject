*** Settings ***
Library  SeleniumLibrary


*** Test Cases ***
Multiple-Browsers
    open browser    https://www.flipkart.com/   chrome
    maximize browser window
    open browser    https://www.myntra.com/     chrome
    maximize browser window
    #close browser
    close all browsers
