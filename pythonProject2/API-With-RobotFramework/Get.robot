*** Settings ***
Library     RequestsLibrary

*** Variables ***
${base_url}     https://reqres.in
${city}     Delhi

*** Test Cases ***
Weather
    create session  myssion     ${base_url}
    ${response}=    get request     myssion     /api/users?page=2
#    log to console      ${response.status_code}
     log to console      ${response.content}
#    log to console      ${response.headers}

# Validation

    ${status_code}  convert to string   ${response.status_code}
    should be equal     ${status_code}      200
    ${body}=        ${response.content}


