import sys
import itertools


# Function To find the Highest Bid under the Generalized second-price auction mechanism
def findHighestBid(auction_bids):
    """
        Built-in function sorted to automatically sort it
        1- In descending way (reverse = True)
        2- Taking into consideration amount first (element[1]) then name second (element[0])
        Time Complexity : O(n logn) [Timesort Algorithm]
    """
    auction_bids = sorted(auction_bids, key=lambda element: (element[1], element[0]),reverse=True)
    print("The Bid Winner:")
    print("-----------------")

    #   Shifting the bid value to the bidder ( Generalized second-price auction )
    for (a0, _), (_, b1) in zip(auction_bids,itertools.islice(auction_bids, 1, None)):
        print("{: <20} {: <20} ".format(*(a0, b1)))

    #   Printing the lower bidder (the looser)
    print("{: <20} {: <20} ".format(*(auction_bids[len(auction_bids)-1][0], "Lost")))


# Function to check if there a valid amount or all zeros
def validateBids(auction_bids):
    for bid in range(len(auction_bids)):
        if auction_bids[bid][1] > str(0):
            return True
    return False


def unvalidatedBids():
    print("NO WINNERS")
    sys.exit()


if __name__ == "__main__":
    # Checking if there's bidders first
    try:
    # Taking the auction from the arguments as a string
        arguments = sys.argv[1]
    except:
        unvalidatedBids()
    # Splitting the string by its separator (,) using iterator for faster access
    temp = iter(arguments.split(','))
    # Convert the string into a list of tuples
    auction_bids = [(ele, next(temp)) for ele in temp]
    # Checking validity of the bids
    if not validateBids(auction_bids):
        unvalidatedBids()

    print("Input Bid is:")
    print("-------------")
    for bid in auction_bids:
        print("{: <20} {: <20}".format(*(bid[0], bid[1])))
    print("************************")

    findHighestBid(auction_bids)


