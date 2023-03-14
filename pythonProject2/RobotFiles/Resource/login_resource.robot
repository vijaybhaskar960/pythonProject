*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***

${url}      https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F
${browser}  chrome

*** Keywords ***
Open Browser
    open browser  ${browser}    ${url}
    maximize browser window

Open Login Page
    go to  ${url}

Input username
    [Arguments]   ${username}
    input text  id:Email    ${username}

Input password
    [Arguments]     ${password}
    input text  id:password     ${password}

Click Login Button

    click element   xpath://button[@class="button-1 login-button"]







