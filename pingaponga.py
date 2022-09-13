from pygame import *
from GameSprite import GameSprite
from Player import *



def main():
    clock = time.Clock()
    FPS = 60

    font.init()
    font1 = font.SysFont('Arial', 35)
    win = font1.render('YOU WIN!',True,(255,255,255))
    lose = font1.render('YOU LOSE!',True,(180,0,0))

    image_player = 'platform.jpeg'
    image_ball = 'ball.jpeg'
    win_back = 'fon2.png'

    win_width = 900
    win_height = 600

    window = display.set_mode((win_width,win_height))
    display.set_caption('Пипонг')

    background = transform.scale(image.load(win_back),(win_width,win_height))

    game = True

    Platform_left = Player(image_player,5,win_height-350,50,100,10,win_width,win_height,window)
    Platform_right = Player(image_player,845,win_height-350,50,100,10,win_width,win_height,window)

    while game:
        for e in event.get():
            if e.type == QUIT:
                game = False

        window.blit(background,(0,0))

        Platform_left.reset()
        Platform_right.reset()

        Platform_left.movement1()
        Platform_right.movement2()

        display.update()

        clock.tick(FPS)

main()