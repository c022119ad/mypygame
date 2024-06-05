import os
import csv
import sys
import time
import pygame as pg
from dataclasses import dataclass

WIDTH = 1600
HEIGHT = 1000
MAIN_DIR = os.path.split(os.path.abspath(__file__))[0]


# class Sioritext(pg.sprite.Sprite):
    
#     def __init__(self,siodata,font="hgp創英角ﾎﾟｯﾌﾟ体",size=100):
#         super().__init__()
#         self.data = siodata
#         self.font = pg.font.SysFont(font,size)
#         text = ""
#         for k,v in self.data.items():
#             text += v
#         self.image = self.font.render(text,0,(0,0,0))
#         self.rect = self.image.get_rect()
#         self.rect.x = WIDTH//2-200
#         self.rect.y = HEIGHT//2+100
#     def updata(self):
#         t = 0
#         #screen.blit(self.image, self.rect)
@dataclass 
class Chara_stats:
    """
    キャラの情報をデータクラスで管理
    """
    name:str
    job:str
    ueapon:str
    level:int
    atk:int
    def_:int
    magic:int
    magic_def:int
    spd:int
    luck:int
    chara_fig:pg.Surface




class Playbgm():
    
    def __init__(self,music,game_mode):
        self.music =music
        self.game_mode = game_mode
        pg.mixer.music.load(self.music)
        pg.mixer.music.set_volume(1)
        pg.mixer.music.play(-1)
    def updata(self,music,game_mode):
        if self.game_mode != game_mode and self.music != music:
            self.game_mode = game_mode
            self.music = music
            pg.mixer.music.pause()
            pg.mixer.music.load(self.music)
            pg.mixer.music.play(-1)
            



class Sioritext():
    count = 0
    def __init__(self,siodata,font="hgp創英角ﾎﾟｯﾌﾟ体",size=30):
        self.data = siodata
        self.font = pg.font.SysFont(font,size)
        text = ""
        for k,v in self.data.items():
            text += v
            text += " "
        self.image = self.font.render(text,0,(0,0,0))
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH//2-200
        self.rect.y = HEIGHT//2+100+150+__class__.count
        __class__.count += 30
        
    def updata(self,screen):
        screen.blit(self.image, self.rect)
        #screen.blit(self.image, self.rect)

class Cur():
    delta = {  # 押下キーと移動量の辞書
        pg.K_UP: (0, -40),
        pg.K_DOWN: (0, +40),
        pg.K_LEFT: (-40, 0),
        pg.K_RIGHT: (40, 0),
    }
    
    
    def __init__(self):
        self.img = pg.image.load(f"{MAIN_DIR}/fig/cur2.png")
        self.rct = self.img.get_rect()
        self.rct.center=(20,20)
        self.lock = 0
        self.count =0  # キーを押したときに瞬間的に移動しすぎないように最大n秒に一回だけ動かすようにする。
        
    def updata(self,key_lst,screen):
        sum_mv =[0,0]
        self.count +=1
        if self.count %7 == 0:  # 0.1秒たったら解凍
            self.lock = 0
            self.count = 0
        if not self.lock:
            for k, mv in __class__.delta.items():
                if key_lst[k]:
                    self.rct.move_ip(mv[0], mv[1])  
                    sum_mv[0] += mv[0]
                    sum_mv[1] += mv[1]
                    self.lock = 1  # いったん移動する機能を凍結させる
        # for k, mv in __class__.delta.items():
        #     if key_lst[k]:
        #         self.rct.move_ip(mv[0], mv[1])  
        #         sum_mv[0] += mv[0]
        #         sum_mv[1] += mv[1]

        screen.blit(self.img, self.rct)

