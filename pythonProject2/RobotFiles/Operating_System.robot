*** Settings ***
Documentation   *  Enables various operating system related tasks to be performed in the system where Robot Framework is running. *

Library    OperatingSystem


*** Test Cases ***
First Test Case
    Create Directory   Demo\\vijay
    Create File     Demo\\vijay
    #Remove File    LOG/log_file.txt
    #Remove Directory    LOG
    #File Should Exist    LOG/log_file.txt    Please create a log_file.txt

#Run System Command
    #${r}    Run    dir
    #Log    ${r}    ERROR


