*** Settings ***
Documentation

*** Variables ***
${name}     Vaishu                           # Scalar operations
${Surname}  Reddy
@{names}    Vaishu  Damini  Lakshmi     Roja        # List Operation
&{Dict}=    name=Vijay  dep=IT  salary=80k      #  Dictionary Operations

*** Test Cases ***
TestCase1
    log to console  ${name}     warn
    log to console  ${Surname}  Error
    log to console  ${names}    Warn
    log to console  ${Dict}     Error