def main():
    pg.display.set_caption("mymenu")
    bg_img = pg.image.load(f"{MAIN_DIR}/fig/title_resize.jpg")
    # bg_img = pg.transform.rotozoom(bg_img,0,1.0)
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    titlefont = pg.font.SysFont("hgp創英角ﾎﾟｯﾌﾟ体", 100)
    startimage = titlefont.render(f"START", 0, (0,0,0))
    settingsimage = titlefont.render(f"Settings", 0, (0,0,0))
    saveimage = titlefont.render(f"旅のしおり",0,(0,0,0))
    grassimg = pg.image.load(f"{MAIN_DIR}/fig/map_grass2.png")
    torideimg = pg.image.load(f"{MAIN_DIR}/fig/toride2.png")
    tatekawaimg = pg.image.load(f"{MAIN_DIR}/fig/tatekawa.png")
    yokokawaimg = pg.image.load(f"{MAIN_DIR}/fig/yokokawa.png")
    nanamekawaimg = pg.image.load(f"{MAIN_DIR}/fig/nanamekawa.png")
    mahoutukaiimg = pg.image.load(f"{MAIN_DIR}/fig/mahoutukai.png")
    # curimg = pg.image.load(f"{MAIN_DIR}/cur2.png")
    # pg.mixer.music.load(f"{MAIN_DIR}/oikazewoukete.mp3")
    # pg.mixer.music.load(f"{MAIN_DIR}/bgm/honnokioku.mp3")
    # pg.mixer.music.set_volume(1)
    # pg.mixer.music.play(-1)
    returnse = pg.mixer.Sound(f"{MAIN_DIR}/bgm/check.mp3")
    clock = pg.time.Clock()
    mousefont = pg.font.Font(None, 60)
    rect_ = 0
    game_mode = 0
    curx = 0
    cury = 0
    datalst = [[1 for _ in range(40)] for _ in range(25) ]
    tiledict = {1:"草原 回避-5％"}
    cur = Cur()
    lock = 0
    tmr = 0
    kao = pg.image.load(f"{MAIN_DIR}/fig/mahoutukai.png")
    charas = []
    charas.append(Chara_stats("モノ","魔法使い","ファイアー",1,10,10,10,10,10,10,kao))
    #siolst =pg.sprite.Group()
    print(charas[0])
    siolst = []
    bgm = Playbgm(f"{MAIN_DIR}/bgm/honnokioku.mp3",game_mode)
    now_bgm = f"{MAIN_DIR}/bgm/honnokioku.mp3"
    with open(f"{MAIN_DIR}/Book1.csv","r",encoding="utf_8") as rfo :
        nakami = csv.reader(rfo)
        for i, row in enumerate(nakami) :
            if i ==0:
                continue
            siodict = {}
            siodict["name"] = row[0]
            siodict["town"] = row[1]
            siodict["time"] = row[2]
            # siolst.add(Sioritext(siodict))
            siolst.append(Sioritext(siodict))
    
    while True:
        key_lst =  pg.key.get_pressed()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return 0
            if event.type == pg.KEYDOWN and event.key == pg.K_DOWN and game_mode == 0:
                rect_ += 1
                if rect_ > 3:
                    rect_ = 3
            if event.type == pg.KEYDOWN and event.key == pg.K_UP and game_mode ==0:
                rect_ -= 1
                if rect_ <0:
                    rect_ = 0
            if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
            
                
                if rect_ == 1:
                    game_mode += 1
                if game_mode >=3:
                    game_mode =2
    
                returnse.play()
            if event.type == pg.KEYDOWN and event.key == pg.K_BACKSPACE:
                if game_mode == 2:  #ゲーム開始したらバックスペースキー無効
                    continue
                game_mode -=1
                returnse.play()
                if game_mode <0:
                    game_mode = 0
            if game_mode == 2:
                if event.type == pg.KEYDOWN and event.key == pg.K_UP:
                    if cury >0:
                        cury -= 40
                if event.type == pg.KEYDOWN and event.key == pg.K_DOWN:
                    if cury <HEIGHT:
                        cury += 40
                if event.type == pg.KEYDOWN and event.key == pg.K_LEFT:
                    if curx>0:
                        curx -=40
                if event.type == pg.KEYDOWN and event.key == pg.K_RIGHT:
                    if curx < WIDTH:
                        curx += 40
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:  # チートモード 完成時にはオフ 
                game_mode -= 1
                if game_mode == -1:
                    return 0
    
        mouseX, mouseY = pg.mouse.get_pos()
        text = mousefont.render(f'{mouseX}, {mouseY}', True, (255, 0, 0))
        
        if game_mode ==0:
            screen.blit(bg_img, [0, 0])
            screen.blit(startimage,[WIDTH//2-200,HEIGHT//2+100])
            screen.blit(settingsimage,[WIDTH//2-200,HEIGHT//2+100+150])
            if rect_:
                if rect_ == 1:
                    pg.draw.rect(screen, (255,0,0), (470,580,930-470,700-580),10)
                elif rect_ == 2:
                    pg.draw.rect(screen, (255,0,0), (470,580+150,1060-470,700-580+30),10)
            now_bgm = f"{MAIN_DIR}/bgm/honnokioku.mp3"
        elif game_mode == 1:
            screen.blit(bg_img, [0, 0])
            screen.blit(saveimage,[WIDTH//2-200,HEIGHT//2+100])
            siolst[0].updata(screen)
            siolst[1].updata(screen)
        
        elif game_mode == 2:
            for i in range (25):
                for j in range(40):
                    
                    if j == 13 and i <10:
                        screen.blit(tatekawaimg,[40*j,40*i])
                    elif i ==10 and j <=12:
                        screen.blit(yokokawaimg,[40*j,40*i])
                    elif i == 10 and j == 13:
                        screen.blit(nanamekawaimg,[40*j,40*i])
                    else:
                        screen.blit(grassimg,[40*j,40*i])
            screen.blit(torideimg,[40,40])
            for k in range(40):
                pg.draw.line(screen,(0,0,0),(k*40,0),(k*40,HEIGHT),1)
            for l in range(25):
                pg.draw.line(screen,(0,0,0),(0,l*40),(WIDTH,l*40))
            now_bgm = f"{MAIN_DIR}/bgm/oikazewoukete.mp3"
            #screen.blit(charas[0].chara_fig,[400,400])
            cur.updata(key_lst,screen)
            screen.blit(mahoutukaiimg,[38*40,23*40])
        screen.blit(text, [0, 0])
        bgm.updata(now_bgm,game_mode)
        # pg.mixer.music.load(f"{MAIN_DIR}/oikazewoukete.mp3")
        # pg.mixer.music.set_volume(1)
        # pg.mixer.music.play(-1)
        pg.display.update()
        tmr += 1
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()