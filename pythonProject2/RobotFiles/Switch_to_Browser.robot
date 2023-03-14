*** Settings ***

Library  SeleniumLibrary

*** Test Cases ***
Switch_To_Browser
    open browser    https://www.myntra.com/     chrome
    maximize browser window
    sleep   4
    open browser    https://www.flipkart.com/   chrome
    maximize browser window

    switch browser  1
    ${title}=   get title
    log to console  ${title}
    sleep   5
    switch browser  2
    ${title}=   get title
    log to console  ${title}

    sleep   5
    close all browsers