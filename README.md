# poker-payout-solver

### Command

`python poker_payouts/solve.py ./input.json`


#### Example Input


```
[
    {
        "player": "Taiyo",
        "net": 10
    },
    {
        "player": "Justin",
        "net": -6
    }
    ,
    {
        "player": "Ted",
        "net": -4
    }
]
```

#### Example Output

```
{
    "Taiyo": [
        "Justin pays 6",
        "Ted pays 4"
    ]
}
```
