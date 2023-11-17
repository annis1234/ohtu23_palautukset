*** Settings ***
Resource            resource.robot
Resource            login_resource.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username    testuser
    Set Password    password123
    Confirm Password    password123
    Submit Credentials
    Registration Should Succeed

Login After Successful Registration
    Go To Login Page
    Set Login Username    testuser
    Set Login Password    password123
    Submit Login Credentials
    Login Should Succeed

Register With Too Short Username And Valid Password
    Set Username    te
    Set Password    password123
    Confirm Password    password123
    Submit Credentials
    Registration Should Fail With Message    Invalid username

Login After Failed Registration
    Go To Login Page
    Set Login Username    te
    Set Login Password    password123
    Submit Login Credentials
    Login Should Fail With Message    Invalid username or password

Register With Valid Username And Invalid Password
    Set Username    testikayttaja
    Set Password    password
    Confirm Password    password
    Submit Credentials
    Registration Should Fail With Message    Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username    tokatesti
    Set Password    salasana222
    Confirm Password    salasana123
    Submit Credentials
    Registration Should Fail With Message    Passwords do not match


*** Keywords ***
Set Username
    [Arguments]    ${username}
    Input Text    username    ${username}

Set Password
    [Arguments]    ${password}
    Input Password    password    ${password}

Confirm Password
    [Arguments]    ${password}
    Input Password    password_confirmation    ${password}

Submit Credentials
    Click Button    Register

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]    ${message}
    Register Page Should Be Open
    Page Should Contain    ${message}
