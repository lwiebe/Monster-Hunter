from settings import *

class Battle:
    def __init__(self, player_monsters, opponent_monster, monster_frames, bg_surf, fonts):
        self.display_surface = pygame.display.get_surface()
        self.bg_surf = bg_surf
        self.monster_frames = monster_frames
        self.fonts = fonts
        self.monster_data = {'player': player_monsters, 'opponent': opponent_monster}

    def update(self, dt):
        self.display_surface.blit(self.bg_surf, (0,0))