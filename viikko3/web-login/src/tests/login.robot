*** Settings ***
Resource            resource.robot
Resource            login_resource.robot

Suite Setup         Open And Configure Browser
Suite Teardown      Close Browser
Test Setup          Create User And Go To Login Page


*** Test Cases ***
Login With Correct Credentials
    Set Login Username    kalle
    Set Login Password    kalle123
    Submit Login Credentials
    Login Should Succeed

Login With Incorrect Password
    Set Login Username    kalle
    Set Login Password    kalle456
    Submit Login Credentials
    Login Should Fail With Message    Invalid username or password

Login With Nonexistent Username
    Set Login Username    testuser
    Set Login Password    password
    Submit Login Credentials
    Login Should Fail With Message    Invalid username or password


*** Keywords ***
Create User And Go To Login Page
    Create User    kalle    kalle123
    Go To Login Page
    Login Page Should Be Open
