*** Settings ***

Library  SeleniumLibrary


*** Test Cases ***
Scrolldown Operations

    open browser    https://www.amazon.in/      chrome
    maximize browser window
    execute javascript  window.scrollTo(0,1500)
    sleep   5

    execute javascript  window.scrollTo(0,document.body.scrollHeight)      #end of page
    sleep   5

    execute javascript  window.scrollTo(0,-document.body.scrollHeight)      #starting of page
    sleep   5




