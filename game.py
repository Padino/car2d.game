import time
import random
import math
import pickle
import pygame
from pygame import mixer

random.seed()

# pava é bot

TITLE = "Cars 2d.run"
HEIGHT = 600
WIDTH = 800
FPS = 120
surface = pygame.display.set_mode((400,300))

spd = 5
spr = 8
time = 0

menu = Actor("menu")
billo1 = Actor("billo1")
billo2 = Actor("billo1")
billo3 = Actor("billo1")
billo4 = Actor("billo1")
billo5 = Actor("billo1")
billo6 = Actor("billo1")
billo7 = Actor("billo1")
billo8 = Actor("billo1")
p1 = Actor("spr_carb")
p2 = Actor("spr_carr")
stra = Actor("bis")
stro = Actor("bis")
stri = Actor("bis")
lamp1 = Actor("lamp1")
lamp0 = Actor("lamp1")
coin1 = Actor("coin")
coin2 = Actor("coin")
coin3 = Actor("coin")
coin4 = Actor("coin")
extral = Actor("extral")
extral1 = Actor("extral")
scudo1 = Actor("scudo")
scudo2 = Actor("scudo")
vel1 = Actor("boostv")
vel2 = Actor("boostv")
gatto = Actor('gattorato')
macnu = Actor('crate')
espos = Actor('crate')
live1 = 3
live2 = 3
p1.score = 0
p2.score = 0
stro.topright = 663, -800
stra.topright = 663, -100
stri.topright = 663, -1500
lamp1.topright = 655, -200
lamp0.topright = 655, 0
p2.topright = 530, 400
p1.topright = 410, 400
calcs = 0
time = 0
patos = 100
vp1 = 0
vp2 = 0
poin1 = 0
poin2 = 0
nb = 0
v1=5
v2=5
ricsalp2 = 0
salp2 = True
ricsalp1 = 0
salp1 = True
insal2 = 0
insal1 = 0
xsa1 = 59
xsa2 = 719
ysa1 = 550
ysa2 = 550
# 550-415
tpos2 = 0
posy2 = 0
tpos1 = 0
posy1 = 0
tcoin1 = 0
tcoin2 = 0
cascoin2 = 0
tcoin3 = 0
tcoin4 = 0
cascoin4 = 0
m1 = 0
m2 = 0
tev = 0
tev1 = 0
via = False
scrity = 380
tscu1 = 0
tscu2 = 0
imm1 = False
imm2 = False
timm1 = 0
timm2 = 0
ai = False
tve1 = 0
tve2 = 0
tiv1 = 0
tv1 = False
tiv2 = 0
vs = 10
tgat = 0
tv2 = False
spaga = False
viast = True
morte_p1 = False
morte_p2 = False
mp = False
scrim1, scrim2 = -275, -275
goy = -350
logoy = -150
deserto = False
endes = False
shop = False
cshop = True
tac = 0
oscx, oscy = 0,0
nomecar = " "
fascio = 0
negy = 50
opzy = 250
invy = 150
mons = 0
cons = 0
rtime = 0
tmo = 0
tshop = 0
camion, jeep,panda,furgone,gelati,deca,taxi,tuc,berlina,ranger = False,False,False,False,False,False,False,False,False,False
garage = False
selez = 0
selz = False
volume = 0.3
bordo = 80
altezza = 60
divis = 8
v = 8
modalita = "MULTIGIOCATORE"
xmodalita = 25
mody = 500
rimbalzo = 0
inv_rimbalzo = False
xpausa = -800
xpalaz = 0
xm,ym = 110,110
tracciamento = False
# 7000
# 13000


ostb = random.randint(225, 370)
ostc = random.randint(450, 590)
ostc2 = random.randint(450, 570)
print(ostb)
print(ostc)
print(ostc2)
macnu.topright = -100, -100
espos.topright = -100, -100

scudo1.topright = ostb, -200
scudo2.topright = ostc, -200

vel1.topright = ostb, -200
vel2.topright = ostc, -200

coin1.topright = ostc, -200
coin2.topright = ostc, -400
coin3.topright = ostb, -200
coin4.topright = ostb, -400

extral.topright = ostc, -200
extral1.topright = ostb, -200

billo3.topright = ostb, -200
billo4.topright = ostb, -180
billo2.topright = ostb, -200
billo1.topright = ostb, -180

billo5.topright = ostc2, -210
billo6.topright = ostc, -180
billo7.topright = ostc2, -200
billo8.topright = ostc, -190
menu.topright = 610,-1111
gatto.y = -200
# billo5.topright = ostc ,-200
# billo6.topright = ostc ,190
# billo7.topright = ostc ,-210
# billo8.topright = ostc ,180
print(billo5.x, billo7.x)
#animate(p2, tween='bounce_end',duration=1,pos=(0,0))

def draw():
    global shop, cshop, espos, nomecar
    screen.clear()
    if deserto == False:
        screen.fill((27, 116, 52))
    else:
        screen.fill((255, 235, 180))
    screen.blit("palazzi", (660, xpalaz))
    screen.blit("palazzi", (0, xpalaz))
    screen.blit("palazzi", (660, xpalaz-600))
    screen.blit("palazzi", (0, xpalaz-600))
    stra.draw()
    stro.draw()
    stri.draw()
    p1.draw()
    p2.draw()
    if via == True or mp == True:
        if vp1 < 3:
            screen.blit("rut", (700, 100))
        if vp1 < 2:
            screen.blit("rut", (700, 180))
        if vp1 < 1:
            screen.blit("rut", (700, 260))
        if vp2 < 3:
            screen.blit("rut", (40, 100))
        if vp2 < 2:
            screen.blit("rut", (40, 180))
        if vp2 < 1:
            screen.blit("rut", (40, 260))
        screen.blit("bus1", (5, -30))
        screen.blit("bus1", (665, -30))
        screen.blit("csalt", (710, 420))
        screen.draw.text("--", (xsa2, ysa2), fontsize=50,color=(0,0,0))
        screen.blit("csalt", (50, 420))
        screen.draw.text("--", (xsa1, ysa1), fontsize=50,color=(0,0,0))
        screen.blit("coin2", (710, 57))
        screen.draw.text(str(m2), (735, 60), fontsize=25)
        screen.blit("coin2", (50, 57))
        screen.draw.text(str(m1), (75, 60), fontsize=25)
    billo1.draw()
    billo2.draw()
    billo3.draw()
    billo4.draw()

    billo5.draw()
    billo6.draw()
    billo7.draw()
    billo8.draw()
    scudo1.draw()
    scudo2.draw()
    vel1.draw()
    vel2.draw()

    lamp0.draw()
    lamp1.draw()
    coin1.draw()
    coin2.draw()
    coin3.draw()
    coin4.draw()
    extral.draw()
    extral1.draw()
    gatto.draw()
    menu.draw()
