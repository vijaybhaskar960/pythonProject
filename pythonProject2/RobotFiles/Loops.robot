*** Settings ***
Documentation  Loops


*** Test Cases ***
TestCase2
    FOR  ${i}  IN RANGE  1   10
        log to console  ${i}    Warn

    END

TestCase3
    FOR  ${i}  IN RANGE  0   10   2
         log to console  ${i}    Warn

        END
TestCase4

    FOR  ${i}   IN RANGE  10  20  2
        log to console  ${i}    Error

    END

TestCase5

    ${items}    create list  1  2   3   4   5   6

    FOR  ${i}   IN  ${items}
        log to console  ${i}    Warn

    END
TestCase6

    @{items}    create list  1  2   3   4   5   6
    FOR  ${i}   IN  @{items}
        log to console  ${i}
        exit for loop if  ${i} == 2

    END