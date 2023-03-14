*** Settings ***
Documentation   *  Library for generating, modifying and verifying strings *

Library    String

*** Variables ***
${name}         VIJAY
${FNAME}        vijayreddy
${FULL_NAME}    vijaybhaskar reddy
${SPLIT}        vijay,bhaskar,reddy

*** Test Cases ***
Testcase:1
    ${name}    Convert To Lowercase    ${name}
    Log    After Converting Lowercase ==> #${name}    ERROR

    ${FNAME}   Remove String    ${FNAME}     bhaskar
    Log    After Removing SUB STRING ==> #${FNAME}    ERROR

    ${FULL_NAME}    Replace String    ${FULL_NAME}    vijay    vaishu   1
    Log    After Replace ==> ${FULL_NAME}    WARN

    ${SPLIT}    Split String    ${SPLIT}    ,
    Log    After spliting ==> ${SPLIT}    ERROR

    ${SUBSTRING}    Get Substring    ${name}    0    3
    Log    Substring is ==> ${SUBSTRING}    WARN
