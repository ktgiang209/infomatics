import arcade

input = open('/Users/macpro16/Desktop/labs/lab5/lab5.csv','r',encoding='utf8')
string = input.read().split('\n')
input.close()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Diagram")
arcade.set_background_color((213,220,219))
arcade.start_render()

for i in range(13):
    arcade.draw_line(50,150+65*i,990,150+65*i,(100,100,100),1)
    arcade.draw_text(i*1000+9000,5,150+65*i,(10,10,10),12,2)
a= (83,158,83)
b= (215,84,66)
c= (108,115,124)
d = 850/(len(string)-1)
keys = []
keys = string[0].split(';')
n = 0
for i in keys:
    if i == "Время":
        time = n
    elif i == "Открытие":
        open = n
    elif i == "Закрытие":
        end = n
    elif i == "Макс":
        max = n
    else:
        min = n
    n = n+1
n = 0
Time = ""
Open = End = Max = Min = 0.
for i in string[1:]:
    txt = i.split(';')
    for j in range(len(txt)):
        if j == time:
            Time = txt[j]
        elif j == open:
            Open = int(txt[j])
        elif j == end:
            End = int(txt[j])
        elif j == max:
            Max = int(txt[j])
        elif j == min:
            Min = int(txt[j])
    if Open > End:
        Color = b
    elif Open < End:
        Color = a
    else:
        Color = c
    Min = (Min-9000)*65/1000+150
    Max = (Max-9000)*65/1000+150
    Open = (Open-9000)*65/1000+150
    End = (End-9000)*65/1000+150
    arcade.draw_rectangle_filled(n*d+d/2+50,(Open+End)/2,20+d/4,abs(Open-End),Color)
    arcade.draw_line(n*d+d/2+50,Min,n*d+d/2+50,Max,Color,3)
    arcade.draw_text(Time,n*d+d/2+30,100,(10,10,10),12,3)
    n = n + 1

    
arcade.draw_line(50,150,50,930,(100,100,100),2)
arcade.draw_text("увеличение",100,40,b,14,5)
arcade.draw_text("уменьшение",480,40,a,14,5)
arcade.draw_text("постоянние",840,40,c,14,5)
arcade.draw_rectangle_filled(70,40,30,30,b)
arcade.draw_rectangle_filled(450,40,30,30,a)
arcade.draw_rectangle_filled(810,40,30,30,c)

arcade.finish_render()
arcade.run()