#     screen.blit("tastomenu", (0, negy))
#     screen.blit("tastomenu", (0, opzy))
#     screen.blit("tastomenu", (0, invy))
#     screen.draw.text("NEGOZIO", (45, negy+20), fontsize=65)
#     screen.draw.text("OPZIONI", (45, opzy+20), fontsize=65)
#     screen.draw.text("GARAGE", (45, invy+20), fontsize=65)
    screen.blit("logocar", (340, logoy))
    screen.blit("spazio", (260, scrity-25+rimbalzo))
    screen.draw.text("PREMI 'SPAZIO' PER INIZIARE", (285, scrity+rimbalzo), fontsize=25, color=(0,0,0))
    screen.draw.text("Ha vinto il giocatore 2!", (260, scrim2), fontsize=40)
    screen.draw.text("Ha vinto il giocatore 1!", (260, scrim1), fontsize=40)
    screen.draw.text("GAME OVER", (280, goy), fontsize=60)
    pygame.draw.rect(surface, (19,20,16), pygame.Rect(0, mody, 300, 84))
    pygame.draw.rect(surface, (223,168,34), pygame.Rect(10, mody+10, 280, 64))
    screen.draw.text(str(modalita), (xmodalita, mody+30), fontsize=40, color=(0,0,0))

    pygame.draw.rect(surface, (19,20,16), pygame.Rect(0, negy-50, 800, 70))
    pygame.draw.rect(surface, (0,0,0), pygame.Rect(10, negy-40, 780, 50))
    screen.draw.text("NEGOZIO", (45, negy-30), fontsize=55)
    screen.draw.text("OPZIONI", (585, opzy-230), fontsize=55)
    screen.draw.text("GARAGE", (324, invy-130), fontsize=55)

    if via == True or morte_p1 == True or morte_p2 == True:
        screen.draw.text(str(round(time)), (395, 5), fontsize=30, color=(0,0,0))


    # HUB m percorsi
    if via == True or mp == True:
        screen.draw.text(str(round(poin1, 2)) + " Km", (40, 40), fontsize=20)
        screen.draw.text(str(round(poin2, 2)) + " Km", (700, 40), fontsize=20)

    if via == True:
        if imm2 == True:
            screen.blit("scudo", (p2.x-20, p2.y-18))
        if ai == False:
            if imm1 == True:
                screen.blit("scudo", (p1.x-20, p1.y-18))
    else:
        screen.blit("pausa", (xpausa,0))
        screen.draw.text("PAUSA", (xpausa+300, 100), fontsize=90)

    if shop == True:
        screen.fill((103, 53, 3))
        if cshop == True:
            screen.blit("crate", (50, 200))
            screen.blit("crate", (325, 200))
            screen.blit("crate", (600, 200))
            screen.blit("buy", (50, 370))
            screen.blit("buy", (325, 370))
            screen.blit("buy", (600, 370))
            screen.blit("coin", (145, 380))
            screen.blit("coin", (420, 380))
            screen.blit("coin", (695, 380))
            screen.blit("esc", (20,20))
            screen.blit("buy", (640, 20))
            screen.blit("coin", (735, 30))
            screen.draw.text(str(cons), (660, 35), fontsize=60)
            screen.draw.text("40", (80, 385), fontsize=60)
        else:
            if tac > 2.5:
                if fascio == 1:
                    screen.blit("fasciov", (0,-100))
                if fascio == 2:
                    screen.blit("fasciog", (0,-100))
                if fascio == 3:
                    screen.blit("fascior", (0,-100))
                screen.draw.text(str(nomecar),(macnu.x-90,400),fontsize = 60, color=(0,0,0))
                screen.blit("esc", (20,20))
        screen.draw.text("AUTOSALONE", (200, 30), fontsize=80)


    if garage == True:
        screen.fill((103, 53, 3))
        screen.draw.text("GARAGE", (260, 30), fontsize=80)
        screen.blit("esc", (20,20))
        if selz == True:
            screen.blit("spazio", (60,120))
            screen.blit("spazio", (420,120))
            screen.draw.text("Giocatore 1", (90, 135), fontsize=60)
            screen.draw.text("Giocatore 2", (450, 135), fontsize=60)
        if selez >= 1:
            screen.draw.text(str(nomecar),(espos.x-90,380),fontsize = 60)
        if selez == 1:
            if camion == True:
                screen.blit("buy", (330, 500))
                screen.draw.text("USA", (360, 515), fontsize=60)
            else:
                screen.blit("lock", (350, 450))
        if selez == 2:
            if jeep == True:
                screen.blit("buy", (330, 500))
                screen.draw.text("USA", (360, 515), fontsize=60)
            else:
                screen.blit("lock", (350, 450))
        if selez == 3:
            if panda == True:
                screen.blit("buy", (330, 500))
                screen.draw.text("USA", (360, 515), fontsize=60)
            else:
                screen.blit("lock", (350, 450))
        if selez == 4:
            if furgone == True:
                screen.blit("buy", (330, 500))
                screen.draw.text("USA", (360, 515), fontsize=60)
            else:
                screen.blit("lock", (350, 450))
        if selez == 5:
            if gelati == True:
                screen.blit("buy", (330, 500))
                screen.draw.text("USA", (360, 515), fontsize=60)
            else:
                screen.blit("lock", (350, 450))
        if selez == 6:
            if deca == True:
                screen.blit("buy", (330, 500))
                screen.draw.text("USA", (360, 515), fontsize=60)
            else:
                screen.blit("lock", (350, 450))
        if selez == 7:
            if taxi == True:
                screen.blit("buy", (330, 500))
                screen.draw.text("USA", (360, 515), fontsize=60)
            else:
                screen.blit("lock", (350, 450))
        if selez == 8:
            if berlina == True:
                screen.blit("buy", (330, 500))
                screen.draw.text("USA", (360, 515), fontsize=60)
            else:
                screen.blit("lock", (350, 450))
        if selez == 9:
            if ranger == True:
                screen.blit("buy", (330, 500))
                screen.draw.text("USA", (360, 515), fontsize=60)
            else:
                screen.blit("lock", (350, 450))
        if selez == 10:
            if tuc == True:
                screen.blit("buy", (330, 500))
                screen.draw.text("USA", (360, 515), fontsize=60)
            else:
                screen.blit("lock", (350, 450))
    macnu.draw()
    espos.draw()








