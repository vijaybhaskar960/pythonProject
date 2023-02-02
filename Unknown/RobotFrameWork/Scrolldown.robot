*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
ScrollingTest
    open browser    https://www.amazon.in/      chrome
    maximize browser window
#    execute javascript  window.scrollTo(1,1500)

    #scroll element into view  xpath://*[@id="db673cea-f06c-469a-a16a-2bbf1ef14f84"]/div[1]/span/a
    execute javascript  window.scrollTo(0,document.body.scrollHeight)   #end of page
    sleep   5
    execute javascript  window.scrollTo(0,-document.body.scrollHeight)  #starting of page
    sleep   2

