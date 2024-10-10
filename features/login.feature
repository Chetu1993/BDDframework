Feature: this is the login test feature

  @login1
  Scenario Outline: login with valid credentials
    Given i goto the login website
    And entering the username as "<username>" and password as "<password>"
    And click on the login button
    Then i should get logged in

    Examples:
    |username|password|
    | schetankumar123@gmail.com  |  chetan456      |
    | hello                      | welcome123      |
    |  nicework@123              |  chetan         |
    |   345                      |    $%^          |

  @login
  Scenario: login with invalid username and valid password
    Given i goto the login website
    And entering the invalid username as "hello@gmail.com" and valid password as "chetan456"
    And click on the login button
    Then i need to get error message

  @login
  Scenario: logging with valid username and invalid password
    Given i goto the login website
    And entering the valid username as "schetankumar123@gmail.com" and invalid password as "123456"
    And click on the login button
    Then i need to get error message

  @loginpage
  Scenario: logging with invalid credentials
    Given i goto the login website
    And entering the invalid username and invalid password as "chetan"
    And click on the login button
    Then i need to get error message

  @login
  Scenario: logging without entering the credentials
    Given i goto the login website
    And without entering the username and password into fields
    And click on the login button
    Then i need to get error message
