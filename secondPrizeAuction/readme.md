#Generalized second-price auction
## For Setup and Start
```bash
$ python3 -m venv .venv
$ source .venv/bin/activate

# Auction bids are added in the arguments 
# "bidder name,bid" separated with ","
$ python3 auction.py "John Doe,100,John Smith,500,Sara Conor,280,Martin Fowler,320"
```
## Test Cases
```bash
# Case(1): With no bidders
$ python3 auction.py

#Case(2): Bidders with zero bids
$ python3 auction.py "John Doe,0,John Smith,0,Sara Conor,0,Martin Fowler,0"

#Case(3): Bidders with negative bids
$ python3 auction.py "John Doe,-1,John Smith,-100,Sara Conor,-200,Martin Fowler,-59"

#Case(4): TieBreaker
$ python3 auction.py "John Doe,500,John Smith,500,Sara Conor,280,Martin Fowler,320"
```
## Space and Time Complexity
```bash
- "Space Complexity": O(n) -> "n" is the length of list of bidders.

- "Time Complexity":
    Using "TimeSort" algorithm to find highest bidder:
    1- Worst complexity:      O(n(log(n)))   
    2- Average complexity:    O(n(log(n)))
    3- Best complexity:       O(n)
```

