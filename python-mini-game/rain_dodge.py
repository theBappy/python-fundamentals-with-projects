'''Here’s the sequential task list (just the points, no extra details):

1. Setup pygame and create a window.

2.Add player rectangle at bottom.

2.Implement left/right movement with arrow keys.

Add background image.'''

'''Create falling stars (white rectangles).

Make stars move downward and remove when off screen.

Display survival timer.

Spawn stars over time with increasing difficulty.

Add collision detection between player and stars.

Show “You Lost!” message on collision.

End game after short delay.

(Optional polish) Restart option, sounds, images, better UI.'''

import pygame          # Importing pygame library to make the game
import time            # Importing time module for tracking elapsed time
import random          # Importing random module for random star positions
pygame.font.init()     # Initialize font module in pygame so we can render text

# Game window dimensions
WIDTH, HEIGHT = 800, 600  
WIN = pygame.display.set_mode((WIDTH, HEIGHT))   # Create the game window
pygame.display.set_caption("Space Dodge")        # Set the window title

# Load background image and scale it to the game window size
BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))

# Player constants
PLAYER_WIDTH = 40      # Player rectangle width
PLAYER_HEIGHT = 60     # Player rectangle height
PLAYER_VEL = 5         # Player movement speed

# Star (falling object) constants
STAR_WIDTH = 10        # Star rectangle width
STAR_HEIGHT = 20       # Star rectangle height
STAR_VEL = 3           # Star falling speed

# Font for rendering text (Comic Sans, size 30)
FONT = pygame.font.SysFont("comicsans", 30)


# Function to draw everything on the screen
def draw(player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))   # Draw the background image at (0,0)

    # Render elapsed time text and draw it on top-left corner
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))

    # Draw player as a red rectangle
    pygame.draw.rect(WIN, "yellow", player)

    # Draw each falling star as a white rectangle
    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    pygame.display.update()   # Refresh the display with all the new drawings


# Main game loop
def main():
    run = True   # Game loop running flag

    # Create player rectangle positioned at bottom of screen
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    clock = pygame.time.Clock()   # Used for controlling FPS and measuring time
    start_time = time.time()      # Record when the game started
    elapsed_time = 0              # Initialize elapsed time tracker

    star_add_increment = 2000     # Time interval (ms) before new stars appear
    star_count = 0                # Timer counter for stars

    stars = []   # List to store falling stars
    hit = False  # Boolean to check if player was hit by a star

    # Game loop
    while run:
        star_count += clock.tick(60)   # Limit game to 60 FPS & add elapsed ms to counter
        elapsed_time = time.time() - start_time   # Update how long the player survived

        # Add stars after timer passes threshold
        if star_count > star_add_increment:
            for _ in range(3):   # Add 3 stars at once
                star_x = random.randint(0, WIDTH - STAR_WIDTH)   # Random x position
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)  
                stars.append(star)   # Add star to list

            star_add_increment = max(200, star_add_increment - 50)   # Increase difficulty
            star_count = 0   # Reset star timer

        # Check for game quit events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   # If user clicks close button
                run = False
                break

        # Player movement with arrow keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:   # Move left
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:   # Move right
            player.x += PLAYER_VEL

        # Update star positions
        for star in stars[:]:   # Iterate over a copy so we can safely remove stars
            star.y += STAR_VEL   # Move star downward
            if star.y > HEIGHT:   # Remove star if it goes out of screen
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):  
                # Check if star collides with player
                stars.remove(star)
                hit = True
                break   # Exit loop since player is hit

        # If player got hit -> display "You Lost!" message and end game
        if hit:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)   # Wait 4 seconds before quitting
            break
            
        # Draw everything for this frame
        draw(player, elapsed_time, stars)

    pygame.quit()   # Quit pygame when loop ends


# Run game only if this file is executed directly
if __name__ == "__main__":
    main()
