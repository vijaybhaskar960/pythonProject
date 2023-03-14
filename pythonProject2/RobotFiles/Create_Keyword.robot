*** Settings ***
Documentation


*** Test Cases ***
Testcase:1
    Addition

Testcase:2
    Subtraction  10     5

Testcase:3
    ${RV}     Multiplication    5    10
    Log       Multip OF 5 * 10 = ${RV}    ERROR





*** Keywords ***
Addition
    [Documentation]  keywords without arguments
    ${sum}  Evaluate    5 + 5
    log to console  Addition of = ${sum}  warn

Subtraction
    [Arguments]  ${a}   ${b}
    [Documentation]     Keyword with arguments
    ${sub}  Evaluate    ${a} - ${b}
    log to console  sub of = ${sub}  warn

Multiplication  [Arguments]     ${a}    ${b}
    [Documentation]   Keyword with RETURN
    ${Mul}   Evaluate    ${a}  *  ${b}
    [Return]   ${Mul}


