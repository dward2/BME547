## Blackjack
Write GUI code to play a simple hand of Blackjack with a single player and 
automated dealer.  The code for implementing the game is provided in a
module called `blackjack_engine`.

### Simple Blackjack Rules
* Uses a standard deck of 52 playing cards.
* The player and dealer are each dealt two cards.  The player can see both 
of their cards but only one of the dealer's cards.
* Cards are valued as follows:
  * Numbered cards have a value equivalent to their number.  
  * Face cards (Jack, Queen, King) have a value of 10.  
  * Aces have a value of 11 unless that would cause the total hand value to 
  be above 21.  In that case, the Ace has a value of 1.  
* The score of a hand is the sum of the card values in their hand.
* The goal for the player is to have a score higher than the dealer but not 
above 21.
* Play starts with the player.  The player can decide whether to take another
card ("hit") or stop where they are ("stay").
* If the player takes another card, their score is determined with the new 
card and evaluated as follows:
  * If the score goes above 21, the player immediately loses ("busts").  
  * If the score remains 21 or lower, the player has another opportunity to 
    decide to whether to hit or stay.
* The player can take as many or as few cards as they like, as long as they
remain at 21 or below.
* When the player stays, play passes to the dealer.
* The dealer reveals their hidden card.
* If the dealer's score is below 17, the dealer must take another card.
* The dealer continues to take cards until the dealer score is 17 or above.
* If the dealer score is above 21, the dealer busts and the player wins.
* If the dealer score is 17 or above, the winner is whoever has the higher
score.  The dealer wins in the event of a tie.

### Specifications
Design a GUI and associated program code that meets the following 
specifications.
* The GUI must use at least:
  * one label
  * one entry box (entered text must be used somehow by the game/code)
  * one radio button, checkbox, or dropdown box (the values of these items must
    be used somehow by the game/code)
  * two buttons  (must be linked to some command code)
* More widgets than this minimum are allowed to implement the needed GUI 
  functions.
* When the game starts, the GUI should display the initially dealt cards of the 
  player and dealer.  Remember to only show the value for one of the dealer 
  cards until the player stays.
* The GUI should allows the player to choose whether to take another card (hit) 
  or not (stay).
* When the player's turn is done, the GUI should display the value of the 
  second dealer card.
* Depending on whether the player exceeded 21 or not, the GUI should implement 
  and display the dealer's turn.  
* The GUI should display appropriate game updates (whose turn it is, who wins, 
  choices, etc.)
* When the hand is finished, the user should be given the option whether to
  play another game or to quit.
* The GUI should have a button that allows the user to quit the game at
  any time and close the window.  
* Additional GUI or game features can be added in order to use the minimum
  required widget types.

### Approach

1. Sketch out the GUI.
2. Start the code for the GUI by defining and placing the needed widgets on
the main window.
3. Follow the instructions under the "Import" heading in the `Blackjack API.md`
file for installing and importing the needed blackjack game code.
4. Review the "API" and "Using Game" sections of the `Blackjack API.md` file.
5. Text for the player and dealer cards can be obtained from 
`Blackjack.player_cards` and `Blackjack.dealer_cards`.
6. Connect your widget(s) that allows the player to decide whether to take
another card to a function using the `command` option of the widget(s).  
This function should:
   1. call the `Blackjack.deal_card_to_player()` method to give the player 
   another card.  
   2. update the GUI with information about the new card.
   3. get the player's score using `Blackjack.player_score`
   4. if the player has busted, update the GUI indicating that the player has
   lost.
7. Connect your widget(s) that allows the player to stay to a function using 
  the `command` option of the widget(s).  This function should:
   1. update the GUI to reveal the hidden card of the dealer
   2. get the dealer's score using `Blackjack.dealer_score`
   3. start a loop that has the dealer take a new card (using the 
   `Blackjack.deal_card_to_dealer()` method) if the score is
      less than 17 and not greater than 21.
   4. Update the GUI with the new cards
   5. Determine the winner and update the GUI accordingly
8. Add other needed functionality to the GUI as outlined in the specifications 
or as needed to use all of the needed widgets.
   1. Call `Blackjack.new_round_reshuffle()` to start a new hand if needed.
