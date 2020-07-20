import pygame
import random
import math
import time
from config import Global
G = Global()
# Initialise the directory
pygame.init()
# Creating the G.screen

# Title
pygame.display.set_caption("River Crossing")

pygame.display.set_icon(G.icon)
# Player

flag1 = 0
flag2 = 9
player1X = 490
player1Y = 736
player1X_Change = 0
player1Y_Change = 0
player1Dead = 0


player2X = 490
player2Y = 0
player2X_Change = 0
player2Y_Change = 0
player2Dead = 0


ship1X = random.randint(0, 1000)
ship1_2X = random.randint(0, 1000)
ship1_3X = random.randint(0, 1000)
ship1Y = 680
ship1X_Change = 0.4

ship2Y = 536
ship2X = random.randint(0, 1000) + random.randint(0, 1000)

ship2X_Change = 0.4
ship2_1X = random.randint(0, 1000) - random.randint(0, 1000)
ship2_2X = random.randint(0, 1000)

ship3_1X = random.randint(0, 1000) - random.randint(0, 1000)
ship3_2X = random.randint(0, 1000)
ship3Y = 420
# ship4X = 0
ship4_1X = random.randint(0, 1000) + random.randint(0, 1000)
ship4_2X = random.randint(0, 1000) - random.randint(0, 1000)
ship4Y = 292
ship5Y = 164

time2 = 0
time3 = 0
# LEVELS
level1 = 1
level2 = 1
# text
# Scores
ScoreP1 = 0
ScoreP2 = 0
# score calculator
heightP1 = 0
heightP2 = 0


def player1(x, y):
    G.screen.blit(G.player1Img, (x, y))


def player2(x, y):
    G.screen.blit(G.player2Img, (x, y))


def rock(x, y):
    G.screen.blit(G.rock1Img, (x, y))


def start(x, y):
    G.screen.blit(G.startimg, (x, y))


def finish(x, y):
    G.screen.blit(G.finishimg, (x, y))


def shipleft(x, y):
    G.screen.blit(G.ship1Img, (x, y))


def shipright(x, y):
    G.screen.blit(G.ship3Img, (x, y))


def isCollision(playerx, playery, objectx, objecty):
    distance = math.sqrt((math.pow(objectx - playerx,
                                   2)) + (math.pow(objecty - playery, 2)))
    if distance < 45:
        return True
    else:
        return False


vel = 1
player1.rect = G.player1Img.get_rect()
rock.rect = G.rock1Img.get_rect()

# Game loop

winner = G.font.render('Use Arrow Keys To Move',
                       True, (0, 0, 0), (255, 255, 255))
winnerRect = winner.get_rect()
winnerRect.center = (500, 500)
G.screen.blit(winner, winnerRect)

winner = G.font1.render('River Crossing',
                        True, (0, 0, 0), (255, 255, 255))
winnerRect = winner.get_rect()
winnerRect.center = (500, 250)
G.screen.blit(winner, winnerRect)

pygame.display.update()
pygame.time.wait(3000)


while G.running:

    G.screen.fill((0, 151, 241))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            G.running = False

# checking keystroke
    if player1Y >= 10:
        if event.type == pygame.KEYDOWN:
            # print("something pressed")
            if event.key == pygame.K_LEFT:
                player1X_Change = -vel
            # print("Left Arrow pressed")
            if event.key == pygame.K_RIGHT:
                player1X_Change = vel
            # print("Right Arrow pressed")

            if event.key == pygame.K_UP:
                player1Y_Change = -vel
                # ScoreP1 += 1
            if event.key == pygame.K_DOWN:
                player1Y_Change = vel
                # ScoreP1 -= 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player1X_Change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player1Y_Change = 0

# print("Left Arrow released")

#    player1X_Change = 0

