*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
MouseActions
    # Right Click Action
    open browser    https://swisnl.github.io/jQuery-contextMenu/demo.html   chrome
    maximize browser window
    open context menu   //span[@class="context-menu-one btn btn-neutral"]
    sleep   4

    # Double Click Action

#    go to   https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3
#    maximize browser window
#    double click element  xpath://button[contains(text(),'Copy Text')]
#    sleep   3

    # Drag and Drop
    go to   http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html
    maximize browser window
    drag and drop   id:box6    id:box106
    sleep   3
    close all browser





