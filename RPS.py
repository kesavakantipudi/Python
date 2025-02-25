import random 

print("Rules")
print("1. Press Enter to start the game ")
print("2. Enter 'exit' to quit the game at at any point")
print("3. Enter the valid input to the game either in upper or lower case")
print("\nWelcome to Rock, Paper, Scissors!")
print("Let's play Rock, Paper, Scissors!")
choices = ['rock', 'paper', 'sissor']
ply = input('Enter to play').lower()
while ply != 'exit':
    choic = random.choice(choices)

    print("Enter you choice from - 1. Rock, 2. Paper, 3. Sissor : ", end= " ")
    user_choice = input().lower()
    
    if user_choice == 'exit':
        print("Exiting the game...")
        break

    if user_choice not in ['rock', 'paper', 'sissor']:
        print("Invalid choice. Please enter a valid number.")
        
        
    if user_choice == choic:
        print('Its a Tie..!')
        
    elif user_choice == 'rock' and choic == 'sissor' or user_choice == 'paper' and choic == 'rock' or user_choice == 'sissor' and choic == 'paper':
        print('You Win!!')
    else:
        print('You Lose!!')

    print(f'Computer choice: {choic}, your choice: {user_choice}')
    
