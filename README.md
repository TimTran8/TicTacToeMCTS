# TicTacToe MCTS
Implemented pure Monte-Carlo Tree Search (MCTS) in Python where it only makes moves based on a defined number of playouts. It then selects the move that resulted in the most wins.

It will win or draw every time the computer (O) goes first against the player (X). However when the playergoes first and they are "smart", such as doing the fork situation, the player may win. This is because without a predefined given knowledge to the computer, it won't be able to detect it is being trapped before it is too late. This is forbidden in the case of the requirements for the assignment.

## How to Run
```
python3 TicTacToe.py
```
