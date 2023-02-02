*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}      chrome
${url}      https://artoftesting.com/samplesiteforselenium

*** Test Cases ***
RadioButtons and Checkboxes
    open browser    ${url}      ${browser}
    maximize browser window
    set selenium speed  2seconds

    # Selecting the Radio Buttons
    select radio button  gender    female
    select radio button  gender    male

    # Selecting check Boxes
    select checkbox  Automation
    select checkbox    Performance

    # Unselecting check boxes
    unselect checkbox   Automation
    unselect checkbox   Performance

    close browser


*** Keywords ***
