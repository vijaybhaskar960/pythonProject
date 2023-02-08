# Scalar
*** Settings ***
Documentation   To know how to do scalar operations

*** Variables ***
${NAME} =    Vijay_Vyshureddy
${EID}     123

*** Test Cases ***
Scalar Operations
    Log    ${EID}    WARN
    Log    ${NAME}  Warn


*** Settings ***
Documentation   To know how to do list operations

*** Variables ***
@{NAMES} =   sriram    RAJU    Balu    RAMESH    222

*** Test Cases ***
List Operations
    Log     ${NAMES}          ERROR
    Log    ${NAMES}[1:3]     ERROR
    Log    ${NAMES}[1:4}    WARN

*** Settings ***
Documentation   To know how to do Dictionary operations

*** Variables ***
&{DICT} =   name=kumar    eid=345    dname=IT

*** Test Cases ***
Dict Operations
    #Log    ${DICT}    WARN
    Log    ${DICT}[eid]    WARN

