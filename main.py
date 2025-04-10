# Pygame game template

import pygame
import sys
import config # Import the config module
import shapes

def init_game ():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def draw_text(screen, font_pose, text='No text', font_size=10, font_name='DejaVuSans.ttf', font_color= (0,0,0), italic=False, bold=False):
    pygame.font.init()
    font = pygame.font.Font(font_name, font_size)
    font.set_italic(italic)
    font.set_bold(bold)
    img = font.render(text, False, font_color)
    screen.blit(img, font_pose)

def handle_events (button):
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            return False
        if events.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(events.pos):
                pygame.quit()
                sys.exit()
        elif events.type == pygame.KEYDOWN:
            if events.key == pygame.K_ESCAPE:
                return False
    return True
def main():
    screen = init_game()
    clock = pygame.time.Clock() # Initialize the clock here

    font = pygame.font.SysFont('Georgia', 40, bold=True)
    surf = font.render('Button', True, config.BLACK)

    button_length = 200
    button_width = 60
    button_x = 300
    button_y = 125
    button = pygame.Rect(button_x,button_y,button_length,button_width)

    surf_rect = surf.get_rect()
    surf_rect.center = button.center

    running = True
    while running:
        running = handle_events(button)
        screen.fill(config.WHITE) # Use color from config
        
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if button.collidepoint(mouse_x, mouse_y):
            button_color = (180,180,180)
        else:
            button_color = (110,110,110)

        pygame.draw.rect(screen, button_color, button)

        screen.blit(surf,surf_rect)

        pygame.display.flip()
        
        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS) # Use the clock to control the frame rate

        

    pygame.quit()

    sys.exit()

if __name__ == "__main__":
    main()
