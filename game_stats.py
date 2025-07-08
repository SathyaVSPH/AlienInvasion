
class GameStat:

    def __init__(self, ai_obj):
        self.settings = ai_obj.settings
        self.reset_stat()
    
    def reset_stat(self):
        self.ship_remaining = self.settings.ship_limit