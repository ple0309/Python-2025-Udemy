from art import logo

def find_highest_bidder(bids):
    winner = ""
    highest_bidder = 0
    for key in bids:
        if bids[key] > highest_bidder:
            highest_bidder = bids[key]
            winner = key
    print(f"The winner is {winner} with a bid of ${highest_bidder}")

print(logo)
print("Welcome to the secret auction program.")

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

bids = {}
continue_bidding = True
while continue_bidding:
    username = input("What is your name?: ")
    price = int(input("What's your bid?: $"))
    bids[username] = price
    choice = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if choice == "no":
        continue_bidding = False
        find_highest_bidder(bids)
    else:
        print("\n" * 20)

