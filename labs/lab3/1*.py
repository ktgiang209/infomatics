#8<(
import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")

arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()

arcade.draw_circle_filled(500,500,450,(244,212,71))

arcade.draw_circle_filled(400,700,101,(0,0,0))
arcade.draw_circle_filled(600,700,101,(0,0,0))
arcade.draw_circle_filled(400,700,70,(255,255,255))
arcade.draw_circle_filled(600,700,70,(255,255,255))

arcade.draw_triangle_filled(450,450,550,450,500,600,(5,6,7))

arcade.draw_ellipse_filled(500,200,600,400,(0,0,0))
arcade.draw_ellipse_filled(500,150,650,300,(244,212,71))
arcade.draw_circle_outline(500,500,522,(255,255,255),72)


arcade.finish_render()

arcade.run()