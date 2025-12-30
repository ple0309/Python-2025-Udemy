import random
from art import logo, vs
from game_data import data

def random_choice(list_data):
    return random.choice(list_data)

def next_choice(data_a, list_data):
    new_data = random.choice(list_data)
    while new_data == data_a:
        new_data = random.choice(list_data)
    return new_data

data_1 = random_choice(data)
data_2 = random_choice(data)
final_score = 0
should_continue = True

while should_continue:
    print("\n" * 20)
    print(logo)
    if final_score > 0:
        print(f"You're right! Current score: {final_score}.")
    print(f"Compare A: {data_1['name']}, a {data_1['description']}, from {data_1['country']}.")
    print(vs)
    print(f"Against B: {data_2['name']}, a {data_2['description']}, from {data_2['country']}.")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if (choice == 'A' and data_1['follower_count'] > data_2['follower_count']) or \
        (choice == 'B' and data_1['follower_count'] < data_2['follower_count']):
            final_score += 1
    else:
        should_continue = False
    data_1 = data_2
    data_2 = next_choice(data_1, data)

print("\n" * 20)
print(logo)
print(f"Sorry, that's wrong. Final score: {final_score}.")
