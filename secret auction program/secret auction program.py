name = input("What is your name?: ")
bid = int(input("What is your bid?: $"))
bids = {}
bids[name] = bid
more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
while more_bidders == "yes":
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bids[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
highest_bid = 0
winner = ""
for bidder in bids:
    if bids[bidder] > highest_bid:
        highest_bid = bids[bidder]
        winner = bidder

print(f"The winner is {winner} with a bid of ${highest_bid}.")
 