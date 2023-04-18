
*** Settings ***
Library  SeleniumLibrary


*** Test Cases ***
GET-TITLE
    open browser    https://www.myntra.com/     chrome
    maximize browser window
    ${loc}=     get location
    log to console  ${loc}
    ${title}    get window titles
    log to console  ${title}

    go to   https://www.amazon.in/

    ${title}    get window titles
    log to console  ${title}

    go back
    ${loc}      get location

