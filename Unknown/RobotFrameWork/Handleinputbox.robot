*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${browser}  chrome
${url}  https://www.amazon.in/

*** Test Cases ***
TestInputBoxes
    open browser  ${url}    ${browser}
    title should be  Online Shopping site in India: Shop Online for Mobiles, Books, Watches, Shoes and More - Amazon.in
    click link  id:nav-link-accountList
    ${"emali_text"}  set variable  id:ap_email

    element should be visible   ${"emali_text"}
    element should be enabled   ${"emali_text"}

    input text  ${"emali_text"}  8074517920
    sleep    5
    clear element text  ${"emali_text"}
    sleep   3
    close browser

*** Keywords ***
