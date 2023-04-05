import pygame

pygame.init()

# Set up the display
screen = pygame.display.set_mode((640, 480))

# Load the image
image = pygame.image.load("Pieces/PieceImages/Black-Pawn.png")

# Set up the initial position of the image
image_rect = image.get_rect()
image_rect.center = (320, 240)

dragging = False

# Main game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse is clicked on the image
            if image_rect.collidepoint(event.pos):
                dragging = True
                mouse_x, mouse_y = event.pos
                offset_x = image_rect.x - mouse_x
                offset_y = image_rect.y - mouse_y
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False
        elif event.type == pygame.MOUSEMOTION:
            # Move the image if it's being dragged
            if dragging:
                mouse_x, mouse_y = event.pos
                image_rect.x = mouse_x + offset_x
                image_rect.y = mouse_y + offset_y

    # Draw everything
    screen.fill((255, 255, 255))
    screen.blit(image, image_rect)
    pygame.display.flip()