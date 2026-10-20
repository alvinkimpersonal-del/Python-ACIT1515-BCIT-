# Imports to access the functions
from spotify import add_song
from spotify import record_listen
from spotify import generate_wrapped

# Loops the menu
while True:
    # Menu
    print("""
========== SPOTIFY WRAPPED ==========
1. Add a song
2. Record a listen
3. Generate Spotify Wrapped
4. Exit
=====================================""")
    
    # User input
    user_input = int(input("Enter your choice: "))
    print("=====================================")

    # Input selected
    if user_input == 1:
        add_song()
    elif user_input == 2:
        record_listen()
    elif user_input == 3:
        generate_wrapped()
    elif user_input == 4:
        print("Goodbye!")
        break
    else:
        print("INVALID! PLEASE TRY AGAIN!")
