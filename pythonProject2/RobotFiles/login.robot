*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
Navigations
    open browser    https://www.google.co.in/   chrome
    ${loc}=     get location
    log to console  ${loc}

    sleep   3
    go to   https://www.flipkart.com/
    ${loc}=     get location
    log to console  ${loc}
    sleep   3
    go back
    ${loc}=     get location
    log to console  ${loc}