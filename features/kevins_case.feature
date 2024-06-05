Feature: Kevins crime case

  Scenario: Making a case againest Kevin
    Given the user launches elucidat page 
    When the user presses start
    Then they should see both crime cases
    When user chooses to judge kevins case 
    When user votes Kevin is guilty
    Then user gets confirmation of choice 
    When user continues to explore the evidence 
    When user views evidence they see popup
    When user closes popup and continues to decision
    Then user lands on the you decide page & continues
    When user decides if fingerprints are reliable
    When user decides DNA is reliable
    When user decides if hair sample is reliable
    When user decides if footprint is reliable
    When user decides if confession is reliable
    When user decides if eyewitness is reliable
    When user must make final vote
    Then user sees what actually happened