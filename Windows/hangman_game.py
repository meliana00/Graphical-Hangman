import pygame
from pygame import mixer
from pygame.locals import *
from sys import exit
import random
import words
import hangman_menu

def gameOver():
    pygame.init()

    bg = pygame.image.load('images/Backgrounds/aa7a90.png')
    grey_button = pygame.image.load('images/Buttons/CGB02-grey_M_btn.png')
    purple_button = pygame.image.load('images/Buttons/CGB02-purple_M_btn.png')
    grave = pygame.image.load('images/Icons/icons8-grave-100.png')
    title = pygame.image.load('images/Text/text-1631276170342.png')
    button_text = pygame.image.load('images/Text/text-1631294245724.png')
    exit_icon = pygame.image.load('images/Icons/icons8-cross-mark-50.png')
    return_icon = pygame.image.load('images/Icons/icons8-undo-50.png')

    click_sfx = pygame.mixer.Sound('SFX/WAV/salamisound-7509291-switch-turn-one-time-toggle.wav')
    
    loss_soundtrack_list = [pygame.mixer.Sound('SFX/WAV/salamisound-1115620-sfx-appearance-loneliness.wav'),
                            pygame.mixer.Sound('SFX/WAV/salamisound-1577870-sfx-appearance-with-choir.wav'),
                            pygame.mixer.Sound('SFX/WAV/salamisound-4228125-sfx-sudden-event.wav'),
                            pygame.mixer.Sound('SFX/WAV/salamisound-4248511-sfx-space-dark-sound-with-a.wav'),
                            pygame.mixer.Sound('SFX/WAV/salamisound-4628705-sfx-sudden-event-metallic.wav'),
                            pygame.mixer.Sound('SFX/WAV/salamisound-5119146-sfx-sudden-event.wav'),
                            pygame.mixer.Sound('SFX/WAV/salamisound-5817448-sfx-space-metallic-glass.wav')]

    loss_soundtrack = random.choice(loss_soundtrack_list)
    loss_soundtrack.play()

    root = pygame.display.set_mode((730, 730))
    pygame.display.set_caption('Game Over')

    run = True
    click = False

    while run:
        root.blit(bg, (0, 0))
        root.blit(grave, (315, 100))
        root.blit(title, (201, 260))
        root.blit(grey_button, (237, 350))
        root.blit(exit_icon, (675, 10))
        root.blit(return_icon, (5, 10))

        replay_button_collide = pygame.Rect(237, 350, 256, 140)
        exit_button_collide = pygame.Rect(675, 10, 50, 50)
        return_button_collide = pygame.Rect(5, 10, 50, 50)

        mx , my = pygame.mouse.get_pos()

        if replay_button_collide.collidepoint((mx, my)):
            root.blit(purple_button, (237, 350))
            if click:
                click_sfx.play()
                game_loop() #Play Again

        elif exit_button_collide.collidepoint((mx, my)):
            if click:
                pygame.quit()
                exit()

        elif return_button_collide.collidepoint((mx, my)):
            if click:
                click_sfx.play()
                hangman_menu.main_menu()

        click = False

        root.blit(button_text, (291, 406))
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                click = True

        pygame.display.update()

    pygame.quit()

