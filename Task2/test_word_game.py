from empty_word_game import WordGuessingGame

def test_word_game():
    # Test initialization with valid and invalid words
    print("Testing initialization...")
    try:
        game = WordGuessingGame("HELLO")
        print("Successfully initialized game with 'HELLO'")
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        game = WordGuessingGame("TOO")
        print("Successfully initialized game with 'TOO'")
    except ValueError as e:
        print(f"Error: {e}")
    
    try:
        game = WordGuessingGame("TOOLONG")
        print("Successfully initialized game with 'TOOLONG'")
    except ValueError as e:
        print(f"Error: {e}")
    
    # Create a game with a known target word
    game = WordGuessingGame("APPLE")
    print("\nCreated game with target word 'APPLE'")
    
    # Test unused letters before any guesses
    print("\nUnused letters before any guesses:")
    print(sorted(game.get_unused_letters()))
    
    # Make some guesses
    guesses = ["HEART", "PLANE", "APPLY", "APPLE"]
    
    for guess_word in guesses:
        print(f"\nGuessing '{guess_word}':")
        try:
            feedback = game.guess(guess_word)
            print(f"Feedback: {feedback}")
            
            # Show unused letters after this guess
            print(f"Unused letters: {sorted(game.get_unused_letters())}")
            
            # Check if the game is solved
            if game.is_solved():
                print("Congratulations! You've guessed the word!")
        except ValueError as e:
            print(f"Error: {e}")
    
    # Test invalid guess
    print("\nTesting invalid guess:")
    try:
        feedback = game.guess("XYZ")
        print(f"Feedback: {feedback}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_word_game()