*** Settings ***

Library  SeleniumLibrary

*** Variables ***
${url}  https://demo.nopcommerce.com/
${browser}  chrome

*** Test Cases ***
LoginTest
    open browser      ${url}    ${browser}
    maximize browser window
    LoginToApplication
    close browser

*** Keywords ***
LoginToApplication
    click link  xpath://a[normalize-space()='Log in']
    sleep   5
    input text  id:Email  vijaybhaskar8341@gmail.com
    input text  id:Password  Test123@
    click element  xpath://button[normalize-space()='Log in']
    sleep   5