def game_loop():
    sample = words.word()
    length = len(sample)

    pygame.init()

    bg = pygame.image.load('images/Backgrounds/f2f5f3.png')
    warning_cover = pygame.image.load('images/Backgrounds/imageedit_16_9860001888.png')
    danger_cover = pygame.image.load('images/Backgrounds/imageedit_12_4983675571.png') 
    gallow = pygame.image.load('images/Gallow/gallow.png')

    heart_icon = pygame.image.load('images/Icons/icons8-heart-70.png')
    exit_icon = pygame.image.load('images/Icons/icons8-cross-mark-50.png')
    return_icon = pygame.image.load('images/Icons/icons8-undo-50.png')
    skull_icon = pygame.image.load('images/Icons/icons8-skull-70.png')
    blank_icon = pygame.image.load('images/Icons/icons8-horizontal-line-52.png')

    letter_a = pygame.image.load('images/Alphabet/icons8-a-key-50.png')
    letter_b = pygame.image.load('images/Alphabet/icons8-b-key-50.png')
    letter_c = pygame.image.load('images/Alphabet/icons8-c-key-50.png')
    letter_d = pygame.image.load('images/Alphabet/icons8-d-key-50.png')
    letter_e = pygame.image.load('images/Alphabet/icons8-e-key-50.png')
    letter_f = pygame.image.load('images/Alphabet/icons8-f-key-50.png')
    letter_g = pygame.image.load('images/Alphabet/icons8-g-key-50.png')
    letter_h = pygame.image.load('images/Alphabet/icons8-h-key-50.png')
    letter_i = pygame.image.load('images/Alphabet/icons8-i-key-50.png')
    letter_j = pygame.image.load('images/Alphabet/icons8-j-key-50.png')
    letter_k = pygame.image.load('images/Alphabet/icons8-k-key-50.png')
    letter_l = pygame.image.load('images/Alphabet/icons8-l-key-50.png')
    letter_m = pygame.image.load('images/Alphabet/icons8-m-key-50.png')
    letter_n = pygame.image.load('images/Alphabet/icons8-n-key-50.png')
    letter_o = pygame.image.load('images/Alphabet/icons8-o-key-50.png')
    letter_p = pygame.image.load('images/Alphabet/icons8-p-key-50.png')
    letter_q = pygame.image.load('images/Alphabet/icons8-q-key-50.png')
    letter_r = pygame.image.load('images/Alphabet/icons8-r-key-50.png')
    letter_s = pygame.image.load('images/Alphabet/icons8-s-key-50.png')
    letter_t = pygame.image.load('images/Alphabet/icons8-t-key-50.png')
    letter_u = pygame.image.load('images/Alphabet/icons8-u-key-50.png')
    letter_v = pygame.image.load('images/Alphabet/icons8-v-key-50.png')
    letter_w = pygame.image.load('images/Alphabet/icons8-w-key-50.png')
    letter_x = pygame.image.load('images/Alphabet/icons8-x-key-50.png')
    letter_y = pygame.image.load('images/Alphabet/icons8-y-key-50.png')
    letter_z = pygame.image.load('images/Alphabet/icons8-z-key-50.png')

    display_a = pygame.image.load('images/Alphabet/icons8-purple-a-50.png')
    display_b = pygame.image.load('images/Alphabet/icons8-purple-b-50.png')
    display_c = pygame.image.load('images/Alphabet/icons8-purple-c-50.png')
    display_d = pygame.image.load('images/Alphabet/icons8-purple-d-50.png')
    display_e = pygame.image.load('images/Alphabet/icons8-purple-e-50.png')
    display_f = pygame.image.load('images/Alphabet/icons8-purple-f-50.png')
    display_g = pygame.image.load('images/Alphabet/icons8-purple-g-50.png')
    display_h = pygame.image.load('images/Alphabet/icons8-purple-h-50.png')
    display_i = pygame.image.load('images/Alphabet/icons8-purple-i-50.png')
    display_j = pygame.image.load('images/Alphabet/icons8-purple-j-50.png')
    display_k = pygame.image.load('images/Alphabet/icons8-purple-k-50.png')
    display_l = pygame.image.load('images/Alphabet/icons8-purple-l-50.png')
    display_m = pygame.image.load('images/Alphabet/icons8-purple-m-50.png')
    display_n = pygame.image.load('images/Alphabet/icons8-purple-n-50.png')
    display_o = pygame.image.load('images/Alphabet/icons8-purple-o-50.png')
    display_p = pygame.image.load('images/Alphabet/icons8-purple-p-50.png')
    display_q = pygame.image.load('images/Alphabet/icons8-purple-q-50.png')
    display_r = pygame.image.load('images/Alphabet/icons8-purple-r-50.png')
    display_s = pygame.image.load('images/Alphabet/icons8-purple-s-50.png')
    display_t = pygame.image.load('images/Alphabet/icons8-purple-t-50.png')
    display_u = pygame.image.load('images/Alphabet/icons8-purple-u-50.png')
    display_v = pygame.image.load('images/Alphabet/icons8-purple-v-50.png')
    display_w = pygame.image.load('images/Alphabet/icons8-purple-w-50.png')
    display_x = pygame.image.load('images/Alphabet/icons8-purple-x-50.png')
    display_y = pygame.image.load('images/Alphabet/icons8-purple-y-50.png')
    display_z = pygame.image.load('images/Alphabet/icons8-purple-z-50.png')

    hang_initial = pygame.image.load('images/Gallow/gallow.png')
    hang_one = pygame.image.load('images/Gallow/hangman1.png')
    hang_two = pygame.image.load('images/Gallow/hangman2.png')
    hang_three = pygame.image.load('images/Gallow/hangman3.png')
    hang_four = pygame.image.load('images/Gallow/hangman4.png')
    hang_five = pygame.image.load('images/Gallow/hangman5.png')
    hang_six = pygame.image.load('images/Gallow/hangman6.png')

    correct_guess_sfx = pygame.mixer.Sound('SFX/WAV/salamisound-3884350-sfx-collect-gather-10.wav')
    false_guess_sfx = pygame.mixer.Sound('SFX/WAV/salamisound-8299642-sfx-collect-gather-1.wav')
    click_sfx = pygame.mixer.Sound('SFX/WAV/salamisound-7509291-switch-turn-one-time-toggle.wav')
    next_level_sfx = pygame.mixer.Sound('SFX/WAV/salamisound-1583857-sfx-jump-4-game-computer.wav')

    root = pygame.display.set_mode((730, 730))
    pygame.display.set_caption('HANGMAN')

    run = True
    click = False
    chosen = '-1'
    visible_letters = []
    cnt = 0
    hang = 0

    while run:
        root.blit(bg, (0, 0))
        root.blit(gallow, (10, 100))

        root.blit(heart_icon, (210, 10))
        root.blit(heart_icon, (290, 10))
        root.blit(heart_icon, (130, 10))
        root.blit(heart_icon, (370, 10))
        root.blit(heart_icon, (450, 10))
        root.blit(heart_icon, (530, 10))

        root.blit(exit_icon, (675, 10))
        root.blit(return_icon, (5, 10))

        blank_x = 200
        positions = []

        for i in range(length):
            root.blit(blank_icon, (blank_x, 222))
            positions.append(blank_x)
            blank_x += 54

        root.blit(letter_a, (50, 400))
        root.blit(letter_b, (100, 400))
        root.blit(letter_c, (150, 400))
        root.blit(letter_d, (200, 400))
        root.blit(letter_e, (250, 400))
        root.blit(letter_f, (300, 400))
        root.blit(letter_g, (350, 400))
        root.blit(letter_h, (400, 400))
        root.blit(letter_i, (450, 400))
        root.blit(letter_j, (500, 400))
        root.blit(letter_k, (550, 400))
        root.blit(letter_l, (600, 400))
        root.blit(letter_m, (650, 400))
        root.blit(letter_n, (50, 500))
        root.blit(letter_o, (100, 500))
        root.blit(letter_p, (150, 500))
        root.blit(letter_q, (200, 500))
        root.blit(letter_r, (250, 500))
        root.blit(letter_s, (300, 500))
        root.blit(letter_t, (350, 500))
        root.blit(letter_u, (400, 500))
        root.blit(letter_v, (450, 500))
        root.blit(letter_w, (500, 500))
        root.blit(letter_x, (550, 500))
        root.blit(letter_y, (600, 500))
        root.blit(letter_z, (650, 500))

        mx , my = pygame.mouse.get_pos()

        a_collide = pygame.Rect(50, 400, 50, 50)
        b_collide = pygame.Rect(100, 400, 50, 50)
        c_collide = pygame.Rect(150, 400, 50, 50)
        d_collide = pygame.Rect(200, 400, 50, 50)
        e_collide = pygame.Rect(250, 400, 50, 50)
        f_collide = pygame.Rect(300, 400, 50, 50)
        g_collide = pygame.Rect(350, 400, 50, 50)
        h_collide = pygame.Rect(400, 400, 50, 50)
        i_collide = pygame.Rect(450, 400, 50, 50)
        j_collide = pygame.Rect(500, 400, 50, 50)
        k_collide = pygame.Rect(550, 400, 50, 50)
        l_collide = pygame.Rect(600, 400, 50, 50)
        m_collide = pygame.Rect(650, 400, 50, 50)
        n_collide = pygame.Rect(50, 500, 50, 50)
        o_collide = pygame.Rect(100, 500, 50, 50)
        p_collide = pygame.Rect(150, 500, 50, 50)
        q_collide = pygame.Rect(200, 500, 50, 50)
        r_collide = pygame.Rect(250, 500, 50, 50)
        s_collide = pygame.Rect(300, 500, 50, 50)
        t_collide = pygame.Rect(350, 500, 50, 50)
        u_collide = pygame.Rect(400, 500, 50, 50)
        v_collide = pygame.Rect(450, 500, 50, 50)
        w_collide = pygame.Rect(500, 500, 50, 50)
        x_collide = pygame.Rect(550, 500, 50, 50)    
        y_collide = pygame.Rect(600, 500, 50, 50)
        z_collide = pygame.Rect(650, 500, 50, 50)

        exit_button_collide = pygame.Rect(675, 10, 50, 50)
        return_button_collide = pygame.Rect(5, 10, 50, 50)

        letter_display_dict = {'a': display_a, 'b': display_b, 'c': display_c, 'd': display_d, 'e': display_e, 'f': display_f, 'g': display_g, 'h': display_h,
                                'i': display_i, 'j': display_j, 'k': display_k, 'l': display_l, 'm': display_m, 'n': display_n, 'o': display_o, 'p': display_p, 
                                'q': display_q, 'r': display_r, 's': display_s, 't': display_t, 'u': display_u, 'v': display_v, 'w': display_w, 'x': display_x, 
                                'y': display_y, 'z': display_z}

        hangman_display_dict = {0: hang_initial, 1: hang_one, 2: hang_two, 3: hang_three, 4: hang_four, 5: hang_five, 6: hang_six}

        chosen = '-1'

        if exit_button_collide.collidepoint((mx, my)):
            if click:
                pygame.quit()
                exit()

        elif return_button_collide.collidepoint((mx, my)):
            if click:
                click_sfx.play()
                hangman_menu.main_menu()

        if a_collide.collidepoint((mx ,my)):
            if click:
                chosen = 'a'

        elif b_collide.collidepoint((mx, my)):
            if click:
                chosen = 'b'

        elif c_collide.collidepoint((mx, my)):
            if click:
                chosen = 'c'

        elif d_collide.collidepoint((mx, my)):
            if click:
                chosen = 'd'

        elif e_collide.collidepoint((mx, my)):
            if click:
                chosen = 'e'

        elif f_collide.collidepoint((mx, my)):
            if click:
                chosen = 'f'

        elif g_collide.collidepoint((mx, my)):
            if click:
                chosen = 'g'

        elif h_collide.collidepoint((mx, my)):
            if click:
                chosen = 'h'

        elif i_collide.collidepoint((mx, my)):
            if click:
                chosen = 'i'

        elif j_collide.collidepoint((mx, my)):
            if click:
                chosen = 'j'

        elif k_collide.collidepoint((mx, my)):
            if click:
                chosen = 'k'

        elif l_collide.collidepoint((mx, my)):
            if click:
                chosen = 'l'

        elif m_collide.collidepoint((mx, my)):
            if click:
                chosen = 'm'

        elif n_collide.collidepoint((mx, my)):
            if click:
                chosen = 'n'

        elif o_collide.collidepoint((mx, my)):
            if click:
                chosen = 'o'

        elif p_collide.collidepoint((mx, my)):
            if click:
                chosen = 'p'

        elif q_collide.collidepoint((mx, my)):
            if click:
                chosen = 'q'

        elif r_collide.collidepoint((mx, my)):
            if click:
                chosen = 'r'

        elif s_collide.collidepoint((mx, my)):
            if click:
                chosen = 's'

        elif t_collide.collidepoint((mx, my)):
            if click:
                chosen = 't'

        elif u_collide.collidepoint((mx, my)):
            if click:
                chosen = 'u'

        elif v_collide.collidepoint((mx, my)):
            if click:
                chosen = 'v'

        elif w_collide.collidepoint((mx, my)):
            if click:
                chosen = 'w'

        elif x_collide.collidepoint((mx, my)):
            if click:
                chosen = 'x'

        elif y_collide.collidepoint((mx, my)):
            if click:
                chosen = 'y'

        elif z_collide.collidepoint((mx, my)):
            if click:
                chosen = 'z'

        click = False

        def findOccurrences(s, ch):
            return [i for i, letter in enumerate(s) if letter == ch]

        if chosen in sample and letter_display_dict[chosen] not in [letter_tuple[0] for letter_tuple in visible_letters]:
            correct_guess_sfx.play()

            found = findOccurrences(sample, chosen)

            for i in found:
                cnt += 1
                visible_letters.append((letter_display_dict[chosen], i))
                
            if cnt == len(sample): #WON
                next_level_sfx.play()
                game_loop()

        elif chosen != '-1' and chosen not in sample: #HANG
            false_guess_sfx.play()
            hang += 1

        if hang > 6:
            gameOver() #GAME OVER
            
        else:
            if hang == 1:
                root.blit(skull_icon, (530, 10))

            elif hang == 2:
                root.blit(skull_icon, (530, 10))
                root.blit(skull_icon, (450, 10))

            elif hang == 3:
                root.blit(skull_icon, (530, 10))
                root.blit(skull_icon, (450, 10))
                root.blit(skull_icon, (370, 10))

            elif hang == 4:
                root.blit(skull_icon, (530, 10))
                root.blit(skull_icon, (450, 10))
                root.blit(skull_icon, (370, 10))
                root.blit(skull_icon, (290, 10))
                root.blit(warning_cover, (0, 0))

            elif hang == 5:
                root.blit(skull_icon, (530, 10))
                root.blit(skull_icon, (450, 10))
                root.blit(skull_icon, (370, 10))
                root.blit(skull_icon, (290, 10))
                root.blit(skull_icon, (210, 10))
                root.blit(warning_cover, (0, 0))

            elif hang == 6:
                root.blit(skull_icon, (530, 10))
                root.blit(skull_icon, (450, 10))
                root.blit(skull_icon, (370, 10))
                root.blit(skull_icon, (290, 10))
                root.blit(skull_icon, (210, 10))
                root.blit(skull_icon, (130, 10))
                root.blit(danger_cover, (0, 0))

            root.blit(hangman_display_dict[hang], (10, 100))

        for char, i in visible_letters:
            root.blit(char, (positions[i]+1, 200))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                click = True

        pygame.display.update()

    pygame.quit()