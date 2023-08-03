class Person:
    max_up = 3
    _max_level = 80
    
    def __init__(self, name, race = 'unknown', speed=100):
        self.name = name
        self.race = race
        self.level = 1
        self.health = 100
        self._speed = speed

    def _check_level(self):
        return self.level < self._max_level
    
    def level_up(self):
        if self._check_level():
            self.level += 1
        else:
            self.level = self._max_level

    

