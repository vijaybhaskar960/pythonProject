*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${url}      https://demo.guru99.com/test/newtours/
${browser}   chrome

*** Test Cases ***
TestCase:
    ${page_title}=   LaunchBrowser   ${url}  ${browser}
    log to console  ${page_title}
    input text    name:userName     Vijay
    input text    name:password     Mercury

*** Keywords ***
LaunchBrowser
    [Arguments]  ${appurl}  ${appbrowser}
    open browser    ${url}      ${browser}
    maximize browser window
    ${title}=   get title
    [Return]    ${title}


