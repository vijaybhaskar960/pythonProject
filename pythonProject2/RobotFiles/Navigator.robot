*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
Navigations
    open browser    https://www.amazon.in/      chrome
    maximize browser window
    ${loc}=     get location
    log to console  ${loc}
    sleep  5
    go to   https://www.myntra.com/
    ${loc}=     get location
    log to console  ${loc}
    sleep   5
    go back
    ${loc}=     get location
    log to console  ${loc}

    close browser

