# Dictionary for the songs
songs = []

# def add_song
# OUTPUT: title, artist, duration, and plays
def add_song():
    # User inputs
    titleInput = input("Enter song title: ")
    artistInput = input("Enter artist: ")
    durationMinInput = int(input("Enter duration (minutes): "))
    durationSecInput = int(input("Enter duration (seconds): "))

    # Adds song to list
    newSong = {
        "title": titleInput,
        "artist": artistInput,
        "duration": (durationMinInput*60) + durationSecInput,
        "plays": 0
    }

    songs.append(newSong)
    print("SONG SUCESSFULLY ADDED")

# def record_listen
def record_listen():
    askSongInput = input("Enter a song title: ")

    # Adds play to a song within the list
    for currentSong in songs:
        if askSongInput == currentSong["title"]:
            currentSong["plays"] += 1
            print("SONG PLAY HAS BEEN SUCESSFULLY ADDED!")
        else:
            print("THE SONG DOESN'T EXIST IN THE PLAYLIST!")

    return songs

# def generate_wrapped
def generate_wrapped():

    # Counters
    totalSongCounter = 0
    totalPlayCounter = 0
    totalListeningCounter = 0
    # Current most played song
    mostPlayed = None

    # Add songs to the counter
    for currentSong in songs:
        totalSongCounter += 1
        totalPlayCounter += currentSong["plays"]
        totalListeningCounter += currentSong["duration"] * currentSong["plays"]

        # Looks for the most played song
        if mostPlayed is None:
            mostPlayed = currentSong
        elif currentSong["plays"] > mostPlayed["plays"]:
            mostPlayed = currentSong

    if totalSongCounter > 0:
        print(f"Total Songs: {totalSongCounter}")
        print(f"Total Plays: {totalPlayCounter}")
        print(f"Total Listening Time: {totalListeningCounter // 60} minutes")

        # Checks if 'mostPlayed' has the most played song
        if mostPlayed is not None:
            print("")
            print("Your Most Played Song:")
            print(f"{mostPlayed['title']} ({mostPlayed['plays']} plays)")

    else:
        print("THERE ARE NO SONGS IN THE PLAYLIST!")

    return