def update(dt):
    global time
    global calcs
    global billo1
    global billo2
    global billo3
    global billo4
    global billo5
    global billo6
    global billo7
    global billo8
    global vp1
    global vp2
    global poin1
    global poin2
    global nb
    global ricsalp2
    global salp2
    global ricsalp1
    global salp1
    global insal2
    global insal1
    global xsa1
    global xsa2
    global ysa1
    global ysa2
    global posy2
    global tpos2
    global posy1
    global tpos1
    global tcoin1
    global tcoin2
    global cascoin2
    global tcoin3
    global tcoin4
    global cascoin4
    global m1
    global m2
    global tev
    global tev1
    global via
    global scrity
    global tscu1
    global tscu2
    global imm1
    global imm2
    global timm1
    global timm2
    global ai, vs
    global tve1
    global tve2
    global v2
    global v1
    global osts
    global osty
    global ostsd
    global ostyd
    global tv1
    global tiv1
    global tv2
    global tiv2
    global tgat, spaga, p2gat, ggat, gatto, p1gat, gp1p2, viast, menu
    global morte_p1, morte_p2, mp, scrim1, scrim2, goy, logoy
    global stra,stro,stri, deserto, endes, lamp0, lamp1
    global shop, cshop, tac, macnu, oscx,oscy, nomecar, fascio, negy, opzy, pos,mons,cons, rtime, tmo, tshop, invy
    global deca,taxi, camion,furgone,gelati,jeep,panda,berlina,tuc,ranger,selz,xpalaz
    global garage, espos, selez
    global volume,bordo,altezza,divis,v,mody,rimbalzo,inv_rimbalzo,xm,ym,tracciamento

    osty = random.randint(-200, -50)
    osts = random.randint(225, 370)
    ostyd = random.randint(-200, -50)
    ostsd = random.randint(465, 605)
    calcs = random.randint(1, 100)
    carcm = random.randint(1, 10)
    # 128x238
    rtime += 0.016
