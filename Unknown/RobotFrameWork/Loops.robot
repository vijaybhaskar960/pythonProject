*** Settings ***
Documentation    Loop operations using list

*** Variables ***
@{names}     sriram    kumar    balu    nagesh    Vijay

*** Test Cases ***
For loops with list
    FOR  ${name}    IN      @{names}

    Log    ${name}      Warn
    END

    FOR     ${index}   IN RANGE     5   20
    Log     ${index}    Error
    END

     FOR    ${V}    IN RANGE    10
        Continue For Loop If    ${V} != 3
        log    ${V}    WARN
        Exit For Loop If        ${V} >= 5
		log    ${V}		Warn

    END