# print("Right Arrow released")
        player1X += player1X_Change
        player1Y += player1Y_Change
    elif player2Y <= 730:
        if event.type == pygame.KEYDOWN:
            # print("something pressed")
            if event.key == pygame.K_LEFT:
                player1X_Change = -vel
                # print("Left Arrow pressed")
            if event.key == pygame.K_RIGHT:
                player1X_Change = vel
                # print("Right Arrow pressed")
            if event.key == pygame.K_UP:
                player1Y_Change = -vel
                # ScoreP2 -= 1
            if event.key == pygame.K_DOWN:
                player1Y_Change = vel
                # ScoreP2 += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player1X_Change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player1Y_Change = 0
        player2X += player1X_Change
        player2Y += player1Y_Change
        # Speed
    ship1X += ship1X_Change
    ship1_2X += ship1X_Change
    ship1_3X -= ship1X_Change
    ship2_1X += ship1X_Change
    ship2X += ship1X_Change
    ship2_2X -= ship1X_Change
    ship3_1X -= ship1X_Change
    ship3_2X -= ship1X_Change
    ship4_1X += ship1X_Change
    ship4_2X -= ship1X_Change
    # boundaries
    if player1X >= 936:
        player1X = 936
    if player1X <= 0:
        player1X = 0
    if player1Y <= 0:
        player1Y = 0
    if player1Y >= 736:
        player1Y = 736
    if player2X >= 936:
        player2X = 936
    if player2X <= 0:
        player2X = 0
    if player2Y <= 0:
        player2Y = 0
    if player2Y >= 736:
        player2Y = 736
    if ship1X >= 1000:
        ship1X = -64
    if ship1_2X >= 1000:
        ship1_2X = -64
    if ship1_3X <= -64:
        ship1_3X = 1064
    if ship2X >= 1000:
        ship2X = -64
    if ship2_1X >= 1000:
        ship2_1X = -64
    if ship2_2X <= -64:
        ship2_2X = 1064
    if ship3_1X <= -64:
        ship3_1X = 1064
    if ship3_2X <= -64:
        ship3_2X = 1064
    if ship4_1X >= 1000:
        ship4_1X = -64
    if ship4_2X <= -64:
        ship4_2X = 1064

    if player1Y >= 10:
        start(0, 736)
        finish(0, 0)
        player1(player1X, player1Y)

        time1 = pygame.time.get_ticks()
        time1 = (time1) // 1000 - time3
        if player1Y <= 10:
            time2 = time1
            if level1 == 1 and (23 - time2) > 0:
                ScoreP1 += 4 * (23 - time2)
            if level1 == 2 and (43 - time2) > 0:
                ScoreP1 += 4 * (43 - time2)
            if level1 == 3 and (63 - time2) > 0:
                ScoreP1 += 4 * (63 - time2)
            if level1 == 4 and (83 - time2) > 0:
                ScoreP1 += 4 * (83 - time2)
            if level1 == 5 and (103 - time2) > 0:
                ScoreP1 += 4 * (103 - time2)
            if level1 == 6 and (123 - time2) > 0:
                ScoreP1 += 4 * (123 - time2)
            if level1 == 7 and (143 - time2) > 0:
                ScoreP1 += 4 * (143 - time2)
            if level1 == 8 and (163 - time2) > 0:
                ScoreP1 += 4 * (163 - time2)
            if level1 == 9 and (183 - time2) > 0:
                ScoreP1 += 4 * (183 - time2)
            if level1 == 10 and (203 - time2) > 0:
                ScoreP1 += 4 * (203 - time2)
    elif player2Y <= 730:
        start(0, 0)
        finish(0, 736)
        player2(player2X, player2Y)
        time1 = pygame.time.get_ticks()
        time1 = time1 // 1000 - time2
        if player2Y >= 729:
            time3 = time1
            if level1 == 1 and (20 - time3) > 0:
                ScoreP2 += 4 * (20 - time3)
            if level1 == 2 and (40 - time3) > 0:
                ScoreP2 += 4 * (40 - time3)
            if level1 == 3 and (60 - time3) > 0:
                ScoreP2 += 4 * (60 - time3)
            if level1 == 4 and (80 - time3) > 0:
                ScoreP2 += 4 * (80 - time3)
            if level1 == 5 and (100 - time3) > 0:
                ScoreP2 += 4 * (100 - time3)
            if level1 == 6 and (120 - time3) > 0:
                ScoreP2 += 4 * (120 - time3)
            if level1 == 7 and (140 - time3) > 0:
                ScoreP2 += 4 * (140 - time3)
            if level1 == 8 and (160 - time3) > 0:
                ScoreP2 += 4 * (160 - time3)
            if level1 == 9 and (180 - time3) > 0:
                ScoreP2 += 4 * (180 - time3)
            if level1 == 10 and (200 - time3) > 0:
                ScoreP2 += 4 * (200 - time3)
