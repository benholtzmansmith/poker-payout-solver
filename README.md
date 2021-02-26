# poker-payout-solver

### Command

`python solve_payouts/solve_payouts.py ./input.json`


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
