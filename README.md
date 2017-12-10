# Connect4

A simple implementation of the game connect four using Python 3. Provides a two player mode and an API for bot battles.

## Adding custom bots

User bots are looked for in the bots directory. All bots must follow these rules:

* The bot must be a class of the same name as the file
* The bot contains a `play_piece` method defined that takes in a `Board` object representing the current board, and returning an integer representing the column to play the piece on
* The bot needs to be initialized with a name

For an example bot, refer to Hal in the bots directory.

## Playing the game

To play, run on the command line `play_game.py`. The game relies on a console that is capable of printing Unicode characters and is responsive to ANSI escape sequences. To play against a bot, run `play_game.py Hal`, where 'Hal' is the name of the bot you wish to play against. To have two bots play against each other, run `play_game.py Hal R2D2`, making sure both are defined in the bots directory.
