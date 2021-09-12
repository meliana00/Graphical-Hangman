import pygame
from pygame.locals import *
from sys import exit
import hangman_game

pygame.init()

def credits():
    pygame.init()

    transparent_bg = pygame.image.load('images/Backgrounds/imageedit_8_6964826368.png')
    menu_bg = pygame.image.load('images/Backgrounds/WallpaperDog-20392214(1).jpg')
    credits_text = pygame.image.load('images/Backgrounds/credits(fixed)(1).png')
    title = pygame.image.load('images/Text/text-1630917000711.png')
    return_icon = pygame.image.load('images/Icons/icons8-undo-50.png')

    click_sfx = pygame.mixer.Sound('SFX/WAV/salamisound-7509291-switch-turn-one-time-toggle.wav')
    soundtrack = pygame.mixer.music.load('SFX/WAV/salamisound-2382220-church-bell-bells-ringing-at.wav')
    pygame.mixer.music.play(-1)

    root = pygame.display.set_mode((730, 730))
    pygame.display.set_caption('Credits')

    run = True
    click = False

    while run:
        root.blit(menu_bg, (0, 0))
        root.blit(transparent_bg, (0, 0))
        root.blit(credits_text, (90, 90))
        root.blit(return_icon, (10, 10))
        root.blit(title, (251.5, 20))

        return_button_collide = pygame.Rect(10, 10, 50, 50)

        mx , my = pygame.mouse.get_pos()

        if return_button_collide.collidepoint((mx, my)):
            if click:
                click_sfx.play()
                main_menu()

        click = False
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                click = True

        pygame.display.update()

    pygame.quit()


def main_menu():
    
    bg = pygame.image.load('images/Backgrounds/WallpaperDog-20392214(1).jpg')
    grey_button = pygame.image.load('images/Buttons/CGB02-grey_M_btn.png')
    blue_button = pygame.image.load('images/Buttons/CGB02-blue_M_btn.png')
    play_text = pygame.image.load('images/Text/text-1630916444275.png')
    credits_text = pygame.image.load('images/Text/text-1630917000711.png')
    quit_text = pygame.image.load('images/Text/text-1630916779674.png')

    github_icon = pygame.image.load('images/Icons/icons8-github-40.png')
    gmail_icon = pygame.image.load('images/Icons/icons8-gmail-35.png')
    github_text = pygame.image.load('images/Text/text-1631459237095.png')
    gmail_text = pygame.image.load('images/Text/text-1631459278554.png')

    click_sfx = pygame.mixer.Sound('SFX/WAV/salamisound-7509291-switch-turn-one-time-toggle.wav')
    soundtrack = pygame.mixer.music.load('SFX/WAV/game-over-danijel-zambo-main-version-02-03-1394(1).wav')
    pygame.mixer.music.play(-1)

    root = pygame.display.set_mode((730, 730))
    pygame.display.set_caption('Menu')

    run = True
    click = False

    while run:
        root.blit(bg, (0, 0))

        root.blit(grey_button, (237, 100)) #PLAY
        root.blit(grey_button, (237, 250)) #CREDITS
        root.blit(grey_button, (237, 400)) #QUIT

        root.blit(github_icon, (10, 620))
        root.blit(github_text, (52, 631))

        root.blit(gmail_icon, (12, 670))
        root.blit(gmail_text, (51, 678))

        play_collide = pygame.Rect(237, 100, 256, 140)
        credits_collide = pygame.Rect(237, 250, 256, 140)
        quit_collide = pygame.Rect(237, 400, 256, 140)

        mx, my = pygame.mouse.get_pos()

        if quit_collide.collidepoint((mx, my)):
            root.blit(blue_button, (237, 400))
            if click:
                pygame.quit()
                exit()

        elif play_collide.collidepoint((mx, my)):
            root.blit(blue_button, (237, 100))
            if click:
                click_sfx.play()
                pygame.mixer.quit()
                hangman_game.game_loop()

        elif credits_collide.collidepoint((mx, my)):
            root.blit(blue_button, (237, 250))
            if click:
                click_sfx.play()
                credits()

            
        click = False

        root.blit(play_text, (301, 145.5))
        root.blit(credits_text, (251.5, 295.5))
        root.blit(quit_text, (294, 445.5))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                click = True

        pygame.display.update()

    pygame.quit()

main_menu()