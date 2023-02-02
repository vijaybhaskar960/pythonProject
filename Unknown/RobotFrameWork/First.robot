*** Settings ***

Library  SeleniumLibrary

*** Variables ***

${browser}      chrome
${url}    https://www.amazon.in/

*** Test Cases ***
LoginTest
    open browser   ${url}   ${browser}
    maximize browser window
    LoginToApplication
    close browser

*** Keywords ***
LoginToApplication
    click link    id:nav-link-accountList
    input text    id:ap_email      8074517920
    click element    id:continue
    input text    id:ap_password    vijayareddy@gmail.com
    click element    id:signInSubmit




