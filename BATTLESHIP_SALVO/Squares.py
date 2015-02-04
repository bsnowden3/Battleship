import pygame


class Square(pygame.sprite.Sprite):
    def __init__(self, row, col, color):
        pygame.sprite.Sprite.__init__(self)
        self.row = row
        self.col = col
        self.ocean_tile_width = 50
        self.ocean_tile_height = 50
        self.image = pygame.Surface([self.ocean_tile_width, self.ocean_tile_height])
        self.image.fill(color)
        self.rect = self.image.get_rect() # gets a rect object with width and height specified above
        # a rect is a pygame object for handling rectangles
 ##       self.rect.x = get_col_left_loc(col)
 ##       self.rect.y = get_row_top_loc(row)
        self.color = color
    
    def get_rect_from_square(self):
        """
            Returns the rect object that belongs to this Square
            """
        
        return self.rect
    """
    def change_color(self):
        
            
        if self.color == black:
            self.color = white
                self.image.fill(white)
        else:
            self.color = black
                self.image.fill(black)
    """
