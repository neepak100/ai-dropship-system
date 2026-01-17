class KillSwitch:
    def __init__(self):
        self.is_active = False
    
    def trigger(self):
        self.is_active = True