#     imm1 = True
#     poin1 = 21000000000000
#     imm2 = True
#     poin2 = 21000000000000

    if via == True:
        time = time + dt

    if via == False:
        if rimbalzo > 5:
            inv_rimbalzo = True
        if inv_rimbalzo == True:
            rimbalzo -= 0.1
        else:
            rimbalzo += 0.1
        if rimbalzo < -5:
            inv_rimbalzo = False

    # negozio

    if keyboard.escape:
        shop = False
        tac = 0
        macnu.x = -100
        macnu.y = -100
        cshop = True
        macnu = Actor('crate')
        macnu.topright = -100, -100
        garage = False
        espos.center = -100,-100
        selz = False
    if shop == True:
        if keyboard.j:
            cshop = False
            macnu.center = 400,300
        if cshop == False:
            tac += 0.016
            oscy = random.randint(-4, 4)
            oscx = random.randint(-4, 4)
        if tac < 2.5:
            if cshop == False:
                macnu.x += oscx
                macnu.y += oscy
        if tac > 2.5:
            if tac < 2.517:
                if carcm == 1:
                    macnu = Actor('camion')
                    nomecar = "CAMION"
                    fascio = 1
                    camion = True
                if carcm == 2:
                    macnu = Actor('jeep')
                    nomecar = "JEEP"
                    fascio = 1
                    jeep = True
                if carcm == 3:
                    macnu = Actor('panda')
                    nomecar = "PANDINO"
                    fascio = 1
                    panda = True
                if carcm == 4:
                    macnu = Actor('furgone')
                    nomecar = "CAMIONCINO"
                    fascio = 1
                    furgone = True
                if carcm == 5:
                    macnu = Actor('gelati')
                    nomecar = "CAMION DEI GELATI"
                    fascio = 1
                    gelati = True
                if carcm == 6:
                    macnu = Actor('deca')
                    nomecar = "DECAPPOTTABILE"
                    fascio = 2
                    deca = True
                if carcm == 7:
                    macnu = Actor('taxi')
                    nomecar = "TAXI"
                    fascio = 1
                    taxi = True
                if carcm == 8:
                    macnu = Actor('berlina')
                    nomecar = "BERLINA"
                    fascio = 1
                    berlina = True
                if carcm == 9:
                    macnu = Actor('ranger')
                    nomecar = "RANGE ROVER"
                    ranger = True
                    fascio = 1
                if carcm == 10:
                    macnu = Actor('tuc')
                    nomecar = "TUC TUC"
                    fascio = 2
                    tuc = True
                macnu.x = 400
                macnu.y = 300





    # garage

    if garage == True:
        if selez == 1:
            espos = Actor('camion')
            nomecar = "CAMION"
        if selez == 2:
            espos = Actor('jeep')
            nomecar = "JEEP"
        if selez == 3:
            espos = Actor('panda')
            nomecar = "PANDINO"
        if selez == 4:
            espos = Actor('furgone')
            nomecar = "CAMIONCINO"
        if selez == 5:
            espos = Actor('gelati')
            nomecar = "CAMION DEI GELATI"
        if selez == 6:
            espos = Actor('deca')
            nomecar = "DECAPPOTTABILE"
        if selez == 7:
            espos = Actor('taxi')
            nomecar = "TAXI"
        if selez == 8:
            espos = Actor('berlina')
            nomecar = "BERLINA"
        if selez == 9:
            espos = Actor('ranger')
            nomecar = "RANGE ROVER"
        if selez == 10:
            espos = Actor('tuc')
            nomecar = "TUC TUC"
        espos.center = 400, 300

    if selez < 1:
        selez = 1
    if selez > 10:
        selez = 10


    # deserto

    if time > 88:
        deserto = True
    if deserto == True:
        stray = stra.y
        striy = stri.y
        stroy = stro.y
        lamp0d = lamp0.y
        lamp1d = lamp1.y
        if endes == False:
            if stra.y < 0:
                stra = Actor('bised')
                stra.x = 407
                stra.y = stray
                endes = True
            if stri.y < 0:
                stri = Actor('bised')
                stri.x = 407
                stri.y = striy
                endes = True
            if stro.y < 0:
                stro = Actor('bised')
                stro.x = 407
                stro.y = stroy
                endes = True
        else:
            if stra.y < -1139:
                stra = Actor('bisedc')
                stra.x = 407
                stra.y = stray
            if stri.y < -1139:
                stri = Actor('bisedc')
                stri.x = 407
                stri.y = striy
            if stro.y < -1139:
                stro = Actor('bisedc')
                stro.x = 407
                stro.y = stroy
            if lamp0.y < 0:
                lamp0 = Actor('lamp1des')
                lamp0.x = 399
                lamp0.y = lamp0d
            if lamp1.y < 0:
                lamp1 = Actor('lamp1des')
                lamp1.x = 399
                lamp1.y = lamp1d



    # game over

    if poin1 < 0 or poin2 < 0:
        via = False
        viast = False
        if mp == False:
            menu.y = -250
            logoy = -230
        if poin1 < 0:
            morte_p1 = True
            mp = True
        if poin2 < 0:
            morte_p2 = True
            mp = True
    if morte_p1 == True or morte_p2 == True:
        if menu.y < 300:
            menu.y += 10
        if poin1 < 0:
            if scrim2< 250:
                scrim2 += 10
        if poin2 < 0:
            if scrim1 < 250:
                scrim1 += 10
        if goy < 170:
            goy += 10
        if logoy < 300:
            logoy += 10
    if vp1 >= 3 or vp2 >= 3:
        via = False
        viast = False
        if mp == False:
            menu.y = -250
            logoy = -230
        mp = True
        if vp2 >= 3:
            morte_p2 = True
            if scrim2 < 250:
                scrim2 += 10
        if vp1 >= 3:
            morte_p1 = True
            if scrim1 < 250:
                scrim1 += 10
    if keyboard.h:
        vp1 = 3



    # strada

    if viast == True:
        stra.y = stra.y + vs
        stro.y = stro.y + vs
        stri.y = stri.y + vs

        lamp0.y = lamp0.y + 3
        lamp1.y = lamp1.y + 3

        xpalaz += 3
        if xpalaz >= 600 and deserto == False:
            xpalaz = 0

    if stra.y > 950:
        stra.y = stri.y - 700
    if stro.y > 950:
        stro.y = stra.y - 700
    if stri.y > 950:
        stri.y = stro.y - 700

    if lamp0.y > 700:
        lamp0.y = -100
    if lamp1.y > 700:
        lamp1.y = -100



    # gioco

    if shop == False:
        if mp == False:
            if keyboard.space:
                via = True

    if via == True:
        v2 += 0.0002
        v1 += 0.0002
        vs += 0.0002
        menu.y -=10
        scrity -= 10
        logoy -= 10
        negy -= 10
        opzy -= 10
        invy -= 10
        mody -= 10
        if billo1.y > 600:
            if deserto == False:
                if calcs < 33:
                    billo1 = Actor("billo1")
                if calcs > 66:
                    billo1 = Actor("motorr")
                if calcs > 33:
                    if calcs < 66:
                        billo1 = Actor("bici")
            else:
                if calcs < 33:
                    billo1 = Actor("balla")
                if calcs > 66:
                    billo1 = Actor("carro")
                if calcs > 33:
                    if calcs < 66:
                        billo1 = Actor("barr")
            billo1.topright = osts, osty

        if billo2.y > 700:
            if deserto == False:
                if calcs < 33:
                    billo2 = Actor("billo1")
                if calcs > 66:
                    billo2 = Actor("motorr")
                if calcs > 33:
                    if calcs < 66:
                        billo2 = Actor("bici")
            else:
                if calcs < 33:
                    billo2 = Actor("balla")
                if calcs > 66:
                    billo2 = Actor("motcc")
                if calcs > 33:
                    if calcs < 66:
                        billo2 = Actor("barr")
            billo2.topright = osts, osty

        if billo3.y > 600:
            if deserto == False:
                if calcs < 33:
                    billo3 = Actor("billo1")
                if calcs > 66:
                    billo3 = Actor("motorr")
                if calcs > 33:
                    if calcs < 66:
                        billo3 = Actor("bici")
            else:
                if calcs < 33:
                    billo3 = Actor("balla")
                if calcs > 66:
                    billo3 = Actor("motcc")
                if calcs > 33:
                    if calcs < 66:
                        billo3 = Actor("barr")
            billo3.topright = osts, osty

        if billo4.y > 700:
            if deserto == False:
                if calcs < 33:
                    billo4 = Actor("billo1")
                if calcs > 66:
                    billo4 = Actor("motorr")
                if calcs > 33:
                    if calcs < 66:
                        billo4 = Actor("bici")
            else:
                if calcs < 33:
                    billo4 = Actor("balla")
                if calcs > 66:
                    billo4 = Actor("motcc")
                if calcs > 33:
                    if calcs < 66:
                        billo4 = Actor("barr")
            billo4.topright = osts, osty

        if billo5.y > 600:
            if deserto == False:
                if calcs < 33:
                    billo5 = Actor("billo1")
                if calcs > 66:
                    billo5 = Actor("motorr")
                if calcs > 33:
                    if calcs < 66:
                        billo5 = Actor("bici")
            else:
                if calcs < 33:
                    billo5 = Actor("balla")
                if calcs > 66:
                    billo5 = Actor("motcc")
                if calcs > 33:
                    if calcs < 66:
                        billo5 = Actor("barr")
            billo5.topright = ostsd, ostyd

        if billo6.y > 700:
            if deserto == False:
                if calcs < 33:
                    billo6 = Actor("billo1")
                if calcs > 66:
                    billo6 = Actor("motorr")
                if calcs > 33:
                    if calcs < 66:
                        billo6 = Actor("bici")
            else:
                if calcs < 33:
                    billo6 = Actor("balla")
                if calcs > 66:
                    billo6 = Actor("motcc")
                if calcs > 33:
                    if calcs < 66:
                        billo6 = Actor("barr")
            billo6.topright = ostsd, ostyd

        if billo7.y > 600:
            if deserto == False:
                if calcs < 33:
                    billo7 = Actor("billo1")
                if calcs > 66:
                    billo7 = Actor("motorr")
                if calcs > 33:
                    if calcs < 66:
                        billo7 = Actor("bici")
            else:
                if calcs < 33:
                    billo7 = Actor("balla")
                if calcs > 66:
                    billo7 = Actor("motcc")
                if calcs > 33:
                    if calcs < 66:
                        billo7 = Actor("barr")
            billo7.topright = ostsd, ostyd

        if billo8.y > 700:
            if deserto == False:
                if calcs < 33:
                    billo8 = Actor("billo1")
                if calcs > 66:
                    billo8 = Actor("motorr")
                if calcs > 33:
                    if calcs < 66:
                        billo8 = Actor("bici")
            else:
                if calcs < 33:
                    billo8 = Actor("balla")
                if calcs > 66:
                    billo8 = Actor("motcc")
                if calcs > 33:
                    if calcs < 66:
                        billo8 = Actor("barr")
            billo8.topright = ostsd, ostyd

        billo1.y = billo1.y + v1
        if time > 5:
            billo2.y = billo2.y + v1
        if time > 30:
            billo3.y = billo3.y + v1
        if time > 88:
            billo4.y = billo4.y + v1

        #     nb += 0.01
        billo5.y = billo5.y + v2
        if time > 5:
            billo6.y = billo6.y + v2
        if time > 30:
            billo7.y = billo7.y + v2
        if time > 88:
            billo8.y = billo8.y + v2

        # monete

        tcoin1 += 1
        if coin1.y > 600:
            if tcoin1 > 300:
                coin1.y = ostyd
                coin1.x = ostsd
                tcoin1 = 0
                tcoin2 = 0
        coin1.y += 5
        if p2.y < coin1.y + 40:
            if p2.y > coin1.y - 40:
                if p2.x < coin1.x + 40:
                    if p2.x > coin1.x - 40:
                        coin1.y = 620
                        poin2 = poin2 + 0.25
                        tcoin1 = 0
                        tcoin2 = 0
                        m2 = m2 + 1

        tcoin2 += 1
        if tcoin2 > 100:
            if tcoin2 < 102:
                cascoin2 = random.randint(0, 2)
        if cascoin2 == 1:
            if coin2.y > 600:
                if tcoin2 > 300:
                    coin2.y = ostyd
                    coin2.x = ostsd
                    tcoin2 = 0
        coin2.y += 5
        if p2.y < coin2.y + 40:
            if p2.y > coin2.y - 40:
                if p2.x < coin2.x + 40:
                    if p2.x > coin2.x - 40:
                        coin2.y = 620
                        poin2 = poin2 + 0.25
                        tcoin2 = 0
                        m2 = m2 + 1

        tcoin3 += 1
        if coin3.y > 600:
            if tcoin3 > 300:
                coin3.y = osty
                coin3.x = osts
                tcoin3 = 0
                tcoin4 = 0
        coin3.y += 5
        if p1.y < coin3.y + 40:
            if p1.y > coin3.y - 40:
                if p1.x < coin3.x + 40:
                    if p1.x > coin3.x - 40:
                        coin3.y = 620
                        poin1 = poin1 + 0.25
                        tcoin3 = 0
                        tcoin3 = 0
                        m1 = m1 + 1

        tcoin4 += 1
        if tcoin2 > 100:
            if tcoin2 < 102:
                cascoin4 = random.randint(0, 2)
        if cascoin4 == 1:
            if coin4.y > 600:
                if tcoin4 > 300:
                    coin4.y = osty
                    coin4.x = osts
                    tcoin4 = 0
        coin4.y += 5
        if p1.y < coin4.y + 40:
            if p1.y > coin4.y - 40:
                if p1.x < coin4.x + 40:
                    if p1.x > coin4.x - 40:
                        coin4.y = 620
                        poin1 = poin1 + 0.25
                        tcoin4 = 0
                        m1 = m1 + 1

    # gatto
        ggat = random.randint(1,100)
        gp1p2 = random.randint(1,2)
        p2gat = random.randint(465,605)
        p1gat = random.randint(225,370)
        tgat += 0.016
        if tgat > 5:
            if ggat == 69:
                spaga = True
                if gp1p2 == 1:
                    gatto.x = p1gat
                else:
                    gatto.x = p2gat
                gatto.y = -200
            tgat = 0
        if spaga == True:
            gatto.y += 7
        if p1.y < gatto.y + 40:
            if p1.y > gatto.y - 40:
                if p1.x < gatto.x + 40:
                    if p1.x > gatto.x - 40:
                        m1 = m1 + 100
                        spaga = False
                        gatto.y = -100

        if p2.y < gatto.y + 40:
            if p2.y > gatto.y - 40:
                if p2.x < gatto.x + 40:
                    if p2.x > gatto.x - 40:
                        m2 = m2 + 100
                        spaga = False
                        gatto.y = -100

    # boost velocita
        tve1 += 1
        if tve1 > 1100:
            vel1.y += 10
            if vel1.y > 700:
                vel1.x = osts
                vel1.y = osty
                tve1 = 0
        if p1.y < vel1.y + 40:
            if p1.y > vel1.y - 40:
                if p1.x < vel1.x + 40:
                    if p1.x > vel1.x - 40:
                        vel1.y = 800
                        v2 = v2+4
                        tv1= True
        if tv1 == True:
                tiv1 += 1
                if tiv1 > 300:
                    tv1 = False
                    tiv1 = 0
                    v2 = v2-4

        tve2 += 1
        if tve2 > 1100:
            vel2.y += 10
            if vel2.y > 700:
                vel2.x = ostsd
                vel2.y = ostyd
                tve2 = 0
        if p2.y < vel2.y + 40:
            if p2.y > vel2.y - 40:
                if p2.x < vel2.x + 40:
                    if p2.x > vel2.x - 40:
                        vel2.y = 800
                        v1 = v1+4
                        tv2= True
        if tv2 == True:
                tiv2 += 1
                if tiv2 > 300:
                    tv2 = False
                    tiv2 = 0
                    v1 = v1-4

    # vite extra
        if vp1 < 0:
            vp1 = 0
            poin2 = poin2 + 0.5
            m2 = m2 + 2
        if vp2 < 0:
            vp2 = 0
            poin1 = poin1 + 0.5
            m1 = m1 + 2
        tev += 1
        if tev > 2000:
            extral.y += 10
            if extral.y > 700:
                extral.x = ostsd
                extral.y = ostyd
                tev = 0
        if p2.y < extral.y + 40:
            if p2.y > extral.y - 40:
                if p2.x < extral.x + 40:
                    if p2.x > extral.x - 40:
                        vp1 = vp1 - 1
                        extral.y = 800

        tev1 += 1
        if tev1 > 2000:
            extral1.y += 10
            if extral1.y > 700:
                extral1.x = osts
                extral1.y = osty
                tev1 = 0
        if p1.y < extral1.y + 40:
            if p1.y > extral1.y - 40:
                if p1.x < extral1.x + 40:
                    if p1.x > extral1.x - 40:
                        vp2 = vp2 - 1
                        extral1.y = 800




        # macchine

        if ai == False:
            if keyboard.w:
                p1.angle = 0
                p1.y -= spd
            if keyboard.s:
                p1.angle = 0
                p1.y += spd
            if keyboard.a:
                p1.angle = 20
                p1.x -= spd
            else:
                p1.angle = 0
            if keyboard.d:
                p1.angle = -20
                p1.x += spd
        if keyboard.up:
            p2.angle = 0
            p2.y -= spd
        if keyboard.down:
            p2.angle = 0
            p2.y += spd
        if keyboard.left:
            p2.angle = 20
            p2.x -= spd
        else:
            p2.angle = 0
        if keyboard.right:
            p2.x += spd
            p2.angle = -20

        # bordi
        if p2.x > 600:
            p2.x = 599
            p2.angle = 0
        if p2.x < 445:
            p2.x = 446
            p2.angle = 0

        if p1.x > 370:
            p1.x = 369
            p1.angle = 0
        if p1.x < 225:
            p1.x = 226
            p1.angle = 0

        if p1.y < 45:
            p1.y = 44
            p1.angle = 0
        if p1.y > 560:
            p1.y = 559
            p1.angle = 0

        if p2.y < 45:
            p2.y = 44
            p2.angle = 0
        if p2.y > 560:
            p2.y = 559
            p2.angle = 0

        if keyboard.T:
            print(round(time))

        if keyboard.P:
            print(billo1.y)

        if keyboard.M:
            print(p1.x)

        # salto
        ricsalp2 = ricsalp2 + 1
        ysa2 = 550 - (ricsalp2/ 3.7)

        if salp2 == True:
            ysa2 = 415

        if ricsalp2 > 500:
            salp2 = True

        if salp2 == True:
            if keyboard.rshift:
                p2.y = p2.y - 150
                salp2 = False
                ysa2 = 550
                ricsalp2 = 0


        ricsalp1 = ricsalp1 + 1
        ysa1 = 550 - (ricsalp1/ 3.7)

        if salp1 == True:
            ysa1 = 415

        if ricsalp1 > 500:
            salp1 = True

        if salp1 == True:
            if keyboard.f:
                p1.y = p1.y - 150
                ricsalp1 = 0
                salp1 = False
                ysa1 = 550

        # hitbox
        if imm2 == False:
            if p2.y < billo5.y + 40:
                if p2.y > billo5.y - 40:
                    if p2.x < billo5.x + 40:
                        if p2.x > billo5.x - 40:
                            billo5.x = ostsd
                            billo5.y = ostyd
                            vp1 = vp1 + 1
                            poin2 = poin2 - 0.1
            if p2.y < billo6.y + 40:
                if p2.y > billo6.y - 40:
                    if p2.x < billo6.x + 40:
                        if p2.x > billo6.x - 40:
                            billo6.x = ostsd
                            billo6.y = ostyd
                            vp1 = vp1 + 1
                            poin2 = poin2 - 0.1
            if p2.y < billo7.y + 40:
                if p2.y > billo7.y - 40:
                    if p2.x < billo7.x + 40:
                        if p2.x > billo7.x - 40:
                            billo7.x = ostsd
                            billo7.y = ostyd
                            vp1 = vp1 + 1
                            poin2 = poin2 - 0.1
            if p2.y < billo8.y + 40:
                if p2.y > billo8.y - 40:
                    if p2.x < billo8.x + 40:
                        if p2.x > billo8.x - 40:
                            billo8.x = ostsd
                            billo8.y = ostyd
                            vp1 = vp1 + 1
                            poin2 = poin2 - 0.1

        if imm1 == False:
            if p1.y < billo1.y + 40:
                if p1.y > billo1.y - 40:
                    if p1.x < billo1.x + 40:
                        if p1.x > billo1.x - 40:
                            billo1.x = osts
                            billo1.y = osty
                            vp2 = vp2 + 1
                            poin1 = poin1 - 0.1
            if p1.y < billo2.y + 40:
                if p1.y > billo2.y - 40:
                    if p1.x < billo2.x + 40:
                        if p1.x > billo2.x - 40:
                            billo2.x = osts
                            billo2.y = osty
                            vp2 = vp2 + 1
                            poin1 = poin1 - 0.1
            if p1.y < billo3.y + 40:
                if p1.y > billo3.y - 40:
                    if p1.x < billo3.x + 40:
                        if p1.x > billo3.x - 40:
                            billo3.x = osts
                            billo3.y = osty
                            vp2 = vp2 + 1
                            poin1 = poin1 - 0.1
            if p1.y < billo4.y + 40:
                if p1.y > billo4.y - 40:
                    if p1.x < billo4.x + 40:
                        if p1.x > billo4.x - 40:
                            billo4.x = osts
                            billo4.y = osty
                            vp2 = vp2 + 1
                            poin1 = poin1 - 0.1
        if vp1 == 3:
            print("gg")

        #     print(" ")
        # se i punti sono negativi game over
        poin1 = float(poin1) + 0.001
        poin2 = float(poin2) + 0.001
        #    if poin2 > 1000:
        #         poin2 = poin2/1000

    # anticamp
        tpos2 += 1
        if tpos2 > 300:
            if tpos2 < 302:
                posy2 = p2.x
        if tpos2 > 500:
            if p2.x == posy2:
                poin2 -= 0.004
            else:
                tpos2 = 0
        #     print(tpos2)
        #     print(posy2)

        tpos1 += 1
        if tpos1 > 300:
            if tpos1 < 302:
                posy1 = p1.x
        if tpos1 > 500:
            if p1.x == posy1:
                poin1 -= 0.004
            else:
                tpos1 = 0

    # scudi

        tscu1 += 1
        if tscu1 > 1300:
            scudo1.y += 10
            if scudo1.y > 700:
                scudo1.x = osts
                scudo1.y = osty
                tscu1 = 0
        if p1.y < scudo1.y + 40:
            if p1.y > scudo1.y - 40:
                if p1.x < scudo1.x + 40:
                    if p1.x > scudo1.x - 40:
                        scudo1.y = 800
                        imm1 = True
        if imm1 == True:
            timm1 += 1
            if timm1 > 300:
                imm1 = False
                timm1 = 0

        tscu2 += 1
        if tscu2 > 1300:
            scudo2.y += 10
            if scudo2.y > 700:
                scudo2.x = ostsd
                scudo2.y = ostyd
                tscu2 = 0
        if p2.y < scudo2.y + 40:
            if p2.y > scudo2.y - 40:
                if p2.x < scudo2.x + 40:
                    if p2.x > scudo2.x - 40:
                        scudo2.y = 800
                        imm2 = True
        if imm2 == True:
            timm2 += 1
            if timm2 > 300:
                imm2 = False
                timm2 = 0







    # ai

        if keyboard.i:
            ai = True
        if ai == True:
            print("ai")
            imm1 = True
            if billo1.y > p1.y-altezza:
                if p1.x > billo1.x:
                    if p1.x < billo1.x+bordo:
                        p1.x += v
                        print("HH1")
                else:
                    if p1.x >= billo1.x-bordo:
                        p1.x -= v
                        print("HHdd1")
            if billo2.y > p1.y-altezza:
                if p1.x > billo2.x:
                    if p1.x < billo2.x+bordo:
                        p1.x += v
                        print("HH2")
                else:
                    if p1.x >= billo2.x-bordo:
                        p1.x -= v
                        print("HHdd2")
            if billo3.y > p1.y-altezza:
                if p1.x > billo3.x:
                    if p1.x < billo3.x+bordo:
                        p1.x += v
                        print("HH3")
                else:
                    if p1.x >= billo3.x-bordo:
                        p1.x -= v
                        print("HHdd3")
            if billo4.y > p1.y-altezza:
                if p1.x > billo4.x:
                    if p1.x < billo4.x+bordo:
                        p1.x += v
                        print("HH4")
                else:
                    if p1.x >= billo4.x-bordo:
                        p1.x -= v
                        print("HHdd4")
            if p1.x > 260:
                p1.x -= 1
            else:
                p1.x += 1

            if p1.y < 500:
                p1.y += 1

            if billo1.y > p1.y-altezza/divis:
                if p1.x < billo1.x+bordo and p1.x >= billo1.x:
                    saltoo()
                if p1.x > billo1.x-bordo and p1.x < billo1.x:
                    saltoo()
            if billo2.y > p1.y-altezza/divis :
                if p1.x < billo2.x+bordo and p1.x >= billo2.x:
                    saltoo()
                if p1.x > billo2.x-bordo and p1.x < billo2.x:
                    saltoo()
            if billo3.y > p1.y-altezza/divis:
                if p1.x < billo3.x+bordo and p1.x >= billo3.x:
                    saltoo()
                if p1.x > billo3.x-bordo and p1.x < billo3.x:
                    saltoo()
            if billo4.y > p1.y-altezza/divis:
                if p1.x < billo4.x+bordo and p1.x >= billo4.x:
                    saltoo()
                if p1.x > billo4.x-bordo and p1.x < billo4.x:
                    saltoo()


         #         \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\   600 445





        #     if billo5.y > p2.y -80:
