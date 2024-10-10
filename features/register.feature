Feature: Register Account functionality


  @register
  Scenario: Register with mandatory fields
    Given i navigate to Register page
    When i enter the below details in mandatory fields
    |firstname      |lastname     |telephone          |password         |confirmpassword         |
    |  chetan       | kumar       |   1234567890      |  chetan789      |    chetan789           |
    And i click on Continue button
    Then Account should get created


  @register
  Scenario: Register with all fields
    Given i navigate to Register page
    When i enter with all below fields
    |firstname      |lastname     |telephone          |password         |confirmpassword         |
    |  chetan       | kumar       |   1234567890      |  chetan789      |    chetan789           |
    And i click on Continue button
    Then Account should get created


  @register1
  Scenario: Register with a duplicate email address
    Given i navigate to Register page
    When i enter all the below mentioned fields into details field except email field
     |firstname      |lastname     |telephone          |password         |confirmpassword         |
    |  chetan       | kumar       |   1234567890      |  chetan789      |    chetan789           |
    And i enter existing account email into email field
    And i click on Continue button
    Then proper warning message with duplicate account should be displayed


  @register
  Scenario: Register without providing any details
    Given i navigate to Register page
    When i dont enter anything into the fields
    And i click on continue button
    Then proper warning message for every mandatory fields should be displayed
