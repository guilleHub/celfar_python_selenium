Feature: Acceptance test Python selenium behave

  Scenario: Celfar has a correct title
    Given I am on the home page
     Then There is a title shown on the page
      And The title is "CelFar"
  
  Scenario: Celfar has a correct description
    Given I am on the home page
     Then There is a description shown on the page
      And The description says "Conversor de temperaturas entre grados Celcius y Fahrenheit"
  
  Scenario: User enter a valid temperature
    Given I am on the home page
     When I enter "10" in the input box
      And I click the submit button
     Then The output is "50"     
  
  Scenario: User enter a below absolute zero temperature
    Given I am on the home page
     When I enter "-274" in the input box
      And I click the submit button
     Then The output is "El valor ingresado está debajo del 0 absoluto"
  
  Scenario: User enter a long temperature
    Given I am on the home page
     When I enter "1234567" in the input box
      And I click the submit button
     Then The output is "El valor ingresado es muy largo"
  
  Scenario: User enter a non numeric value
    Given I am on the home page
     When I enter "test" in the input box
      And I click the submit button
     Then The output is "El valor ingresado no es un número (recuerde que los decimales deben expresarse con '.' y no con ',')"