#                 if billo5.y < p2.y +20:
#                     if billo5.x > p2.x-60 :
#                         if billo5.x < p2.x:
#                             p2.x += 6
#                     if billo5.x < p2.x+60:
#                         if billo5.x > p2.x:
#                             p2.x -= 6

#             else:
#                 if billo5.x > p2.x-60:
#                     pass
#                 else:
#                     if p2.x > 523:
#                         p2.x -= 2
#                     if p2.x < 523:
#                         p2.x += 2
#                 if billo5.x < p2.x+60:
#                     pass
#                 else:
#                     if p2.x > 523:
#                         p2.x -= 2
#                     if p2.x < 523:
#                         p2.x += 2



#             if billo6.y > p2.y -80:
#                 if billo6.y < p2.y +20:
#                     if billo6.x > p2.x-60 :
#                         if billo6.x < p2.x:
#                             p2.x += 6
#                     if billo6.x < p2.x+60:
#                         if billo6.x > p2.x:
#                             p2.x -= 6
#             else:
#                 if billo6.x > p2.x-60:
#                     pass
#                 else:
#                     if p2.x > 523:
#                         p2.x -= 2
#                     if p2.x < 523:
#                         p2.x += 2
#                 if billo6.x < p2.x+60:
#                     pass
#                 else:
#                     if p2.x > 523:
#                         p2.x -= 2
#                     if p2.x < 523:
#                         p2.x += 2


