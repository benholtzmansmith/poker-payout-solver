import json

import click


def solve(player_data):
    """
    Constraint solver for poker payouts.
    """

    winners = []
    losers = []
    for player in player_data:
        if player["net"] > 0:
            winners.append(player)
        else:
            losers.append(player)
    
    def loop(rem_winners, rem_losers, acc):
        # no more winners to process, return
        if len(rem_winners) == 0:
            return acc
        else: 
            winner = rem_winners[0]
            loser = rem_losers[0]
            remaining = winner["net"] + loser["net"] # loser value is negative, so we should add
            if remaining > 0: # winner is owed more but loser is done paying
                winner["net"] = remaining
                losing_player, losing_net = loser["player"], loser["net"]
                entry = f"{losing_player} pays {abs(losing_net)}"
                acc[winner["player"]] = acc.get(winner["player"], []) + [entry]
                losers.pop(0)
            else: # winner is done, but loser owes more
                loser["net"] = remaining
                losing_player, winning_net = loser["player"], winner["net"]
                entry = f"{losing_player} pays {abs(winning_net)}"
                acc[winner["player"]] = acc.get(winner["player"], []) + [entry]
                winners.pop(0)
            loop(rem_winners, rem_losers, acc)
        return acc
    return loop(winners, losers, {})

@click.command()
@click.argument('filename')
def solve_payouts(filename):
    with open(filename) as f:
        data = json.load(f)
        print(json.dumps(solve(data), indent=4, sort_keys=True))


if __name__ == '__main__':
    solve_payouts()
