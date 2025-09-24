def play_game():
    # Dictionary of locations with outcome messages
    locations = {
        "forest": "You see a mysterious treasure chest.",
        "cave": "A wild animal attacks you suddenly!",
        "river": "You find a small boat that might help you escape."
    }

    print("Welcome to the Adventure Game!")
    player_name = input("What is your name, adventurer? ").strip()

    print("\nChoose your location to explore:")
    for loc in locations:
        print(f"- {loc}")

    # Get player's location choice with error handling
    location_choice = input("\nEnter your chosen location: ").lower().strip()
    if location_choice not in locations:
        print("Oops! That's not a valid location. Please restart the game and choose from the available locations.")
        return

    # Show initial outcome for chosen location
    print(f"\n{locations[location_choice]}")

    final_outcome = ""

    # Additional choice if the location is forest
    if location_choice == "forest":
        chest_options = ["open", "ignore"]
        chest_choice = input("Do you want to 'open' the chest or 'ignore' it? ").lower().strip()

        if chest_choice not in chest_options:
            print("That's not a valid option. The chest remains untouched and you leave safely.")
            final_outcome = "You left the chest alone and walked away safely."
        elif chest_choice == "open":
            final_outcome = "You opened the chest and found gold! You're rich!"
        else:
            final_outcome = "You ignored the chest and walked away safely."
    elif location_choice == "cave":
        final_outcome = "You were attacked but managed to escape with minor injuries."
    elif location_choice == "river":
        final_outcome = "You used the boat to escape safely."

    # Store summary in a tuple
    adventure_summary = (player_name, location_choice, final_outcome)

    # Display summary
    print("\n--- Adventure Summary ---")
    print(f"Player: {adventure_summary[0]}")
    print(f"Location chosen: {adventure_summary[1]}")
    print(f"Outcome: {adventure_summary[2]}")
    print("------------------------\n")

# Run the game
play_game()
