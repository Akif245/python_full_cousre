from replit import clear
from bidder import logo
print(logo)

bids={}
bid_finish=False

def compare(bidding_rec):
    max=0
    winner=""
    for bidder in bidding_rec:
        bid_amt=bidding_rec[bidder]
        if bid_amt > max:
            max=bid_amt
            winner=bidder
    print(f"the Winner is {winner} with a bid of $ {bid_amt}")
  
while not bid_finish:
    name=input("Enter your name \n")
    price=int(input("Enter your bids?  \n"))
    bids[name]=price
    bid_continue=input("Are there other bidders type 'y' or 'n' \n")


    if bid_continue=="n":
        compare(bids)         
        bid_finish=True

    elif bid_continue=="y":
        clear()



    






