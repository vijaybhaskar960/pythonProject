*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
MultipleBrowserTest
    open browser    https://www.myntra.com/     chrome
    maximize browser window
    sleep   4
    open browser    https://www.flipkart.com/   chrome
    maximize browser window

    switch browser  1
    ${title}=   get title
    log to console  ${title}

    switch browser  2
    ${title1}=   get title
    log to console  ${title1}

    sleep   3

    close all browsers
