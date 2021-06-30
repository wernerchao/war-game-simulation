# Simulation of War (card game)
Reference:
https://en.wikipedia.org/wiki/War_(card_game)

## Approach
- generate deck 52 cards, [1-13 + ace] * 4
- each player sample 26 cards without replacement, using list()
- pop both list at index 0, compare values
- player with bigger value append both values (shuffle) into end of the list
- if equal, pop first 2 values from the list, compare the first one,
- if equal again keep repeating the pop until one is bigger than the other
- player with bigger value take all popped values (shuffle), append those values into end of the list
- repeat this game until one list is empty

## Assumptions
- after one player won all cards on the table, these cards are *shuffled* and moved to the bottom of their deck
    - shuffling cards on the table helps prevent entering an infinite loop
- during battles, only face-up cards are used to compare values. Face-down cards are not used
- ace is represented as number 14 in the simulation
- no suits are attached to any card value, only integers are used

## Usage Instructions
- make sure to have at least python3.7 installed on your system, reference: https://www.python.org/downloads/
- game by default is not interactive, and only print game results
- run the following to show available arguments:
```
python game.py --help
```

- run the following commands to play:
```
git clone https://github.com/wernerchao/war-game-simulation
cd war-game-simulation/
python3 game.py
```

- interactive play round by round *[using interactive will activate verbose]*:
```
python3 game.py --interactive 1
```

- show details of every round:
```
python3 game.py --verbose
```

## Run Without Any Installation
- gmail sign in required
- https://colab.research.google.com/drive/18OFYNOIuFm-zRZi6WouhXMTpZMKAPGJJ?usp=sharing
