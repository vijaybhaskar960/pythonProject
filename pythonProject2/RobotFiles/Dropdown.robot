*** Settings ***

Library  SeleniumLibrary

*** Variables ***
${browser}  https://www.globalsqa.com/demo-site/select-dropdown-menu/
${url}  chrome


*** Test Cases ***
DropdownValues
    open browser    ${url}  ${browser}
    maximize browser window
    sleep   5


