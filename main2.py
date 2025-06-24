import random
import pygame as pg
from os import path
vec=pg.math.Vector2


img_dir=path.join(path.dirname(__file__),"img")


WIDTH = 800
HEIGHT = 650
FPS = 80
TITLE="PLATFORM"
FONT_NAME = 'arial'

pg.init()
pg.mixer.init()

#player properties
PLAYER_ACC=0.8
PLAYER_FRICTION=-0.12
PLAYER_GRAV=0.8

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHTBLUE = (0, 155, 155)
BGCOLOR = LIGHTBLUE

forwardx = 400
backwardx = 230





class Game:
    def __init__(self):
    #init the game window
        
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running=True
        self.gameover="W"
        self.world_shift=0
        self.level_limit=-7200
        self.font_name = pg.font.match_font(FONT_NAME)
        self.last_update=pg.time.get_ticks()
        self.frame=0
        self.timer=5600
        #self.BG=pg.image.load(path.join(img_dir,"Anirban-01.jpg")).convert()
        #self.bg=pg.transform.scale(self.BG,(3350,642))

    

        
    
   
    def new(self):
        #start a new game 
        self.all_sprites = pg.sprite.Group()
        self.platforms=pg.sprite.Group()
        self.bullets=pg.sprite.Group()
        self.balls=pg.sprite.Group()
        self.instantkill=pg.sprite.Group()
        self.enemys=pg.sprite.Group()
        self.saws=pg.sprite.Group()
        self.bombs=pg.sprite.Group()
        self.hearts=pg.sprite.Group()
        self.flags=pg.sprite.Group()
        self.player=Player(self)
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p=Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
            
        for saw in SAW_LIST:
            s=Saw(*saw)
            self.all_sprites.add(s)
            self.saws.add(s) 
        
        for bomb in BOMB_LIST:
            b=Bomb(*bomb)
            self.all_sprites.add(b)
            self.bombs.add(b) 
        
        for heart in HEART_LIST:
            h=Health(*heart)
            self.all_sprites.add(h)
            self.hearts.add(h)  
                    
        self.movingplat()
        self.enemy()
        for pool in POOL_LIST:
            p=Pools(*pool)
            self.all_sprites.add(p)
            self.instantkill.add(p)
        for canball in CANNON_LIST:
            c=Cannon(*canball)
            self.all_sprites.add(c) 
            self.platforms.add(c) 

        flag=Flag(8065,HEIGHT-90,princess_l)
        self.all_sprites.add(flag)
        self.flags.add(flag)
        self.run()

    def movingplat(self): 
        
        mp1=Moving_platform(self,1900,HEIGHT-380,green_plat)
        mp1.boundary_left=1650
        mp1.boundary_right=2130
        mp1.change_x=1
        mp1.player=self.player
        self.all_sprites.add(mp1)
        self.platforms.add(mp1)
        
        mp2=Moving_platform(self,1020,200,green_plat_s)
        mp2.boundary_bottom=400
        mp2.boundary_top=200
        mp2.change_y=-1
        mp2.player=self.player
        self.all_sprites.add(mp2)
        self.platforms.add(mp2)
        
         
        mp3=Moving_platform(self,3100,200,green_plat_s)
        mp3.boundary_bottom=400
        mp3.boundary_top=100
        mp3.change_y=-1
        mp3.player=self.player
        self.all_sprites.add(mp3)
        self.platforms.add(mp3)
        
        mp4=Moving_platform(self,3500,HEIGHT-380,green_plat_s)
        mp4.boundary_left=3300
        mp4.boundary_right=3550
        mp4.change_x=1
        mp4.player=self.player
        self.all_sprites.add(mp4)
        self.platforms.add(mp4)

        mp5=Moving_platform(self,3800,HEIGHT-390,ice_box)
        mp5.boundary_left=3700
        mp5.boundary_right=3850
        mp5.change_x=1
        mp5.player=self.player
        self.all_sprites.add(mp5)
        self.platforms.add(mp5)

        mp6=Moving_platform(self,4480,HEIGHT-370,ice_box)
        mp6.boundary_left=4380
        mp6.boundary_right=4520
        mp6.change_x=1
        mp6.player=self.player
        self.all_sprites.add(mp6)
        self.platforms.add(mp6)
        
        mp7=Moving_platform(self,5000,HEIGHT-280,ice_box)
        mp7.boundary_left=4980
        mp7.boundary_right=5200
        mp7.change_x=1
        mp7.player=self.player
        self.all_sprites.add(mp7)
        self.platforms.add(mp7)

        mp8=Moving_platform(self,7100,HEIGHT-280,ice_box)
        mp8.boundary_left=7020
        mp8.boundary_right=7400
        mp8.change_x=2
        mp8.player=self.player
        self.all_sprites.add(mp8)
        self.platforms.add(mp8)

        mp9=Moving_platform(self,7550,HEIGHT-380,ice_box)
        mp9.boundary_left=7440
        mp9.boundary_right=7740
        mp9.change_x=1
        mp9.player=self.player
        self.all_sprites.add(mp9)
        self.platforms.add(mp9)
        
    def enemy(self):
        e1=Enemy(self,1450,HEIGHT-120,1320,1650,enemy_walk)
        self.all_sprites.add(e1)
        self.enemys.add(e1)  
        e2=Enemy(self,4700,45,4590,4900,enemy_walk2)
        self.all_sprites.add(e2)
        self.enemys.add(e2) 
        e3=Enemy(self,2450,HEIGHT-125,2400,2615,enemy_walk2)
        self.all_sprites.add(e3)
        self.enemys.add(e3)
        e4=Enemy(self,5000,50,4900,5160,enemy_walk)
        self.all_sprites.add(e4)
        self.enemys.add(e4) 
        d1=Dragon(5650,120,dra_img1,210)
        self.all_sprites.add(d1)
        self.enemys.add(d1) 
        d2=Dragon(5750,HEIGHT-120,dra_img2,170)
        self.all_sprites.add(d2)
        self.enemys.add(d2) 
        d3=Dragon2(6530,HEIGHT-150)
        self.all_sprites.add(d3)
        self.platforms.add(d3)
        d4=Dragon2(6768,HEIGHT-150)
        self.all_sprites.add(d4)
        self.platforms.add(d4) 
        d5=Dragon(7350,HEIGHT-350,dra_img2,170)
        self.all_sprites.add(d5)
        self.enemys.add(d5)  
        d6=Dragon(7700,HEIGHT-425,dra_img2,170)
        self.all_sprites.add(d6)
        self.enemys.add(d6)  
        d7=Dragon(350,HEIGHT-250,dra_img2,170)
        self.all_sprites.add(d7)
        self.enemys.add(d7)  
        d8=Dragon(5650,300,dra_img4,170)
        self.all_sprites.add(d8)
        self.enemys.add(d8) 
           
      
    
   
 

    def run(self):
        #game loop
        self.playing=True
        while self.playing:
            self.clock.tick(FPS)
            self.timer-=1
            if self.timer<0:
                self.timer=0
            self.event()
            self.update()
            self.draw()

    
    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll
        everything: """
 
        # Keep track of the shift amount
        self.world_shift += shift_x
        for p in self.platforms:
            p.rect.x +=shift_x 
        for s in self.instantkill:
            s.rect.x +=shift_x 
        for e in self.enemys:
            e.rect.x +=shift_x  
        for s in self.saws:
            s.rect.x +=shift_x  
        for b in self.bombs:
            b.rect.x +=shift_x  
        for h in self.hearts:
            h.rect.x +=shift_x              
        for f in self.flags:
            f.rect.x+=shift_x 
        for b in self.balls:
            b.rect.x +=shift_x                         
    def update(self):
        #game loop update
        self.all_sprites.update()
       
        #scroll screen
       
        #scroll the world forward (FUTURE)      
        if self.player.rect.x >= forwardx:
                scroll = self.player.rect.x - forwardx
                self.player.rect.x = forwardx
                self.shift_world(-scroll)
        
        hits=pg.sprite.spritecollide(self.player,self.balls,True)
        for hit in hits:
            self.player.lives-=1
            expl_sound.play()
            exp=Explosion1(hit.rect.center,"bomb")
            self.all_sprites.add(exp)        
        

        hits=pg.sprite.spritecollide(self.player,self.saws,False) 
        for hit in hits:
            player_hitsound.play()
            if self.player.rect.right>hit.rect.left:
                self.player.change_x=3
            if  self.player.rect.left<hit.rect.right:
                self.player.change_x=-3
            if self.player.rect.bottom>=hit.rect.top:
                self.player.change_y=-10 
            self.player.lives-=1 
        
        hits=pg.sprite.spritecollide(self.player,self.bombs,True)
        for hit in hits:
            self.player.lives-=1
            expl_sound.play()
            exp=Explosion1(hit.rect.center,"bomb")
            self.all_sprites.add(exp)

        hits=pg.sprite.groupcollide(self.enemys,self.bullets,True,True,pg.sprite.collide_circle) 
        for hit in hits:
            expl_sound.play()
            exp=Explosion2(hit.rect.center,"enemy")
            self.all_sprites.add(exp)
        
        hits=pg.sprite.spritecollide(self.player,self.enemys,True)
        for hit in hits:
            self.player.lives-=1
            player_hitsound.play()
            exp=Explosion2(hit.rect.center,"enemy")
            self.all_sprites.add(exp)

        hits=pg.sprite.spritecollide(self.player,self.hearts,True)   
        for hit in  hits:
            if self.player.lives>=5:
                self.player.lives=5
            else:
                self.player.lives+=1                 
        #hiting with pools        
        hits=pg.sprite.spritecollide(self.player,self.instantkill,False)   
        if hits:
            #for sprite in self.all_sprites:
                #sprite.kill()   
            self.player.lives=0

        #hiting with flag     
        hits= pg.sprite.spritecollide(self.player,self.flags,False) 
        if hits:
            pg.time.wait(2000)
            self.playing=False 
            for sprite in self.all_sprites:
                sprite.kill()
            self.world_shift=0 #changing the background image to startposition         
            self.gameover="W"
                
       
        if self.player.lives==0 or self.timer==0:
            self.frame+=1
            if self.frame>=20:
                go_snd.play()
                self.player.kill()
                if self.frame==50:
                    self.playing=False 
                    for sprite in self.all_sprites:
                            sprite.kill()
                    self.world_shift=0 #changing the background image to startposition         
                    self.gameover="L"
                    self.frame=0
                    self.timer=5600
        
        #current_position = self.player.rect.x + self.world_shift
        #if current_position < self.level_limit:
            #self.player.rect.x=420 
        
        # scroll the world backward
        #if self.player.rect.x <= backwardx:
                #scroll = backwardx - self.player.rect.x
                #self.player.rect.x = backwardx
                #for p in self.platforms:
                        #p.rect.x += scroll
    def event(self):
        #game loop events
        for event in pg.event.get():
        # check for closing window
           if event.type == pg.QUIT:
               if self.playing:
                   self.playing=False
               self.running = False
           if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.player.jump()
                if event.key == pg.K_LEFT:
                    self.player.go_left()
                if event.key == pg.K_RIGHT:
                    self.player.go_right() 
                if event.key == pg.K_SPACE:
                    self.player.start_shoot=True
                    self.player.shoot()      
           if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT and self.player.change_x < 0:
                    self.player.stop()
                if event.key == pg.K_RIGHT and self.player.change_x > 0:
                    self.player.stop()




    def draw(self):
        #game loop draw
        #Draw / render
        self.screen.fill(BLACK)
        
        self.screen.blit(bg,(self.world_shift//3,0))
        self.all_sprites.draw(self.screen)
        self.draw_text("TIME: " + str(self.timer//80), 30, BLACK, WIDTH / 2, 20)
        self.draw_lives(WIDTH-200,20,self.player.lives,heart_img)
        # *after* drawing everything, flip the display
        pg.display.flip()


    def show_start_screen(self):
        pg.mixer.music.load(path.join(img_dir,"Flaming Soul.ogg"))
        pg.mixer.music.play(-1)
        self.screen.fill(BLACK)
        #self.draw_text(TITLE, 48, WHITE, WIDTH / 2, HEIGHT / 4)
        self.screen.blit(strt_player,(WIDTH/2-230,200))
        self.screen.blit(strt_enemy,(WIDTH-350,280))
        self.screen.blit(TITLE2,(219,20))
        self.screen.blit(ice_block_b,(0,HEIGHT-200))
        self.screen.blit(ice_block_b,(199,HEIGHT-200))
        self.screen.blit(ice_block_b,(398,HEIGHT-200))
        self.screen.blit(ice_block_b,(597,HEIGHT-200))
        self.screen.blit(paper,(200,HEIGHT-190))
        self.draw_text("Arrows to move, Up key to jump", 22, BLACK, WIDTH / 2, HEIGHT / 2+218)
        self.draw_text("Click to play", 22, BLACK, WIDTH / 2, HEIGHT * 3 / 4+25)
        self.draw_text("Space to shoot", 22, BLACK, WIDTH / 2, HEIGHT * 3 / 4+88)
        pg.display.flip()
        self.wait_for_key()
        pg.mixer.music.fadeout(500)
    
    def show_go_screen(self):
        self.timer=5600
        if not self.running:
                return
        if self.gameover=="L":
            self.screen.fill(BLACK)
            self.screen.blit(gameover,(252,30))
            self.screen.blit(player_dead,(292,200))
            #self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 4)
            #self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH / 2, HEIGHT / 2)
            self.screen.blit(paper,(200,HEIGHT-200))
            self.draw_text("Click to play again", 25, BLACK, WIDTH / 2, HEIGHT * 3 / 4+40)
        else:
            self.screen.fill(BLACK)
            self.screen.blit(tile2,(WIDTH/2-220,30))
            self.screen.blit(player_enjoy,(WIDTH/2-170,200))
            self.screen.blit(princess_enjoy2,(390,230))
            self.screen.blit(life_img,(WIDTH/2-20,200))
            self.screen.blit(life_img,(WIDTH/2+50,160))
            self.screen.blit(life_img,(WIDTH/2+120,220))
            self.screen.blit(paper,(200,HEIGHT-200))
            #self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH / 2, HEIGHT / 2)
            self.draw_text("Click to play again", 25, BLACK, WIDTH / 2, HEIGHT * 3 / 4+40)

        pg.display.flip()
        self.wait_for_key()
        
    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    waiting = False
                    
                

    def draw_text(self, text, size, color, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)
    
    def draw_lives(self,x,y,live,img):
        for i in range(live):
            img_rect=img.get_rect()
            img_rect.x=x+40*i
            img_rect.y=y
            self.screen.blit(img,img_rect)
      

class Player(pg.sprite.Sprite):
    def __init__(self,game):
        pg.sprite.Sprite.__init__(self)
        self.game=game
        self.walking=False
        self.jumping=False
        self.current_frame=0
        self.last_update=0
        self.direction = "R"
        self.start="S"
        self.start_shoot=False
        self.load_images()
        self.image=self.idle_r[0]
        self.rect2=self.image.get_rect()
        self.rect=pg.Rect(self.rect2.x+10,self.rect2.y+10,self.rect2.width-23,self.rect2.height-7)
        #pg.draw.rect(self.image,BLUE,self.rect)
        self.rect.center=(20,HEIGHT/2)
        self.change_x = 0
        self.change_y = 0
        self.shoot_delay=500
        self.last_shoot=pg.time.get_ticks()
        self.walkcount=vec(self.rect.center)
        self.lives=5

    def load_images(self):
        self.idle_r=idle
        self.idle_l=[]
        for frame in self.idle_r:
            self.idle_l.append(pg.transform.flip(frame, True, False))

        self.walk_r=walk
        self.walk_l = []
        for frame in self.walk_r:
            self.walk_l.append(pg.transform.flip(frame, True, False))
        self.jump_r=imgj1
        self.jump_l=pg.transform.flip(imgj1,True,False)
        self.attack_r=attack
        self.attack_l=[]
        for frame in self.attack_r:
            self.attack_l.append(pg.transform.flip(frame, True, False))
    def jump(self):
        self.rect.y+=2
        #check if player hits a platform
    
        hits=pg.sprite.spritecollide(self,self.game.platforms,False)
        self.rect.y-=2
        if len(hits) > 0 or self.rect.bottom >= HEIGHT-50:
            jump_snd.play()
            self.change_y = -13

    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .35
 
        # See if we are on the ground.
        if self.rect.y >= HEIGHT-50 - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = HEIGHT-50 - self.rect.height

    def go_left(self):
         
        self.change_x = -3
        self.direction = "L"
        
 
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 3
        self.direction = "R"
 
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0            
    def update(self):
        self.walkcount.x+=self.change_x
        self.walkcount.y+=self.change_y
        self.animate()
          # Gravity
        self.calc_grav()
 
        # Move left/right
        self.rect.x += self.change_x

        if self.rect.x<=10:
            self.rect.x=10
           
 
        # See if we hit anything
        block_hit_list = pg.sprite.spritecollide(self, self.game.platforms, False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
            
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right

        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we hit anything
        block_hit_list = pg.sprite.spritecollide(self, self.game.platforms, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
           
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                #if self.rect.x<block.rect.right and self.rect.x>block.rect.left:
                self.rect.top = block.rect.bottom
 
            # Stop our vertical movement
            self.change_y = 0
            self.jumping=False

            if isinstance(block,Moving_platform ):
                
                self.rect.x += block.change_x
                
                
        
        #keys=pg.key.get_pressed()
        #if keys[pg.K_SPACE]:
            #self.start_shoot=True
            #self.shoot()
    def animate(self):
        now = pg.time.get_ticks()
        if self.change_x != 0:
            self.walking=True
        else:
            self.walking=False

        #walk animation
        if self.walking: 
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walk_r)   
                if self.change_x>0:
                    self.image = self.walk_r[self.current_frame]
                else:
                    self.image = self.walk_l[self.current_frame]    
        
        #jump
        if self.change_y !=0:
            self.jumping=True
        else:
            self.jumping=False  

        if self.jumping:
            if self.direction=="R":
                self.image=self.jump_r
            else:
                self.image=self.jump_l           
        
        #shoot
        if self.start_shoot:
            if now - self.last_update > 5:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.attack_r)
                if self.direction=="R":
                    self.image = self.attack_r[self.current_frame]
                else:
                    self.image = self.attack_l[self.current_frame] 
                self.start_shoot=False
                                  
        #idleanimation    
        if not self.jumping and not self.walking and not self.start_shoot:
            if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.idle_r)
                #bottom = self.rect.bottom
                if self.direction=="R":
                   self.image = self.idle_r[self.current_frame]
                else:
                    self.image = self.idle_l[self.current_frame]
                
    def shoot(self):
        now = pg.time.get_ticks()
        if now-self.last_shoot>self.shoot_delay:
            self.last_shoot=now
            if self.direction=="R":
                bullet=Bullet(self.rect.centerx,self.rect.centery+30,1)
                g.all_sprites.add(bullet)
                g.bullets.add(bullet) 
                shoot_snd.play() 
            else:
                bullet=Bullet(self.rect.centerx,self.rect.centery+30,-1)
                g.all_sprites.add(bullet)
                g.bullets.add(bullet) 
                shoot_snd.play() 

class Platform(pg.sprite.Sprite):
    def __init__(self,x,y,image):
        pg.sprite.Sprite.__init__(self)
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

class Moving_platform(pg.sprite.Sprite):
    def __init__(self,game,x,y,image):
        pg.sprite.Sprite.__init__(self)
        self.game=game
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.change_x = 0
        self.change_y = 0
    
        self.boundary_top = 0
        self.boundary_bottom = 0
        self.boundary_left = 0
        self.boundary_right = 0

        self.player=None
    
    def update(self):
         # Move left/right
        self.rect.x += self.change_x
 
        # See if we hit the player
        hit = pg.sprite.collide_rect(self, self.game.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.
 
            # If we are moving right, set our right side
            # to the left side of the item we hit
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.player.rect.left = self.rect.right
 
        # Move up/down
        self.rect.y += self.change_y
 
        # Check and see if we the player
        hit = pg.sprite.collide_rect(self, self.game.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom
 
        # Check the boundaries and see if we need to reverse
        # direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < self.boundary_top:
            self.change_y *= -1
            
 
        cur_pos = self.rect.x - self.game.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1  

class Bullet(pg.sprite.Sprite):

    def __init__(self,x,y,facing):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.transform.scale(shield_img,(28,28))
        #self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.radius=int(self.rect.width*0.9/2)
        #pg.draw.circle(self.image,RED,self.rect.center,self.radius)
        self.rect.bottom=y
        self.rect.centerx=x
        self.facing=facing
        self.speedy=5*facing

    def update(self):
        self.rect.x+=self.speedy
        #goes of the screen kills it
        if self.rect.left<0 or self.rect.right>WIDTH:
            self.kill()

class Pools(pg.sprite.Sprite):
    def __init__(self,x,y,image):
        pg.sprite.Sprite.__init__(self)
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
class Flag(pg.sprite.Sprite):
    def __init__(self,x,y,drag):
        pg.sprite.Sprite.__init__(self)
        self.drag=drag
        self.image=self.drag[0]
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.current_frame=0
        self.last_update=0

    def update(self):
        now= pg.time.get_ticks()
        if now - self.last_update > 120:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.drag)
                self.image=self.drag[self.current_frame]    


class Enemy(pg.sprite.Sprite):
    def __init__(self,game,x,y,start,end,image):
        pg.sprite.Sprite.__init__(self)
        self.game=game
        self.walk_r=image
        self.walk_l = []
        for frame in self.walk_r:
            self.walk_l.append(pg.transform.flip(frame, True, False))
        self.image=self.walk_r[0]
        self.rect=self.image.get_rect()
        self.radius=int(self.rect.width*0.7/2)
        #pg.draw.circle(self.image,RED,self.rect.center,self.radius)
        self.rect.x=x
        self.rect.y=y
        self.current_frame=0
        self.last_update=0
        self.start=start
        self.end=end
        self.path=[self.start,self.end]
        self.change_x=1
    
    def load_image(self):
        self.walk_r=enemy_walk
        self.walk_l = []
        for frame in self.walk_r:
            self.walk_l.append(pg.transform.flip(frame, True, False))
    def update(self):
        self.animate()
        self.rect.x+=self.change_x
        cur_pos = self.rect.x - self.game.world_shift
        if cur_pos < self.path[0] or cur_pos > self.path[1]:
            self.change_x *= -1  
    def animate(self):
        now= pg.time.get_ticks()
        if now - self.last_update > 100:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walk_r)   
                if self.change_x>0:
                    self.image = self.walk_r[self.current_frame]
                else:
                    self.image = self.walk_l[self.current_frame]   

class Saw(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.load_data()
        self.image=self.saw[0]
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.current_frame=0
        self.last_update=0
    
    def load_data(self):
        self.saw=saw_img
    def update(self):
        now= pg.time.get_ticks()
        if now - self.last_update > 2:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.saw)
                self.image=self.saw[self.current_frame]
        
class Bomb(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image=bomb_img
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)

class Health(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image=life_img
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)

class Explosion1(pg.sprite.Sprite):
    def __init__(self,center,size):
        pg.sprite.Sprite.__init__(self)
        self.size=size
        self.image=explosion_anim[self.size][0]
        self.rect=self.image.get_rect()
        self.rect.center=center
        self.frame=0
        self.last_update=pg.time.get_ticks()
        self.frame_rate=75

    def update(self):
        now=pg.time.get_ticks()
        if now-self.last_update>self.frame_rate:
            self.last_update=now
            self.frame+=1
            if self.frame==len(explosion_anim[self.size]):
                self.kill()
            else:
                center=self.rect.center
                self.image=explosion_anim[self.size][self.frame]
                self.rect=self.image.get_rect()
                self.rect.center=center        

class Explosion2(pg.sprite.Sprite):
    def __init__(self,center,size):
        pg.sprite.Sprite.__init__(self)
        self.size=size
        self.image=explosion_anim[self.size][0]
        self.rect=self.image.get_rect()
        self.rect.center=center
        self.frame=0
        self.last_update=pg.time.get_ticks()
        self.frame_rate=10

    def update(self):
        now=pg.time.get_ticks()
        if now-self.last_update>self.frame_rate:
            self.last_update=now
            self.frame+=1
            if self.frame==len(explosion_anim[self.size]):
                self.kill()
            else:
                center=self.rect.center
                self.image=explosion_anim[self.size][self.frame]
                self.rect=self.image.get_rect()
                self.rect.center=center        

class Cannon(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.image=cannon
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.shoot_delay=1200
        self.last_shot=pg.time.get_ticks()
    
    def update(self):
        now = pg.time.get_ticks()
        if now-self.last_shot>self.shoot_delay:
            self.last_shot=now
            bullet=Cannonball(self.rect.centerx,self.rect.top,ball)
            g.all_sprites.add(bullet)
            g.balls.add(bullet)

class Cannonball(pg.sprite.Sprite):
    
    def __init__(self,x,y,image):
        pg.sprite.Sprite.__init__(self)
        self.image=image
        #self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.radius=int(self.rect.width*0.9/2)
        #pg.draw.circle(self.image,RED,self.rect.center,self.radius)
        self.rect.bottom=y
        self.rect.centerx=x
        self.speedy=-3

    def update(self):
        self.rect.y+=self.speedy
        #goes of the screen kills it
        if self.rect.bottom<0 :
            self.kill()

class Dragon(pg.sprite.Sprite):
    def __init__(self,x,y,drag,frame):
        pg.sprite.Sprite.__init__(self)
        self.drag=drag
        self.image=self.drag[0]
        self.rect=self.image.get_rect()
        self.rect.center=(x,y)
        self.current_frame=0
        self.last_update=0
        self.frame=frame
    
    def update(self):
        now= pg.time.get_ticks()
        if now - self.last_update > self.frame:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.drag)
                self.image=self.drag[self.current_frame]

class Dragon2(pg.sprite.Sprite):
    def __init__(self,x,y):
        pg.sprite.Sprite.__init__(self)
        self.drag=dra_img3
        self.image=self.drag[0]
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        self.current_frame=0
        self.last_update=0
        self.shoot_delay=1500
        self.last_shot=pg.time.get_ticks()
    
    def update(self):
        self.animate()
        now = pg.time.get_ticks()
        if now-self.last_shot>self.shoot_delay:
            self.last_shot=now
            bullet=Cannonball(self.rect.centerx,self.rect.top+10,fireball)
            g.all_sprites.add(bullet)
            g.balls.add(bullet)

    def animate(self):
        now= pg.time.get_ticks()
        if now - self.last_update > 170:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.drag)
                self.image=self.drag[self.current_frame]

g=Game()


#graphics
BG=pg.image.load(path.join(img_dir,"Anirban-01.jpg")).convert()
bg=pg.transform.scale(BG,(3350,815))

#kn1.set_colorkey(BLACK)

imgi1= pg.transform.scale(pg.image.load(path.join(img_dir, "Idle (1).png")),(87,107))
imgi2= pg.transform.scale(pg.image.load(path.join(img_dir, "Idle (2).png")),(87,107))
imgi3= pg.transform.scale(pg.image.load(path.join(img_dir, "Idle (3).png")),(87,107))
imgi4= pg.transform.scale(pg.image.load(path.join(img_dir, "Idle (4).png")),(87,107))
imgi5= pg.transform.scale(pg.image.load(path.join(img_dir, "Idle (5).png")),(87,107))
imgi6= pg.transform.scale(pg.image.load(path.join(img_dir, "Idle (6).png")),(87,107))
imgi7= pg.transform.scale(pg.image.load(path.join(img_dir, "Idle (7).png")),(87,107))
imgi8= pg.transform.scale(pg.image.load(path.join(img_dir, "Idle (8).png")),(87,107))
imgi9= pg.transform.scale(pg.image.load(path.join(img_dir, "Idle (9).png")),(87,107))
imgi10= pg.transform.scale(pg.image.load(path.join(img_dir, "Idle (10).png")),(87,107))

idle=[imgi1,imgi2,imgi3,imgi4,imgi5,imgi6,imgi7,imgi8,imgi9,imgi10]

imgr1= pg.transform.scale(pg.image.load(path.join(img_dir, "Run (1).png")),(87,107))
imgr2= pg.transform.scale(pg.image.load(path.join(img_dir, "Run (2).png")),(87,107))
imgr3= pg.transform.scale(pg.image.load(path.join(img_dir, "Run (3).png")),(87,107))
imgr4= pg.transform.scale(pg.image.load(path.join(img_dir, "Run (4).png")),(87,107))
imgr5= pg.transform.scale(pg.image.load(path.join(img_dir, "Run (5).png")),(87,107))
imgr6= pg.transform.scale(pg.image.load(path.join(img_dir, "Run (6).png")),(87,107))
imgr7= pg.transform.scale(pg.image.load(path.join(img_dir, "Run (7).png")),(87,107))
imgr8= pg.transform.scale(pg.image.load(path.join(img_dir, "Run (8).png")),(87,107))
imgr9= pg.transform.scale(pg.image.load(path.join(img_dir, "Run (9).png")),(87,107))
imgr10= pg.transform.scale(pg.image.load(path.join(img_dir, "Run (10).png")),(87,107))

walk= [imgr1,imgr2,imgr3,imgr4,imgr5,imgr6,imgr7,imgr8,imgr9,imgr10]

shield_img= pg.image.load(path.join(img_dir, "Shield.png"))
#jump
imgj1= pg.transform.scale(pg.image.load(path.join(img_dir, "Jump (5).png")),(87,107))

#attack

imga6= pg.transform.scale(pg.image.load(path.join(img_dir, "Attack (16).png")),(87,107))
imga7= pg.transform.scale(pg.image.load(path.join(img_dir, "Attack (17).png")),(87,107))
imga8= pg.transform.scale(pg.image.load(path.join(img_dir, "Attack (18).png")),(87,107))
imga9= pg.transform.scale(pg.image.load(path.join(img_dir, "Attack (19).png")),(87,107))
imga10= pg.transform.scale(pg.image.load(path.join(img_dir, "Attack (20).png")),(87,107))

attack= [imga6,imga7,imga8,imga9,imga10]

#Enemy
imge1= pg.transform.scale(pg.image.load(path.join(img_dir, "_WALK_000.png")),(95,80))
imge2= pg.transform.scale(pg.image.load(path.join(img_dir, "_WALK_001.png")),(95,80))
imge3= pg.transform.scale(pg.image.load(path.join(img_dir, "_WALK_002.png")),(95,80))
imge4= pg.transform.scale(pg.image.load(path.join(img_dir, "_WALK_003.png")),(95,80))
imge5= pg.transform.scale(pg.image.load(path.join(img_dir, "_WALK_004.png")),(95,80))
imge6= pg.transform.scale(pg.image.load(path.join(img_dir, "_WALK_005.png")),(95,80))
imge7= pg.transform.scale(pg.image.load(path.join(img_dir, "_WALK_006.png")),(95,80))

enemy_walk=[imge1,imge2,imge3,imge4,imge5,imge6,imge7]

imgen1= pg.transform.scale(pg.image.load(path.join(img_dir, "E_WALK_000.png")),(105,90))
imgen2= pg.transform.scale(pg.image.load(path.join(img_dir, "E_WALK_001.png")),(105,90))
imgen3= pg.transform.scale(pg.image.load(path.join(img_dir, "E_WALK_002.png")),(105,90))
imgen4= pg.transform.scale(pg.image.load(path.join(img_dir, "E_WALK_003.png")),(105,90))
imgen5= pg.transform.scale(pg.image.load(path.join(img_dir, "E_WALK_004.png")),(105,90))
imgen6= pg.transform.scale(pg.image.load(path.join(img_dir, "E_WALK_005.png")),(105,90))
imgen7= pg.transform.scale(pg.image.load(path.join(img_dir, "E_WALK_006.png")),(105,90))

enemy_walk2=[imgen1,imgen2,imgen3,imgen4,imgen5,imgen6,imgen7]
#Saw
imgs1= pg.transform.scale(pg.image.load(path.join(img_dir, "SAW0.png")),(70,70))
imgs2= pg.transform.scale(pg.image.load(path.join(img_dir, "SAW1.png")),(70,70))
imgs3= pg.transform.scale(pg.image.load(path.join(img_dir, "SAW2.png")),(70,70))
imgs4= pg.transform.scale(pg.image.load(path.join(img_dir, "SAW3.png")),(70,70))

saw_img=[imgs1,imgs2,imgs3,imgs4]

imgd1= pg.transform.scale(pg.image.load(path.join(img_dir, "dragon1.png")),(230,149))
imgd2= pg.transform.scale(pg.image.load(path.join(img_dir, "dragon2.png")),(230,149))
imgd3= pg.transform.scale(pg.image.load(path.join(img_dir, "dragon3.png")),(230,149))

dra_img1=[imgd1,imgd2,imgd3]

imgdr1= pg.transform.scale(pg.image.load(path.join(img_dir, "flying_dragon-red-RGB_10.png")),(150,120))
imgdr2= pg.transform.scale(pg.image.load(path.join(img_dir, "flying_dragon-red-RGB_11.png")),(150,120))
imgdr3= pg.transform.scale(pg.image.load(path.join(img_dir, "flying_dragon-red-RGB_12.png")),(150,120))
imgdr4= pg.transform.scale(pg.image.load(path.join(img_dir, "flying_dragon-red-RGB_1.png")),(150,120))
imgdr5= pg.transform.scale(pg.image.load(path.join(img_dir, "flying_dragon-red-RGB_2.png")),(150,120))
imgdr6= pg.transform.scale(pg.image.load(path.join(img_dir, "flying_dragon-red-RGB_3.png")),(150,120))

dra_img2=[imgdr1,imgdr2,imgdr3]
dra_img3=[imgdr4,imgdr5,imgdr6]
dra_img4=[]
for frame in dra_img2:
            dra_img4.append(pg.transform.flip(frame, True, False))
#bomb
bomb_img= pg.image.load(path.join(img_dir, "bomb.png"))
#plateforms
ice_plat= pg.transform.scale(pg.image.load(path.join(img_dir, "iceplat.png")),(120,30))
ice_box=  pg.transform.scale(pg.image.load(path.join(img_dir, "icebox.png")),(60,60))
ice_block= pg.transform.scale(pg.image.load(path.join(img_dir, "ice_block.png")),(60,60))
green_plat=pg.transform.scale(pg.image.load(path.join(img_dir, "platform-07.png")),(120,30))
green_plat_s=pg.transform.scale(pg.image.load(path.join(img_dir, "platform-07.png")),(90,30))
stone_plat=pg.transform.scale(pg.image.load(path.join(img_dir, "stoneplat2.png")),(60,60))
stone_edge=pg.transform.scale(pg.image.load(path.join(img_dir, "stoner.png")),(60,60))
stone_plat2=pg.transform.scale(pg.image.load(path.join(img_dir, "stoneplat.png")),(60,60))
castle= pg.transform.scale(pg.image.load(path.join(img_dir, "castle2.png")),(320,550))
castleflip=pg.transform.flip(castle,True,False)
PLATFORM_LIST = [(0, HEIGHT - 105, stone_plat),(57, HEIGHT - 105, stone_plat),(0, HEIGHT - 157, stone_plat),(57, HEIGHT - 157, stone_plat),(117, HEIGHT - 157, stone_edge),(650, 420, green_plat),
                 (860, HEIGHT - 105, stone_plat2),(860, HEIGHT - 164, stone_plat2),(860, HEIGHT - 223, stone_plat2),(919, HEIGHT - 105, stone_plat2),(978, HEIGHT - 105, stone_plat2),(1037, HEIGHT - 105, stone_plat2),(1096, HEIGHT - 105, stone_plat2),(1155, HEIGHT - 105, stone_plat2),(1214, HEIGHT - 105, stone_plat2),(1214, HEIGHT - 164, stone_plat2),(1214, HEIGHT - 223, stone_plat2),(1214, HEIGHT - 282, stone_plat2),(1214, HEIGHT - 341, stone_plat2),(1214, HEIGHT - 400, stone_plat2),(1214, HEIGHT - 459, stone_plat2),(1273, HEIGHT - 459, stone_plat2),
                 (1450, HEIGHT - 250, green_plat),(1820, HEIGHT - 105, stone_plat2),(1820, HEIGHT - 164, stone_plat2),(1879, HEIGHT - 105, stone_plat2),(1938, HEIGHT - 105, stone_plat2),(1997, HEIGHT - 105, stone_plat2),(2056, HEIGHT - 105, stone_plat2),(2115, HEIGHT - 105, stone_plat2),(2174, HEIGHT - 105, stone_plat2),(2233, HEIGHT - 105, stone_plat2),(2292, HEIGHT - 105, stone_plat2),(2292, HEIGHT - 164, stone_plat2),
                 (2500, HEIGHT - 250, green_plat),(2400,150, green_plat),
                 (2700, HEIGHT - 105, stone_plat2),(2700, HEIGHT - 164, stone_plat2),(2700, HEIGHT - 223, stone_plat2),(2700, HEIGHT - 282, stone_plat2),(2700, HEIGHT - 341, stone_plat2),(2759, HEIGHT - 105, stone_plat2),(2759, HEIGHT - 164, stone_plat2),(2759, HEIGHT - 223, stone_plat2),(2759, HEIGHT - 282, stone_plat2),(2759, HEIGHT - 341, stone_plat2),
                 (2759, HEIGHT - 400, stone_plat2),(2818, HEIGHT - 105, stone_plat2),(2818, HEIGHT - 164, stone_plat2),(2818, HEIGHT - 223, stone_plat2),(2818, HEIGHT - 282, stone_plat2),(2818, HEIGHT - 341, stone_plat2),(2818, HEIGHT - 400, stone_plat2),(2818, HEIGHT - 459, stone_plat2),
                 (2877, HEIGHT - 105, stone_plat2),(2936, HEIGHT - 105, stone_plat2),(2995, HEIGHT - 105, stone_plat2),(3054, HEIGHT - 105, stone_plat2),(3113, HEIGHT - 105, stone_plat2),(3172, HEIGHT - 105, stone_plat2),(3231, HEIGHT - 105, stone_plat2),(3290, HEIGHT - 105, stone_plat2),(3349, HEIGHT - 105, stone_plat2),(3408, HEIGHT - 105, stone_plat2),(3467, HEIGHT - 105, stone_plat2),(3526, HEIGHT - 105, stone_plat2),(3585, HEIGHT - 105, stone_plat2),(3585, HEIGHT - 164, stone_plat2),(3585, HEIGHT - 223, stone_plat2),(3585, HEIGHT - 282, stone_plat2),
                 (4100, HEIGHT - 105, ice_block), (4100, HEIGHT - 164, ice_block), (4100, HEIGHT - 223, ice_block), (4100, HEIGHT - 282, ice_block), (4100, HEIGHT - 341, ice_block), (4100, HEIGHT - 400, ice_block), (4041, HEIGHT - 282, ice_block), (4159, HEIGHT - 105, ice_block),(4218, HEIGHT - 105, ice_block),(4277, HEIGHT - 105, ice_block),(4336, HEIGHT - 105, ice_block),(4395, HEIGHT - 105, ice_block),(4454, HEIGHT - 105, ice_block),(4513, HEIGHT - 105, ice_block),(4572, HEIGHT - 105, ice_block),(4631, HEIGHT - 105, ice_block),(4690, HEIGHT - 105, ice_block),(4749, HEIGHT - 105, ice_block),
                 (4808, HEIGHT - 105, ice_block),(4867, HEIGHT - 105, ice_block),(4926, HEIGHT - 105, ice_block),(4985, HEIGHT - 105, ice_block),(5044, HEIGHT - 105, ice_block),(5103, HEIGHT - 105, ice_block),(5162, HEIGHT - 105, ice_block),(5221, HEIGHT - 105, ice_block),(5280, HEIGHT - 105, ice_block),(5339, HEIGHT - 105, ice_block),(5339, HEIGHT - 164, ice_block),(5339, HEIGHT - 223, ice_block),(5339, HEIGHT - 282, ice_block),
                 (4290, HEIGHT - 280, ice_box), (4250, 100, ice_plat),(4605, 120, ice_plat),(4724, 120, ice_plat),(4843, 120, ice_plat),(4962, 120, ice_plat),(5081, 120, ice_plat),
                 (4600, HEIGHT - 280, ice_box),(4660, HEIGHT-280, ice_plat), (4720, HEIGHT - 340, ice_box), (4860, HEIGHT - 280, ice_box),
                 (5398, HEIGHT - 341, ice_block), (5457, HEIGHT - 400, ice_block), (5516, HEIGHT - 459, ice_block),(5575, HEIGHT - 459, ice_block),(5634, HEIGHT - 459, ice_block),(5693, HEIGHT - 459, ice_block),(5870, HEIGHT - 459, ice_block),(5870, HEIGHT - 518, ice_block),(5870, HEIGHT - 577, ice_block),(5870, HEIGHT - 636, ice_block),(5870, HEIGHT - 695, ice_block),(5870, HEIGHT - 754, ice_block),(5870, HEIGHT - 400, ice_block),(5870, HEIGHT - 341, ice_block),(5870, HEIGHT - 282, ice_block),(5810, HEIGHT - 282, ice_block),(5751, HEIGHT - 282, ice_block),(5692, HEIGHT - 282, ice_block),(5633, HEIGHT - 282, ice_block),
                 (5988, HEIGHT - 105, stone_plat2),(6047, HEIGHT - 105, stone_plat2),(6106, HEIGHT - 105, stone_plat2),(6106, HEIGHT - 164, stone_plat2),(6106, HEIGHT - 223, stone_plat2),(6106, HEIGHT - 282, stone_plat2),(6106, HEIGHT - 341, stone_plat2),(6106, HEIGHT - 400, stone_plat2),(6106, HEIGHT - 459, stone_plat2),(5929, HEIGHT - 282, ice_block),
                 (6280, HEIGHT - 105, stone_plat2),(6280, HEIGHT - 164, stone_plat2),(6280, HEIGHT - 223, stone_plat2),(6280, HEIGHT - 282, stone_plat2),(6280, HEIGHT - 341, stone_plat2),(6280, HEIGHT - 400, stone_plat2),(6280, HEIGHT - 459, stone_plat2),(6339, HEIGHT - 105, stone_plat2),(6398, HEIGHT - 105, stone_plat2),(6457, HEIGHT - 105, stone_plat2),(6457, HEIGHT - 164, stone_plat2),(6457, HEIGHT - 223, stone_plat2),(6457, HEIGHT - 282, stone_plat2),(6457, HEIGHT - 341, stone_plat2),(6457, HEIGHT - 400, stone_plat2),(6457, HEIGHT - 459, stone_plat2),(6516, HEIGHT - 459, stone_plat2),(6516, HEIGHT - 400, stone_plat2),
                 (6634, HEIGHT - 459, stone_plat2),(6634, HEIGHT - 400, stone_plat2),(6693, HEIGHT - 459, stone_plat2),(6693, HEIGHT - 400, stone_plat2),(6693, HEIGHT - 341, stone_plat2),(6693, HEIGHT - 282, stone_plat2),(6693, HEIGHT - 223, stone_plat2),(6693, HEIGHT - 164, stone_plat2),(6693, HEIGHT - 105, stone_plat2),(6752, HEIGHT - 459, stone_plat2),(6752, HEIGHT - 400, stone_plat2),(6870, HEIGHT - 459, stone_plat2),(6870, HEIGHT - 400, stone_plat2),(6929, HEIGHT - 459, stone_plat2),(6929, HEIGHT - 400, stone_plat2),(6929, HEIGHT - 341, stone_plat2),(6929, HEIGHT - 282, stone_plat2),(6929, HEIGHT - 223, stone_plat2),(6929, HEIGHT - 164, stone_plat2),(6929, HEIGHT - 105, stone_plat2),
                 (6988, HEIGHT - 105, stone_plat2),(7047, HEIGHT - 105, stone_plat2),(7106, HEIGHT - 105, stone_plat2),(7165, HEIGHT - 105, stone_plat2),(7224, HEIGHT - 105, stone_plat2),(7283, HEIGHT - 105, stone_plat2),(7342, HEIGHT - 105, stone_plat2),(7401, HEIGHT - 105, stone_plat2),(7460, HEIGHT - 105, stone_plat2),(7519, HEIGHT - 105, stone_plat2),(7578, HEIGHT - 105, stone_plat2),(7637, HEIGHT - 105, stone_plat2),(7696, HEIGHT - 105, stone_plat2),(7755, HEIGHT - 105, stone_plat2),(7755, HEIGHT - 164, stone_plat2),(7755, HEIGHT - 223, stone_plat2),
                 (8080,55,castleflip)]
#SAWS
SAW_LIST=[(710,HEIGHT-90),(1940,HEIGHT-140),(2040,HEIGHT-140),(2140,HEIGHT-140),(2240,HEIGHT-140)]
#BOMBS
BOMB_LIST=[(893,405),(2560,HEIGHT-270),(3720,HEIGHT-90),(3625,HEIGHT-301),(3840,HEIGHT-90),(3960,HEIGHT-90),
           (4700,95),(4320,80),(4900,95),(5100,95)]
#hearts
HEART_LIST=[(2460,120),(4700,260),(6730,130)]

#pool
lava= pg.transform.scale(pg.image.load(path.join(img_dir, "lava2.png")),(297,120))
lava_large= pg.transform.scale(pg.image.load(path.join(img_dir, "lava2.png")),(711,150))
ice=  pg.transform.scale(pg.image.load(path.join(img_dir, "frozenspike.png")),(595,100))
ice2= pg.transform.scale(pg.image.load(path.join(img_dir, "frozenspike.png")),(385,100))
POOL_LIST=[(919,HEIGHT-220,lava),(2877,HEIGHT-250,lava_large),(4159,HEIGHT-200,ice),(4749,HEIGHT-200,ice),
          (6988,HEIGHT-200,ice2),(7374,HEIGHT-200,ice2)]
#heart
heart_img= pg.transform.scale(pg.image.load(path.join(img_dir, "heart.png")),(25,20))
#life
life_img= pg.transform.scale(pg.image.load(path.join(img_dir, "heart.png")),(45,40))

flag_img= pg.transform.scale(pg.image.load(path.join(img_dir, "flag.png")),(90,500)) 

explosion_anim={}
explosion_anim["bomb"]=[]
explosion_anim["enemy"]=[]

for i in range(9):
    file_name="regularExplosion0{}.png".format(i)
    img=pg.image.load(path.join(img_dir,file_name)).convert()
    img.set_colorkey(BLACK)
    img_lg=pg.transform.scale(img,(95,95))
    explosion_anim["bomb"].append(img_lg)

for i in range(1,33):
    file_name="magic exp_{}.png".format(i)
    img=pg.image.load(path.join(img_dir,file_name)).convert()
    img.set_colorkey(BLACK)
    img_en=pg.transform.scale(img,(95,95))
    explosion_anim["enemy"].append(img_en)     
cannon= pg.transform.scale(pg.image.load(path.join(img_dir, "cannon.png")),(70,90)) 
ball = pg.transform.scale(pg.image.load(path.join(img_dir, "cannon ball.png")),(40,40)) 
fireball= pg.transform.scale(pg.image.load(path.join(img_dir, "fireball.png")),(40,60))
CANNON_LIST=[(6190,HEIGHT-135),(6360,HEIGHT-195)]
strt_player= pg.transform.scale(pg.image.load(path.join(img_dir, "Jump (5).png")),(177,197)) 
strt_enemy=pg.transform.scale(pg.image.load(path.join(img_dir, "knight.png")),(185,170))
tile= pg.image.load(path.join(img_dir, "TITLE2.png")).convert()
tile.set_colorkey(BLACK) 
gameover= pg.image.load(path.join(img_dir, "go.jpg")).convert()
player_dead=pg.transform.scale(pg.image.load(path.join(img_dir, "Dead (9).png")),(307,250))
player_enjoy=pg.transform.scale(pg.image.load(path.join(img_dir, "Walk (9).png")),(177,197))
princess_enjoy=pg.transform.scale(pg.image.load(path.join(img_dir, "reimu_120-0.png")),(140,160))
princess_enjoy2=pg.transform.flip(princess_enjoy,True,False)
ice_block_b= pg.transform.scale(pg.image.load(path.join(img_dir, "ice_block.png")),(200,200))
tile2= pg.image.load(path.join(img_dir, "WIN.png")).convert()
tile2.set_colorkey(BLACK) 

imgp1= pg.transform.scale(pg.image.load(path.join(img_dir, "reimu_0-0.png")),(85,90))
imgp2= pg.transform.scale(pg.image.load(path.join(img_dir, "reimu_0-1.png")),(85,90))
imgp3= pg.transform.scale(pg.image.load(path.join(img_dir, "reimu_0-2.png")),(85,90))
imgp4= pg.transform.scale(pg.image.load(path.join(img_dir, "reimu_0-3.png")),(85,90))
imgp5= pg.transform.scale(pg.image.load(path.join(img_dir, "reimu_0-4.png")),(85,90))
imgp6= pg.transform.scale(pg.image.load(path.join(img_dir, "reimu_0-5.png")),(85,90))
imgp7= pg.transform.scale(pg.image.load(path.join(img_dir, "reimu_0-6.png")),(85,90))
imgp8= pg.transform.scale(pg.image.load(path.join(img_dir, "reimu_0-7.png")),(85,90))
imgp9= pg.transform.scale(pg.image.load(path.join(img_dir, "reimu_0-8.png")),(85,90))
imgp10= pg.transform.scale(pg.image.load(path.join(img_dir, "reimu_0-9.png")),(85,90))
imgp11= pg.transform.scale(pg.image.load(path.join(img_dir, "reimu_0-10.png")),(85,90))

princess=[imgp1,imgp2,imgp3,imgp4,imgp5,imgp6,imgp7,imgp8,imgp9,imgp10,imgp11]
princess_l=[]
for frame in princess:
            princess_l.append(pg.transform.flip(frame, True, False))
paper=pg.transform.scale(pg.image.load(path.join(img_dir, "paper.png")),(400,191))
TITLE2= pg.transform.scale(pg.image.load(path.join(img_dir, "TITLE3.png")),(337,167))
#Sound
expl_sound= pg.mixer.Sound(path.join(img_dir,"Explosion.wav")) 
player_hitsound=pg.mixer.Sound(path.join(img_dir,"Hit_Hurt.wav")) 
jump_snd=pg.mixer.Sound(path.join(img_dir,"Jump5.wav")) 
shoot_snd=pg.mixer.Sound(path.join(img_dir,"Fire 4.wav"))
go_snd=pg.mixer.Sound(path.join(img_dir,"Game Over.wav")) 

g.show_start_screen()
while g.running:
    pg.mixer.music.load(path.join(img_dir,"battle-mus.mp3"))
    pg.mixer.music.play(-1)
    g.new()
    g.show_go_screen()
    
    pg.mixer.music.fadeout(500)
pg.quit()    
