*** Settings ***
Library      SeleniumLibrary
Resource     ../Resource/login_resource.robot
Library      DataDriver ../TestData/Demo.xlsx

#
#Suite Setup  Open Browser
#Test Template  Invalid login

*** Test Cases ***
LoginTestwithExecl   using  ${username}     ${password}


*** Keywords ***

Invalid login
    [Arguments]  ${username}     ${password}
    Input username  ${username}
    Input password  ${password}
    Click Login Button
    Error Message should be visible


