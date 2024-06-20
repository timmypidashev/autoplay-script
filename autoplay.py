import pygame
import time

# Initialize pygame
pygame.init()

# Function to play and loop a track until a right-click or right arrow key is detected
def play_track_loop(track):
    # Load the sound file
    pygame.mixer.music.load(track)
    pygame.mixer.music.play(-1)  # Loop the track indefinitely

    # Start the main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:  # Right-click
                pygame.mixer.music.fadeout(1000)  # Fade out over 1 second
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:  # Right arrow key
                pygame.mixer.music.fadeout(1000)  # Fade out over 1 second
                return

        time.sleep(0.1)

# List of tracks to play
tracks = ['sfx/campfire.mp3', 'sfx/crickets.mp3', 'sfx/scratching.mp3']

# Main loop to iterate over the tracks
for track in tracks:
    play_track_loop(track)

# Quit pygame
pygame.quit()
