*** Settings ***

Suite Setup  log to console     Opening Browser
Suite Teardown  log to console      Close Browser

Test Setup   log to console   Before Every test case Staring
Test Teardown  log to console   After Every test case complesion

*** Test Cases ***
TC1 Prepaid Recharge
    log to console  This is Prepaid Recharge Testcase

TC2 Postpaid Recharge
    log to console  This is Postpaid Recharge Testcase


