'''
Simulation of War (card game)
Reference:
https://en.wikipedia.org/wiki/War_(card_game)

Approach
- generate deck 52 cards, [1-13 + ace] * 4
- each player sample 26 cards without replacement, using list()
- pop both list at index 0, compare values
- player with bigger value append both values (shuffle) into end of the list
- if equal, pop first 2 values from the list, compare the first one,
- if equal again keep repeating the pop until one is bigger than the other
- player with bigger value take all popped values (shuffle), append those values into end of the list
- repeat this game until one list is empty
'''
import random
import argparse


parser = argparse.ArgumentParser(description='simulate playing a WAR card game')
parser.add_argument('--interactive',
                    default=0,
                    type=int, 
                    help='play interactively round by round ' +
                    '| 0=run the game all by itself, 1=run the game round by round')
parser.add_argument('--verbose',
                    default=False,
                    action='store_true',
                    help='print details each game iteration or not | True or False')
args = parser.parse_args()


def main():
    '''
    Main function that runs the whole game.
    1. Initialize deck
    2. Draw top cards and compare values
    3. If values are equal, then go into battle
    4. Finish the game and return strings about which player won
    Returns:
        string: winner of the game | 'A' or 'B'
    '''
    # initialize deck
    deck = list(range(1, 15)) * 4
    random.shuffle(deck)
    player_a = deck[:len(deck)//2]
    player_b = deck[len(deck)//2:]
    while len(player_a) > 0 and len(player_b) > 0:
        if args.interactive == 1:
            args.verbose = True
            input("Press Enter to continue...")
        # draw cards
        a, b = player_a.pop(0), player_b.pop(0)
        table_cards = [a, b]
        random.shuffle(table_cards)
        if a > b:
            if args.verbose:
                print(f"A won this round: {a} > {b}")
            player_a.extend(table_cards)
        elif b > a:
            if args.verbose:
                print(f"B won this round: {b} > {a}")
            player_b.extend(table_cards)
        else:
            # battle begins because cards are equal
            while a == b and (len(player_a) > 0 and len(player_b) > 0):
                if args.verbose:
                    print(f"battle begins......a={a} vs b={b}")
                a, b = player_a.pop(0), player_b.pop(0)
                if len(player_a) == 0 or len(player_b) == 0:
                    table_cards.extend([a, b])
                    break
                a_down, b_down = player_a.pop(0), player_b.pop(0)
                table_cards.extend([a, b, a_down, b_down])
            random.shuffle(table_cards)
            if a > b:
                if args.verbose:
                    print(f"A won this battle: {a} > {b}")
                player_a.extend(table_cards)
            elif b > a:
                if args.verbose:
                    print(f"B won this battle: {b} > {a}")
                player_b.extend(table_cards)
            else:
                print(f"\nfinal battle is a draw: a={a} vs b={b}")
                print(f"{len(table_cards)} remaining cards on table: {table_cards}")
    print(f'\nplayer A cards: {len(player_a)}, ' +
          f'player B cards: {len(player_b)}')
    if len(player_a) == 0:
        return 'B'
    else:
        return 'A'


if __name__ == '__main__':
    print(f"player {main()} won the game!!! ")