#             if billo7.y > p2.y -80:
#                 if billo7.y < p2.y +20:
#                     if billo7.x > p2.x-60 :
#                         if billo7.x < p2.x:
#                             p2.x += 6
#                     if billo7.x < p2.x+60:
#                         if billo7.x > p2.x:
#                             p2.x -= 6
#             else:
#                 if billo7.x > p2.x-60:
#                     pass
#                 else:
#                     if p2.x > 523:
#                         p2.x -= 2
#                     if p2.x < 523:
#                         p2.x += 2
#                 if billo7.x < p2.x+60:
#                     pass
#                 else:
#                     if p2.x > 523:
#                         p2.x -= 2
#                     if p2.x < 523:
#                         p2.x += 2


#             if billo8.y > p2.y -80:
#                 if billo8.y < p2.y +20:
#                     if billo8.x > p2.x-60:
#                         if billo8.x < p2.x:
#                             p2.x += 6
#                     if billo8.x < p2.x+60:
#                         if billo8.x > p2.x:
#                             p2.x -= 6
#             else:
#                 if billo8.x > p2.x-60:
#                     pass
#                 else:
#                     if p2.x > 523:
#                         p2.x -= 2
#                     if p2.x < 523:
#                         p2.x += 2
#                 if billo8.x < p2.x+60:
#                     pass
#                 else:
#                     if p2.x > 523:
#                         p2.x -= 2
#                     if p2.x < 523:
#                         p2.x += 2

