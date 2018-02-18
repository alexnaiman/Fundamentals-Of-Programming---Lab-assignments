# About this assignment
We had to make choose and implement a game from a given list

The game I chose: Connect4.
The game is described [here](https://en.wikipedia.org/wiki/Connect_Four)
## Config 
You can configure the project settings from the `settings.properties` file 

You can modify:
* `ui` = oneOf(`console`, `gui`)
* `difficulty` = integer, how many moves ahead should the AI go(max - 2, it can go further but the algorithm needs a lot of refactoring)
* `width` = integer, the width of the board
* `height` = integer, the height of the boad


### Requirements (the exact problem statement)
* You will be given one of the problems below to solve.
* Use object oriented programming and layered architecture
* All modules with the exception of the UI will be covered with specification and PyUnit test cases.
* The program must protect itself against the user’s invalid input.
### BONUS POSSIBILITY (0.2P)
* In addition to the console-based user interface required, also implement a graphical user interface
(GUI) for the program.
* To receive the bonus, both user interfaces (menu-based and graphical) must use the same program
layers. You have to be able to start the application with either user interface.

We do not expect you to implement optimal play on the part of the computer player. However, it
should still employ a strategy when making its moves in order to attempt to win the game and provide
an entertaining opponent for the human player. Minimally, the computer player should make its
moves close to the area where stones have been placed, it should move to win the game whenever
possible and should block the human player’s attempts at 1-move victory, whenever possible