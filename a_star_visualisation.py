'''
author: Utkarsh Dev
email: utkarshdev047@gmail.com
'''

import pygame
import math
from queue import PriorityQueue

WIDTH = 600
WIN = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
white = (255,255,255)
black = (0,0,0)
purple = (128,0,128)
orange = (255,165,0)
grey  = (128,128,128)
turquoise = (64,244,208)

#building the visulaisation tool
class Node:
    def __init__(self,row,col,width,total_rows):
        self.row = row
        self.col = col
        self.x = row*width
        self.y = col*width
        self.color = white
        self.neighbours = []
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):   #method
        return self.row, self.col
    
    def is_closed(self):
        return self.color == red
    
    def is_open(self):
        return self.color == green
    
    def is_barrier(self):
        return self.color == black
    
    def is_start(self):
        return self.color == orange
    
    def is_end(self):
        return self.color == purple
    
    def reset(self):
        self.color = white
    
    def make_start(self):
        self.color = orange

    def make_closed(self):
        self.color = red

    def make_open(self):
        self.color = green

    def make_barrier(self):
        self.color = black

    def make_end(self):
        self.color = turquoise

    def make_path(self):
        self.color = purple

    def draw(self,win):   #where to draw a window
        pygame.draw.rect(win,self.color,(self.x,self.y,self.width,self.width))

    def update_neighbours(self,grid):
        self.neighbours = []
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): #down
            self.neighbours.append(grid[self.row + 1][self.col])

        if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): #up
            self.neighbours.append(grid[self.row - 1][self.col])
        
        if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): #right
            self.neighbours.append(grid[self.row][self.col + 1])
        
        if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): #left
            self.neighbours.append(grid[self.row][self.col - 1])


    def __lt__(self,other):
        return False
    
##  Defining the Hueristic Function

def heuristic(p1,p2):
    # We are essentially using the Manhattan distance
    x1,y1 = p1
    x2,y2 = p2

    return abs(x1 -x2) + abs(y1 -y2)

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()





def algorithm(draw,grid,start,end):
    draw()                       #calling function draw
    count = 0
    open_set = PriorityQueue()
    open_set.put((0,count,start))
    came_from = {}
    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0
    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = heuristic(start.get_pos(),end.get_pos())

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True
        
        for neighbour in current.neighbours:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + heuristic(neighbour.get_pos(), end.get_pos())

                if neighbour not in open_set_hash:
                    count +=1
                    open_set.put((f_score[neighbour],count,neighbour))
                    open_set_hash.add(neighbour)
                    neighbour.make_closed()

        draw()

        if current != start:
            current.make_closed()

    return False

def make_grid(rows,width):
    grid = []
    gap = width // rows  # integer division
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i,j,gap,rows)
            grid[i].append(node)


    return grid

def draw_grid(win,rows,width): #draw grid lines
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win,grey,(0,i*gap),(width, i*gap))

    for j in range(rows):
        pygame.draw.line(win,grey,(j*gap,0),(j*gap, width))

    
def draw(win,grid,rows,width):
    win.fill((255,255,255))

    for row in grid:
        for node in row:
            node.draw(win) 

    draw_grid(win,rows,width)
    pygame.display.update()

def get_clicked_pos(pos,rows,width):
    gap = width // rows
    y,x = pos
    row = y // gap
    col = x // gap
    return row,col

def main(win,width):
    ROWS = 50
    grid = make_grid(ROWS,width)

    start = None
    end = None

    run = True
    started = False
    while run:
        draw(win,grid,ROWS,width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  #left
                pos = pygame.mouse.get_pos()
                row,col = get_clicked_pos(pos,ROWS,width)
                node = grid[row][col]
                if not start:
                    start = node
                    start.make_start()

                elif not end and node != start:
                    end = node
                    end.make_end()

                elif node != end and node != start:
                    node.make_barrier()


            elif pygame.mouse.get_pressed()[2]: #right
                pos = pygame.mouse.get_pos()
                row,col = get_clicked_pos(pos,ROWS,width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for node in row:
                            node.update_neighbours(grid)

                    algorithm(lambda : draw(win,grid,ROWS,width), grid, start, end) #lambda is an anyonomous funtion
                    


                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

    

    pygame.quit()

main(WIN,WIDTH)













    

    



    


    








