*** Settings ***
Resource        resource.robot

Test Setup      Input New Command And Create User


*** Test Cases ***
Register With Valid Username And Password
    Input Credentials    tokatesti    salasana123
    Output Should Contain    New user registered

Register With Already Taken Username And Valid Password
    Input Credentials    testikayttaja    salasana123
    Output Should Contain    User with username testikayttaja already exists

 Register With Too Short Username And Valid Password
    Input Credentials    te    salasana123
    Output Should Contain    Invalid username

Register With Enough Long But Invald Username And Valid Password
    Input Credentials    testikayttaja2    salasana123
    Output Should Contain    Invalid username

Register With Valid Username And Too Short Password
    Input Credentials    testuser    sa12
    Output Should Contain    Invalid password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials    kolmastesti    salasana
    Output Should Contain    Invalid password


*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User    testikayttaja    testi123
