import random
import sys

print('''
This program simulates a game where you roll a die with the following rules:
- If you roll a 6, you win $10.
- If you roll a 4 or 5, you win $5.
- If you roll a 1, 2, or 3, you pay $6.

The program will simulate a specified number of games and calculate the total amount gained, 
the total amount lost, and the net profit. It will then average the net profit over multiple simulations.

To use this program, you will be prompted to enter the number of simulations and the number of games per simulation.
''')

def simulate_game(num_games):
    # Define the outcomes and their corresponding rewards
    outcomes = {1: -6, 2: -6, 3: -6, 4: 5, 5: 5, 6: 10}
    
    # Initialize the total amounts gained and lost
    total_gained = 0
    total_lost = 0
    
    current_percentage = None
    last_percentage    = None
    
    # Simulate the games
    for i in range(num_games):
        # Roll the die
        roll = random.randint(1, 6)
        
        # Update the total gained or lost based on the outcome of the roll
        if outcomes[roll] > 0:
            total_gained += outcomes[roll]
        else:
            total_lost += abs(outcomes[roll])
            
        # Calculate the current percentage
        current_percentage = "{}%".format(int(((i+1)/num_games) * 100))
        
        # Print the current percentage if it has changed
        if current_percentage != last_percentage:
            sys.stdout.write('\rCalculating... (' + current_percentage + ')')
            sys.stdout.flush()
            last_percentage = current_percentage
    
    # Calculate the net profit
    net_profit = total_gained - total_lost
    
    # Print the total amount gained, total amount lost, and net profi
    print()
    print(f"Total amount gained: ${total_gained}")
    print(f"Total amount lost: ${total_lost}")
    print(f"Net profit after {num_games} games: ${net_profit}")
    
    return net_profit

# Run the function

# Ask the user for the number of sims and games
num_sims  = int(input("Enter the number of simulations: "))
num_games = int(input("Enter the number of games: "))

average_profit = 0

for i in range(num_sims):
    print(f"\nGame number {i + 1}:")
    average_profit += simulate_game(num_games)

average_profit = average_profit / num_sims
print(f"\nThe average profit across all simulations was ${average_profit:.2f}")