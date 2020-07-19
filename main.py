import pygame as py
from math import pi,sqrt,sin,cos

from space import Space

class Window:
    def __init__(self):
        self.running = True
        self.interval = pi/10000          #amount the angles change when you move

        #initialize the space
        self.t0 = 50
        self.space = Space(self.t0)

        #initialize pygame
        self.size = (500,500)
        self.display_window = py.display.set_mode((self.size))
        self.background = py.Surface(self.display_window.get_size()).convert()
        self.background.fill((0, 0, 128))
        
        #run the viewer
        self.run()

    def run(self):
        while self.running:
            self.transfer_dim()             #recalculate the a b values for each 3d point using the greeks
            self.check_user_action()        #see if user wants to update the greeks
            self.change_angle()             #update the greeks based on user input
            if self.running:
                self.update_image()             #draw each point on the screen given the a b 

    def transfer_dim(self):
        self.space.update_objects_ab()

    def update_image(self,edges=True):

        self.display_window.blit(self.background,(0,0))
        self.background.fill((0, 0, 128))
        for obj in self.space.objs:
            if edges == True:
                for point in obj.points.values():
                    py.draw.circle(self.background,obj.colour,self.recenter_coord(point.pixel),4)
                for edge in obj.edges:
                    py.draw.line(self.background,obj.colour,self.recenter_coord(edge.ab1),self.recenter_coord(edge.ab2),3)
        py.display.flip()
        
    def recenter_coord(self,coord):       #translates the 2d coordinates so that the (0,0) origin is in the center of the screen
        return (int(coord[0] + self.size[0]/2),int(coord[1] + self.size[1]/2))

    def check_user_action(self):
        for event in py.event.get():
            if event.type == py.QUIT:
                self.running = False
                py.quit()
            elif event.type == py.KEYDOWN:
                if event.key == py.K_w:
                    self.space.delta_gamma = -2*self.interval
                elif event.key == py.K_s:
                    self.space.delta_gamma = 2*self.interval
                elif event.key == py.K_d:
                    self.space.delta_alpha = self.interval
                elif event.key == py.K_a:
                    self.space.delta_alpha = -self.interval
            elif event.type == py.KEYUP:
                if event.key == py.K_w or event.key == py.K_s:
                    self.space.delta_gamma = 0
                elif event.key == py.K_d or event.key == py.K_a:
                    self.space.delta_alpha = 0

    def change_angle(self):
        self.space.gamma += self.space.delta_gamma
        self.space.alpha += self.space.delta_alpha
        self.space.plane.update()



if __name__ == "__main__":
    py.init()
    win = Window()