# print("test")
        if player2Y >= 729:
            level1 += 0.5
            ship1X_Change = ship1X_Change + ship1X_Change * (level1) / 16
    elif player2Y > 730 or player2Dead == 1 or player1Dead == 1:
        player1X = 490
        player1Y = 736
        player1(player1X, player1Y)
        time1 = pygame.time.get_ticks()
        time1 = (time1) // 1000 - time3

        if player1Y <= 10:
            time2 = time1
        start(0, 0)
        finish(0, 736)
        player2X = 490
        player2Y = 0
        player2(player2X, player2Y)
        time1 = pygame.time.get_ticks()
        time1 = time1 // 1000 - time2
        if player2Y >= 729:
            time3 = time1

    if player1Y == 680 and flag1 == 0:
        ScoreP1 += 50
        flag1 += 1
    elif player1Y == 610 and flag1 == 1:
        ScoreP1 += 25
        flag1 += 1
    elif player1Y == 536 and flag1 == 2:
        ScoreP1 += 50
        flag1 += 1
    elif player1Y == 490 and flag1 == 3:
        ScoreP1 += 25
        flag1 += 1
    elif player1Y == 420 and flag1 == 4:
        ScoreP1 += 50
        flag1 += 1
    elif player1Y == 356 and flag1 == 5:
        ScoreP1 += 25
        flag1 += 1
    elif player1Y == 292 and flag1 == 6:
        ScoreP1 += 50
        flag1 += 1

    elif player1Y == 228 and flag1 == 7:
        ScoreP1 += 25
        flag1 += 1
    elif player1Y == 164 and flag1 == 8:
        ScoreP1 += 50
        flag1 += 1
    elif player1Y == 100 and flag1 == 9:
        ScoreP1 += 25
        flag1 += 1
    elif player1Y < ship5Y:
        flag1 = 0
    if player2Y == 680 and flag2 == 0:
        ScoreP2 += 50
        flag2 -= 1
    elif player2Y == 610 and flag2 == 1:
        ScoreP2 += 25
        flag2 -= 1
    elif player2Y == 536 and flag2 == 2:
        ScoreP2 += 50
        flag2 -= 1
    elif player2Y == 490 and flag2 == 3:
        ScoreP2 += 25
        flag2 -= 1
    elif player2Y == 420 and flag2 == 4:
        ScoreP2 += 50
        flag2 -= 1
    elif player2Y == 356 and flag2 == 5:
        ScoreP2 += 25
        flag2 -= 1
    elif player2Y == 292 and flag2 == 6:
        ScoreP2 += 50
        flag2 -= 1

    elif player2Y == 228 and flag2 == 7:
        ScoreP2 += 25
        flag2 -= 1
    elif player2Y == 164 and flag2 == 8:
        ScoreP2 += 50
        flag2 -= 1
    elif player2Y == 100 and flag2 == 9:
        ScoreP2 += 25
        flag2 -= 1
    elif player2Y > ship1Y:
        flag2 = 9
# print("test")
    if player1Dead == 1 and player2Y >= 730:
        G.running = False

    if player2Dead == 1 and player1Y <= 10:
        G.running = False
    G.font = pygame.font.Font('freesansbold.ttf', 32)
    text = G.font.render('Score Player 1 : ' + str(ScoreP1),
                         True, (0, 0, 0), (253, 217, 181))
    textRect = text.get_rect()
    textRect.center = (200, 900)
    text1 = G.font.render('Score Player 2 : ' + str(ScoreP2),
                          True, (0, 0, 0),(253, 217, 181))
    text1Rect = text1.get_rect()
    text1Rect.center = (750, 900)
    Time = G.font.render('Time : ' + str(time1),
                         True, (0, 0, 0),(253, 217, 181))
    TimeRect = Time.get_rect()
    TimeRect.center = (750, 835)
    level = G.font.render('Level : ' + str(level1),
                          True, (0, 0, 0), (253, 217, 181))
    levelRect = level.get_rect()
    levelRect.center = (90, 825)
    pygame.draw.rect(G.screen, (253, 217, 181), [0, 800, 1000, 150])
    G.screen.blit(text, textRect)
    G.screen.blit(Time, TimeRect)
    G.screen.blit(level, levelRect)
    G.screen.blit(text1, text1Rect)
    # layer1
    shipleft(ship1X, ship1Y)
    shipleft(ship1_2X, ship1Y)
    shipright(ship1_3X, ship1Y)
    rock(0, 610)
    rock(64, 610)
    rock(294, 610)
    rock(358, 610)
    rock(520, 610)
    rock(858, 610)
    rock(794, 610)
    if level1 >= 2:
        rock(128, 610)
        collision = isCollision(player1X, player1Y, 128, 610)
        if collision and player2Dead == 1:
            G.running = False
        elif collision:
            player1Dead = 1
            player1Y = 9
        collision = isCollision(player2X, player2Y, 128, 610)
        if collision and player1Dead == 1:
            G.running = False
        elif collision:
            player2Dead = 1
            player2Y = 736