#             if billo5.y > p2.y -50:
#                 if billo5.x > p2.x-40 :
#                     if billo5.x < p2.x+40:
#                         if salp2 == True:
#                             ricsalp2 = 0
#                             salp2 = False
#                             ysa2 = 550
#                             p2.y = p2.y - 150
#             if billo6.y > p2.y -50:
#                 if billo6.x > p2.x-40 :
#                     if billo6.x < p2.x+40:
#                         if salp2 == True:
#                             ricsalp2 = 0
#                             salp2 = False
#                             ysa2 = 550
#                             p2.y = p2.y - 150
#             if billo7.y > p2.y -50:
#                 if billo7.x > p2.x-40 :
#                     if billo7.x < p2.x+40:
#                         if salp2 == True:
#                             ricsalp2 = 0
#                             salp2 = False
#                             ysa2 = 550
#                             p2.y = p2.y - 150
#             if billo8.y > p2.y -50:
#                 if billo8.x > p2.x-40 :
#                     if billo8.x < p2.x+40:
#                         if salp2 == True:
#                             ricsalp2 = 0
#                             salp2 = False
#                             ysa2 = 550
#                             p2.y = p2.y - 150
#             if p2.y < 460:
#                 p2.y += 2
    # tracciatore
    if via == False:
        if keyboard.left:
            if keyboard.right:
                tracciamento = True
    else:
        if tracciamento == True:
            if p2.x > xm:
                p2.x -= spd
                p2.angle = 20
            if p2.x == xm:
                p2.angle = 0
            if p2.x < xm:
                p2.x += spd
                p2.angle = -20
            if p2.y < ym:
                p2.y += spd
            if p2.y > ym:
                p2.y -= spd





    #Salvataggi

    if mp == False:
        if ai == False:
            mons = m1 + m2
        else:
            mons = m2

    if mp == True:
        tmo += 1
        if tmo < 2:
            cons = cons + mons
            with open("save.pkl", "wb") as f:
             cons = pickle.dump(cons, f)


    if rtime < 0.017:
        with open("save.pkl", "rb") as f:
           cons = pickle.load(f)

    if tac > 2.5:
        if tac < 2.517:
            with open("auto", "wb") as f:
                pickle.dump(taxi, f)
                pickle.dump(deca, f)
                pickle.dump(camion, f)
                pickle.dump(furgone, f)
                pickle.dump(gelati, f)
                pickle.dump(jeep, f)
                pickle.dump(panda, f)
                pickle.dump(tuc, f)
                pickle.dump(ranger, f)
                pickle.dump(berlina, f)

    with open("auto", "rb") as f:
       taxi = pickle.load(f)
       deca = pickle.load(f)
       camion = pickle.load(f)
       furgone = pickle.load(f)
       gelati = pickle.load(f)
       jeep = pickle.load(f)
       panda = pickle.load(f)
       tuc = pickle.load(f)
       ranger = pickle.load(f)
       berlina = pickle.load(f)

