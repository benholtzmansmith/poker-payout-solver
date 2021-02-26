from .solve import solve


def test_one_winner_two_losers():
    player_results = [
        {
            "player": "Taiyo",
            "net": 10,
        },
        {
            "player": "Justin",
            "net": -6,
        }
        ,
        {
            "player": "Ted",
            "net": -4,
        },
    ]

    results = solve(player_data=player_results)
    assert results == {'Taiyo': ['Justin pays 6', 'Ted pays 4']}



def test_two_winners_two_losers():
    player_results = [
        {
            "player": "Taiyo",
            "net": 10,
        },
        {
            "player": "Ben",
            "net": 6,
        },
        {
            "player": "Justin",
            "net": -3,
        }
        ,
        {
            "player": "Ted",
            "net": -13,
        },
    ]

    results = solve(player_data=player_results)
    assert results == {'Taiyo': ['Justin pays 3', 'Ted pays 7'], 'Ben': ['Ted pays 6']}



def test_two_winners_three_losers():
    player_results = [
        {
            "player": "Sen",
            "net": -11,
        },
        {
            "player": "Taiyo",
            "net": 10,
        },
        {
            "player": "Ben",
            "net": 6,
        },
        {
            "player": "Justin",
            "net": -3,
        }
        ,
        {
            "player": "Ted",
            "net": -2,
        },
    ]

    results = solve(player_data=player_results)
    print(results)
    assert results == {'Taiyo': ['Sen pays 10'], 'Ben': ['Sen pays 1', 'Justin pays 3', 'Ted pays 2']}
