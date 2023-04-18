*** Settings ***
Documentation

*** Variables ***
${name}     Vijay   Vaishu
${Scalar}   Prasad
*** Test Cases ***
Test
    Log     ${name}     warn
    log     ${Scalar}   error

