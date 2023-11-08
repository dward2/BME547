# Blackjack

Instructions for using the `blackjack` module for administering a game of 
Blackjack to use with your GUI.

### Import
To use the `blackjack` module, copy the `blackjack.py` file into the same folder
as your GUI code and then include the following import statement in your GUI
code:
```python
from blackjack import Blackjack
```

### API
* `Blackjack()` 
  * Starts a new game with a player and a dealer and deals two
      cards to each.  
  * Example:
      ```python
      game = Blackjack()
      ```

* `Blackjack.player_cards`  
  `Blackjack.dealer_cards`
  * Returns a list of strings that indicate what cards are currently in the 
    player's hand or the dealer's hand  
  * Example:
      ```python
      print(game.player_cards)
      # output: ["Ace of Spades", "7 of Hearts"]
    
      print(game.dealer_cards)
      # output: ["5 of Diamonds", "8 of Clubs"]
      ```

  
* `Blackjack.player_score`  
  `Blackjack.dealer_score`
  * Returns an integer with the current score of either the player or dealer.  
  * Examples:
      ```python
      # Continuing from above example
      print(game.player_score)
      # output: 18
  
      print(game.player_score)
      # output: 13
      ```

* `Blackjack.deal_card_to_player()`  
  `Blackjack.deal_card_to_dealer()`
  * Adds a card from the deck to the hand of either the player or dealer and
    returns a string indicating what the added card was.
  * Examples:
    ```python
    new_card = game.deal_card_to_player()
    print("The new card was {}".format(new_card))
    # output:  "King of Spades"
    print(game.player_cards)
    # output: ["Ace of Spades, "7 of Hearts", "King of Spades"]
    print(game.player_score)
    # output: 18
    
    new_card = game.deal_card_to_dealer()
    print("The new card was {}".format(new_card))
    # output:  "Queen of Hearts"
    print(game.player_cards)
    # output: ["5 of Diamonds", "8 of Clubs", "Queen of Hearts"]
    print(game.player_score)
    # output: 23
    ```

* `Blackjack.new_round_reshuffle()`
  * Shuffles all cards and starts a new hand by dealing two cards each to the 
  player and dealer.  
  
### Using Game

1. Create a variable with an instance of the `Blackjack` class, such as 
`game = Blackjack()`.
2. Get the cards in each hand by using `game.player_cards` and
`game.dealer_cards`.
3. Get the scores for each hand by using `game.player_score` and 
`game.dealer_score`.
4. Display the cards to the user.  Make sure to keep the first dealer card
hidden.
5. Accept input from the user whether the player should "Hit" (take
another card) or "Stay" (keep current cards and see what the dealer has).
6. For each "Hit", use the `game.deal_card_to_player()` method to put another
card in the players hand.  If the player's score is greater than 21 after
receiving the new card, the player busts and loses.
7. While the players score stays below 21, repeat 4 through 6 until the user 
chooses to Stay.
8. Based on the dealer score, get more cards using `game.deal_card_to_dealer()`
until dealer busts (goes over 21) or has a score of 17 or greater.
