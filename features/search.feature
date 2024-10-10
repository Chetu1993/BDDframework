Feature: Search functionality

  @search1
  Scenario: search for a valid product
    Given when i goto the search product page
    When i have entered the product "HP" in search box
    And i click on the search button
    Then valid product should be visible

  @search
  Scenario: search for a invalid product
    Given when i goto the search product page
    When i have entered the invalid "paper" product
    And i click on the search button
    Then proper message should be visible



  @search
  Scenario: searching without entering the product name
    Given when i goto the search product page
    When i dont enter anything in search box field
    And i click on the search button
    Then proper message should be visible









