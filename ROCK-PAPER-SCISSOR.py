import random

def determine_winner(user_choice, computer_choice):
    """
    Applies the game logic to determine the winner.
    Returns: 0 for a tie, 1 for user win, -1 for computer win.
    """
    if user_choice == computer_choice:
        return 0  # Tie
    
    # Logic: Rock (r) > Scissors (s), Scissors (s) > Paper (p), Paper (p) > Rock (r)
    if (user_choice == 'r' and computer_choice == 's') or \
       (user_choice == 's' and computer_choice == 'p') or \
       (user_choice == 'p' and computer_choice == 'r'):
        return 1  # User Wins
    else:
        return -1 # Computer Wins

def play_game():
    """
    Main function to run the Rock-Paper-Scissors game.
    """
    user_score = 0
    computer_score = 0
    choices = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}
    
    print("Welcome to Rock-Paper-Scissors! Choose R, P, or S.")
    
    while True:
        # --- User Input ---
        user_input = input("\nEnter your choice (r/p/s) or type 'q' to quit: ").lower().strip()
        
        if user_input == 'q':
            break

        if user_input not in choices:
            print("Invalid input. Please choose 'r' for Rock, 'p' for Paper, or 's' for Scissors.")
            continue
            
        # --- Computer Selection ---
        computer_choice = random.choice(list(choices.keys()))
        
        # Display Choices
        print(f"\nYou chose: {choices[user_input]}")
        print(f"Computer chose: {choices[computer_choice]}")
        
        # --- Game Logic ---
        result = determine_winner(user_input, computer_choice)
        
        # --- Display Result and Score Tracking ---
        if result == 1:
            print("🎉 You win this round! 🎉")
            user_score += 1
        elif result == -1:
            print("💻 Computer wins this round! 😔")
            computer_score += 1
        else:
            print("🤝 It's a tie!")

        print(f"\nCURRENT SCORE: You - {user_score} | Computer - {computer_score}")

    # Final Score and Goodbye Message
    print("\n--- GAME OVER ---")
    print(f"FINAL SCORE: You {user_score} - {computer_score} Computer")
    
    if user_score > computer_score:
        print("🥇 Congratulations! You are the overall winner! 🥇")
    elif computer_score > user_score:
        print("Better luck next time! The computer won the game. 🤖")
    else:
        print("It's an overall tie! A true battle of wits. ⚔️")
        
    print("Thanks for playing!")

# Run the game
if __name__ == "__main__":
    play_game()