# layer2
    shipleft(ship2X, ship2Y)
    shipleft(ship2_1X, ship2Y)
    shipright(ship2_2X, ship2Y)
    rock(128, 490)
    rock(64, 490)
    rock(422, 490)
    rock(358, 490)
    rock(570, 490)
    rock(730, 490)
    rock(794, 490)
    if level1 >= 3:
        rock(0, 490)
        collision = isCollision(player1X, player1Y, 0, 490)
        if collision and player2Dead == 1:
            G.running = False
        elif collision:
            player1Dead = 1
            player1Y = 9

        collision = isCollision(player2X, player2Y, 0, 490)
        if collision and player1Dead == 1:
            G.running = False
        elif collision:
            player2Dead = 1
            player2Y = 736
# layer3
    shipleft(ship1X, ship3Y)
    shipright(ship3_1X, ship3Y)
    shipright(ship3_2X, ship3Y)
    rock(128, 356)
    rock(64, 356)
    rock(192, 356)
    rock(422, 356)
    rock(486, 356)
    rock(570, 356)
    rock(730, 356)
    rock(794, 356)
    rock(880, 356)
    if level1 >= 4:
        rock(0, 356)
        collision = isCollision(player1X, player1Y, 0, 356)
        if collision and player2Dead == 1:
            G.running = False
        elif collision:
            player1Dead = 1
            player1Y = 9

        collision = isCollision(player2X, player2Y, 0, 356)
        if collision and player1Dead == 1:
            G.running = False
        elif collision:
            player2Dead = 1
            player2Y = 736
        shipleft(ship4_1X, ship3Y)
        collision = isCollision(player1X, player1Y, ship4_1X, ship3Y)
        if collision and player2Dead == 1:
            G.running = False
        elif collision:
            player1Dead = 1
            player1Y = 9

        collision = isCollision(player2X, player2Y, ship4_1X, ship3Y)
        if collision and player1Dead == 1:
            G.running = False
        elif collision:
            player2Dead = 1
            player2Y = 736
    # layer 4
    shipleft(ship1X, ship4Y)
    shipleft(ship4_1X, ship4Y)
    shipright(ship3_1X, ship4Y)
    shipright(ship4_2X, ship4Y)
    rock(128, 228)
    rock(64, 228)
    rock(0, 228)
    rock(422, 228)
    rock(350, 228)
    rock(570, 228)
    rock(730, 228)
    rock(794, 228)
    rock(880, 228)
    rock(286, 228)
    # layer 5
    shipleft(ship1X, ship5Y)
    shipleft(ship2_1X, ship5Y)
    shipright(ship2_2X, ship5Y)
    rock(0, 100)
    rock(64, 100)
    rock(294, 100)
    rock(358, 100)
    rock(520, 100)
    rock(858, 100)
    rock(794, 100)

    collision = isCollision(player1X, player1Y, ship1X, ship1Y)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, ship1_2X, ship1Y)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, ship1_3X, ship1Y)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, ship2X, ship2Y)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, ship2_1X, ship2Y)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, ship2_2X, ship2Y)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, ship1X, ship3Y)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9

    collision = isCollision(player1X, player1Y, ship3_1X, ship3Y)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, ship3_2X, ship3Y)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, ship1X, ship4Y)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, ship4_1X, ship4Y)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, ship3_1X, ship4Y)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, ship3_2X, ship4Y)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, ship1X, ship5Y)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, ship2_1X, ship5Y)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, ship2_2X, ship5Y)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 0, 610)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 64, 610)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 294, 610)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 358, 610)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 520, 610)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 858, 610)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 794, 610)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 64, 490)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 128, 490)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 358, 490)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 422, 490)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 570, 490)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 730, 490)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 794, 490)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 64, 356)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 192, 356)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 128, 356)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 422, 356)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 486, 356)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 570, 356)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 730, 356)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 794, 356)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 880, 356)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 0, 228)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 64, 228)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 128, 228)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 286, 228)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 350, 228)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 422, 228)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 570, 228)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 730, 228)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 794, 228)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 880, 228)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 0, 100)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 64, 100)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 294, 100)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 358, 100)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 520, 100)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 794, 100)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9
    collision = isCollision(player1X, player1Y, 858, 100)
    if collision and player2Dead == 1:
        G.running = False
    elif collision:
        player1Dead = 1
        player1Y = 9

    collision = isCollision(player2X, player2Y, ship1X, ship1Y)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, ship1_2X, ship1Y)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, ship1_3X, ship1Y)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, ship2X, ship2Y)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, ship2_1X, ship2Y)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, ship2_2X, ship2Y)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, ship1X, ship3Y)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736

    collision = isCollision(player2X, player2Y, ship3_1X, ship3Y)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, ship3_2X, ship3Y)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, ship1X, ship4Y)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, ship4_1X, ship4Y)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, ship3_1X, ship4Y)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, ship3_2X, ship4Y)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, ship1X, ship5Y)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, ship2_1X, ship5Y)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, ship2_2X, ship5Y)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 0, 610)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 64, 610)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 294, 610)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 358, 610)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 520, 610)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 858, 610)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 794, 610)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 64, 490)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 128, 490)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 358, 490)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 422, 490)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 570, 490)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 730, 490)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 794, 490)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 64, 356)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 192, 356)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 128, 356)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 422, 356)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 486, 356)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 570, 356)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 730, 356)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 794, 356)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 880, 356)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 0, 228)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 64, 228)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 128, 228)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 286, 228)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 350, 228)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 422, 228)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 570, 228)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 730, 228)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 794, 228)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 880, 228)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 0, 100)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 64, 100)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 294, 100)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 358, 100)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 520, 100)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 794, 100)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
    collision = isCollision(player2X, player2Y, 858, 100)
    if collision and player1Dead == 1:
        G.running = False
    elif collision:
        player2Dead = 1
        player2Y = 736
        # print(player2Y)
    pygame.display.update()
