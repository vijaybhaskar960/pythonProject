*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
Frames
    open browser    https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html    chrome
    maximize browser window

    select frame    packageFrame
    click link  xpath:/html/body/main/ul/li[1]/a
    sleep   5
    unselect frame

    select frame    packageFrame
    click link  xpath://span[text()="WebDriver"]
    sleep   5
    unselect frame
