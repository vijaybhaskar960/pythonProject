*** Settings ***
Documentation

*** Variables ***
${name}     vijay   vaishu
${Scalar}   Prasad
*** Test Cases ***
Test
    Log     ${name}     warn
    log     ${Scalar}   error

