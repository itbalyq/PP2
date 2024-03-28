import pygame

pygame.init()
pygame.mixer.init()
pygame.display.init()

screen = pygame.display.set_mode((500, 500))
done = True

BLACK = (0, 0, 0)
v = 0.6
pygame.mixer.music.load('piano.mp3')
pygame.mixer.music.set_volume(v)
pygame.mixer.music.play()

musics = ['piano.mp3', 'la_la_land.mp3', 'rick_roll.mp3']

pygame.display.set_caption("Music")
cnt = 0

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.pause()
            if event.key == pygame.K_RETURN:
                pygame.mixer.music.unpause()
            if event.key == pygame.K_LEFT:
                if cnt == 0:
                    cnt = 2
                    pygame.mixer.music.load(musics[cnt])
                    pygame.mixer.music.play()
                else:
                    cnt -= 1
                    pygame.mixer.music.load(musics[cnt])
                    pygame.mixer.music.play()
            if event.key == pygame.K_RIGHT:
                if cnt == 2:
                    cnt = 0
                    pygame.mixer.music.load(musics[cnt])
                    pygame.mixer.music.play()
                else:
                    cnt += 1
                    pygame.mixer.music.load(musics[cnt])
                    pygame.mixer.music.play()
            if event.key == pygame.K_UP:
                v += 0.2
                pygame.mixer.music.set_volume(v)
            if event.key == pygame.K_DOWN:
                v -= 0.2
                pygame.mixer.music.set_volume(v)

    screen.fill(BLACK)
    pygame.time.delay(10)

    pygame.display.flip()