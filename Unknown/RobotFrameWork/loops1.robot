*** Settings ***

*** Test Cases ***
#ForLoops:
#    FOR  ${i}  IN RANGE  1   10
#        Log to console  ${i}    Warn
#    END

#Forloopwithlist
#    ${items}    create list  1  2   3   6   9   8
#    FOR  ${i}   IN  ${items}
#        log to console  ${i}
#
#    END

forloopwithExit
    @{items}    create list  1  2   3   4   5   6
    FOR  ${i}    IN    @{items}
        log to console  ${i}
        exit for loop if  ${i}==3

    END
