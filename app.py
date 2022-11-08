import pygame
pygame.init()


def just(r,v):
    s = f"{r : ^30}"+f"{v[1] : ^40}"+f"{v[0] : ^30}"
    return s
 
v1 = [[23,"Rahulaasfs afa adf asf"],
      [4353,"Rahul  adsfa"],
      [2412,"Rahul asfasf"],
      [324,"Rahul asdf"],
      [2433,"Rahul asdfasd"],
      [253,"Rahulasdf "],
      [253,"Rahulasdf"],
      [23,"Rahul"],
      [273,"Rahul"],
      [243,"Rahul"],
      [2833,"Rahul"],
      [23,"Rahul"],
      [27743,"Rahul"],
      [243,"Rahul"]]
a=v1.copy()
a.insert(0,["NAME","SCORES"])
# head = ['Adm no.','Score ']
screen = pygame.display.set_mode((1550,800))
screen.fill((255, 255, 255))
pygame.display.set_caption('Just reference')
s = ''
v1.sort(reverse=True)
width = 1550
height = 800

st = 100

row_1 = s = f"{'RANKING' : ^30}"+f"{'NAME' : ^30}"+ f"{'SCORES' : ^30}"

text_font = pygame.font.SysFont("arial",55)
text = text_font.render(str(row_1),True,'black')
text_rect = (st-60,50)


text_font = pygame.font.SysFont("arial",50)
row_2 = just("1",v1[0])

text2 = text_font.render(str(row_2),True,'black')
text_rect2 = (st,170)


row_3= just("2",v1[1])

text3= text_font.render(str(row_3),True,'black')
text_rect3 = (st,170+110)

row_4= just("3",v1[2])

text4= text_font.render(str(row_4),True,'black')
text_rect4 = (st,170+110+110)


st=st

row_5= just("4",v1[3])

text5= text_font.render(str(row_5),True,'black')
text_rect5 = (st,170+110+110+110)

row_6= just("5",v1[4])

text6= text_font.render(str(row_6),True,'black')
text_rect6 = (st,170+110+110+110+110)

row_7= just("6",v1[5])

text7= text_font.render(str(row_7),True,'black')
text_rect7= (st,170+110+110+110+110+110)

row_8= just("7",v1[6])

text8= text_font.render(str(row_8),True,'black')
text_rect8= (st,170+110+110+110+110+110+110)

row_9 = just("8",v1[7])

text9= text_font.render(str(row_9),True,'black')
text_rect9 = (st,170+110+110+110+110+110+110+110)

row_10 = just("9",v1[8])

text10= text_font.render((str(row_10)),True,'black')
text_rect10 =(st, 170+110+110+110+110+110+110+110+110+110)


row_11 = just("10",v1[9])

text11= text_font.render((str(row_11)),True,'black')
text_rect11 = (st,170+110+110+110+110+110+110+110+110+110+110)



clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255, 255, 255))

    
    screen.blit(text,text_rect)

    pygame.draw.rect(screen, (250, 188, 41),
                 pygame.Rect(text_rect2[0]+100, text_rect2[1]-22, 1200, 100),50,50)
    screen.blit(text2,text_rect2)

    pygame.draw.rect(screen, (254, 132, 47),
                 pygame.Rect(text_rect3[0]+100, text_rect3[1]-22, 1200, 100),50,50)
    screen.blit(text3,text_rect3)

    pygame.draw.rect(screen, (239, 74, 46),
                 pygame.Rect(text_rect4[0]+100, text_rect4[1]-22, 1200, 100),50,50)
    screen.blit(text4,text_rect4)

    pygame.draw.rect(screen, (41, 189, 163),
                 pygame.Rect(text_rect5[0]+100, text_rect5[1]-22, 1200, 100),50,50)
    screen.blit(text5,text_rect5)

    pygame.draw.rect(screen, (41, 189, 163),
                 pygame.Rect(text_rect6[0]+100, text_rect6[1]-22, 1200, 100),50,50)
    screen.blit(text6,text_rect6)

    pygame.draw.rect(screen, (41, 189, 163),
                 pygame.Rect(text_rect7[0]+100, text_rect7[1]-22, 1200, 100),50,50)
    screen.blit(text7,text_rect7)
    
    screen.blit(text8,text_rect8)
    screen.blit(text9,text_rect9)
    screen.blit(text10,text_rect10)
    screen.blit(text11,text_rect11)
    


    pygame.display.update()
    clock.tick(60)