if G.running is False:
    pygame.draw.rect(G.screen, (255, 255, 255), [0, 0, 1000, 1000])
    if ScoreP1 > ScoreP2:
        # print("P1 wins")
        G.font = pygame.font.Font('freesansbold.ttf', 64)
        winner = G.font.render(
            'Player 1 Wins', True, (0, 0, 0), (255, 255, 255))
        winnerRect = winner.get_rect()
        winnerRect.center = (500, 500)
        G.screen.blit(winner, winnerRect)
        G.font = pygame.font.Font('freesansbold.ttf', 40)
        winner = G.font.render('Player 1 : ' +
                               str(ScoreP1), True, (0, 0, 0), (255, 255, 255))
        winnerRect = winner.get_rect()
        winnerRect.center = (200, 750)
        G.screen.blit(winner, winnerRect)
        G.font = pygame.font.Font('freesansbold.ttf', 40)
        winner = G.font.render('Player 2 : ' +
                               str(ScoreP2), True, (0, 0, 0), (255, 255, 255))
        winnerRect = winner.get_rect()
        winnerRect.center = (800, 750)
        G.screen.blit(winner, winnerRect)
    elif ScoreP2 > ScoreP1:
        # print("P1 wins")
        G.font = pygame.font.Font('freesansbold.ttf', 64)
        winner = G.font.render(
            'Player 2 Wins', True, (0, 0, 0), (255, 255, 255))
        winnerRect = winner.get_rect()
        winnerRect.center = (500, 500)
        G.screen.blit(winner, winnerRect)
        G.font = pygame.font.Font('freesansbold.ttf', 40)
        winner = G.font.render('Player 1 : ' +
                               str(ScoreP1), True, (0, 0, 0), (255, 255, 255))
        winnerRect = winner.get_rect()
        winnerRect.center = (200, 750)
        G.screen.blit(winner, winnerRect)
        G.font = pygame.font.Font('freesansbold.ttf', 40)
        winner = G.font.render('Player 2 : ' +
                               str(ScoreP2), True, (0, 0, 0), (255, 255, 255))
        winnerRect = winner.get_rect()
        winnerRect.center = (800, 750)
        G.screen.blit(winner, winnerRect)
    else:
        G.font = pygame.font.Font('freesansbold.ttf', 64)
        winner = G.font.render(' No Winner ', True, (0, 0, 0), (255, 255, 255))
        winnerRect = winner.get_rect()
        winnerRect.center = (500, 500)
        G.screen.blit(winner, winnerRect)

    pygame.display.update()
    pygame.time.wait(3500)
