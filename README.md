# Connect4

A simple implementation of the game connect four using Python 3. Provides a two player mode and an API for bot battles.

## Adding custom bots

User bots are looked for in the bots directory. All bots must follow these rules:

* The bot must be a class of the same name as the file
* The bot contains a `play_piece` method defined that takes in a `Board` object representing the current board, and returns an integer representing the column to play the piece on
* The bot needs to accept an initialization parameter for the color it is being assigned
* The bot needs to be initialized with a string called `name`

For example bots, refer to any of the bots in the `bots` directory.

## Playing the game

To play, run on the command line `play_game.py`. The game relies on a console that is capable of printing Unicode characters and is responsive to ANSI escape sequences. To play against a bot, run `play_game.py Hal`, where 'Hal' is the name of the bot you wish to play against.

You can also specify which player goes first, using the `-g` argument. For example,
`play_game.py -g bvh Hal` will start a game where the bot Hal plays a human player,
with the bot going first. Likewise, `play_game.py -g hvb Hal` starts a game where
the human player goes first.

To have two bots play against each other, run `play_game.py -g bvb Hal R2D2`, making sure both are defined in the bots directory. To have the bots (or humans) play multiple games, put the number of rounds as an additional command line argument. For example, `play_game.py -g bvb -n 100 Hal R2D2` play a simulation of 100 matches between Hal and R2D2.