# reset

    if keyboard.b:
        taxi = False
        deca = False
        camion = False
        furgone = False
        gelati = False
        jeep = False
        panda = False
        tuc = False
        ranger = False
        berlina = False
        with open("auto", "wb") as f:
                pickle.dump(taxi, f)
                pickle.dump(deca, f)
                pickle.dump(camion, f)
                pickle.dump(furgone, f)
                pickle.dump(gelati, f)
                pickle.dump(jeep, f)
                pickle.dump(panda, f)
                pickle.dump(tuc, f)
                pickle.dump(ranger, f)
                pickle.dump(berlina, f)


    if keyboard.m:
        cons = 1
        with open("save.pkl", "wb") as f:
            cons = pickle.dump(cons, f)
        with open("save.pkl", "rb") as f:
           cons = pickle.load(f)

#     print(deca,taxi)

def on_mouse_down(pos, button):
    global shop, cshop, macnu, mons, cons,garage, espos,selz,selez,p1,p2,tac,fascio,modalita,xmodalita,ai
    x,y = pos
    print(x,y)
    if via == False:
        if shop == False:
            if garage == False:
                if x > 30 and x < 230:
                    if y > 15 and y < 55:
                        shop = True
            if x > 300 and x < 500:
                if y > 15 and y < 55:
                    garage = True
        else:
            if cshop == True:
                if x > 25 and x < 120:
                    if y > 20 and y < 100:
                        shop = False
                        tac = 0
                        macnu.x = -100
                        macnu.y = -100
                        cshop = True
                        macnu = Actor('crate')
                        macnu.topright = -100, -100
                # costo
                if cons >= 40:
                    if x > 50 and x < 200:
                            if y > 370 and y < 430:
                                cshop = False
                                macnu.center = 400,300
                                cons = cons-40
                                with open("save.pkl", "wb") as f:
                                    cons = pickle.dump(cons, f)
                                with open("save.pkl", "rb") as f:
                                   cons = pickle.load(f)


        if garage == True:
            if x > 25 and x < 120:
                    if y > 20 and y < 100:
                        garage = False
                        espos.center = -100,-100
                        selz = False

            if x > 330 and x < 480:
                    if y > 500 and y < 560:
                        if selez == 1:
                            if camion == True:
                                selz = True
                        if selez == 2:
                            if jeep == True:
                                selz = True
                        if selez == 3:
                            if panda == True:
                                selz = True
                        if selez == 4:
                            if furgone == True:
                                selz = True
                        if selez == 5:
                            if gelati == True:
                                selz = True
                        if selez == 6:
                            if deca == True:
                                selz = True
                        if selez == 7:
                            if taxi == True:
                                selz = True
                        if selez == 8:
                            if berlina == True:
                                selz = True
                        if selez == 9:
                            if ranger == True:
                                selz = True
                        if selez == 10:
                            if tuc == True:
                                selz = True
            if selz == True:
                if x > 60 and x < 360:
                    if y > 120 and y < 180:
                        if selez == 1:
                            p1 = Actor('camion')
                        if selez == 2:
                            p1 = Actor('jeep')
                        if selez == 3:
                            p1 = Actor('panda')
                        if selez == 4:
                            p1= Actor('furgone')
                        if selez == 5:
                            p1 = Actor('gelati')
                        if selez == 6:
                            p1 = Actor('deca')
                        if selez == 7:
                            p1 = Actor('taxi')
                        if selez == 8:
                            p1 = Actor('berlina')
                        if selez == 9:
                            p1 = Actor('ranger')
                        if selez == 10:
                            p1 = Actor('tuc')
                        selz = False
                        p1.topright = 410, 400
                if x > 420 and x < 720:
                    if y > 120 and y < 180:
                        if selez == 1:
                            p2 = Actor('camion')
                        if selez == 2:
                            p2 = Actor('jeep')
                        if selez == 3:
                            p2 = Actor('panda')
                        if selez == 4:
                            p2= Actor('furgone')
                        if selez == 5:
                            p2 = Actor('gelati')
                        if selez == 6:
                            p2 = Actor('deca')
                        if selez == 7:
                            p2 = Actor('taxi')
                        if selez == 8:
                            p2 = Actor('berlina')
                        if selez == 9:
                            p2 = Actor('ranger')
                        if selez == 10:
                            p2 = Actor('tuc')
                        selz = False
                        p2.topright = 530, 400
        if shop == True:
            if cshop == False:
                if x > 25 and x < 120:
                    if y > 20 and y < 100:
                        tac = 0
                        macnu.x = -100
                        macnu.y = -100
                        cshop = True
                        macnu = Actor('crate')
                        macnu.topright = -100, -100
                        fascio = 0

        if modalita == "MULTIGIOCATORE":
            if x > 5 and x < 300:
                if y > 500 and y < 580:
                    xmodalita = 95
                    modalita = "SINGOLO"
                    ai = True
        else:
            if x > 5 and x < 300:
                if y > 500 and y < 580:
                    xmodalita = 25
                    modalita = "MULTIGIOCATORE"
                    ai = False







#city_mus = mixer.music.load('music\City-Plus.oga')
#mixer.music.play(-1)

def on_key_down(key):
    global selez,selz,time,via,xpausa,viast
    if selz == False:
        if key == keys.RIGHT:
            selez = selez + 1
        if key == keys.LEFT:
            selez = selez - 1

    if time > 0:
        if via == True:
            if key == keys.ESCAPE:
                via = False
                viast = False
                xpausa = 0
        else:
            if key == keys.ESCAPE:
                via = True
                viast = True
                xpausa = -800

def saltoo():
    global salp1,ricsalp1,ysa1
    if salp1 == True:
        p1.y = p1.y - 150
        ricsalp1 = 0
        salp1 = False
        ysa1 = 550

def on_mouse_move(pos):
    global xm,ym
    xm,ym = pos








#     print(tpos2)
#     print(posy2)
         #    if billo8.y > p2.y -80:
#                 if billo8.y < p2.y +20:
#                     if billo8.x > p2.x-60:
#                         if billo8.x < p2.x:
#                             p2.x += 6
#                             if billo8.y > p2.y -60:
#                                 if billo8.y < p2.y:
#                                     p2.x -= 10
#                     if billo8.x < p2.x+60:
#                         if billo8.x > p2.x:
#                             p2.x -= 6
#                             if billo8.y > p2.y -60:
#                                 if billo8.y < p2.y:
#                                     p2.x += 1




# if billo1.y > p1.y -15:
#                 if billo1.x > p1.x-10 :
#                     p1.x += 3
#                 if billo1.x < p1.x+10:
#                     p1.x -= 3
#             if billo2.y > p1.y -15:
#                 if billo2.x > p1.x-10 :
#                     p1.x += 3
#                 if billo2.x < p1.x+10:
#                     p1.x -= 3
#             if billo3.y > p1.y -15:
#                 if billo3.x > p1.x-10 :
#                     p1.x += 3
#                 if billo3.x < p1.x+10:
#                     p1.x -= 3
#             if billo4.y > p1.y -15:
#                 if billo4.x > p1.x-10 :
#                     p1.x += 3
#                 if billo4.x < p1.x+10:
#                     p1.x -= 3



