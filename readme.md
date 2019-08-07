# Alien
An Alien Invasion game I am working on from the book "Python Crash Course" by Eric Matthes
## My first attempts at Python
This is my first attempt at understanding the Python language and it's me trying to expand my knowledge surrounding computer science.
## Config
To change your settings only edit the Settings.py file

```python
        self.screen_width = 1200 # Max screen width 
        self.screen_height = 800 # Max screen height
        self.bg_colour = (230, 230, 230) # Background colour
        self.ship_limit = 3 # Max lives 
        self.game_caption = "Alien Invasion!" # Game title
        
        self.bullet_width = 5 # Size of the bullets width
        self.bullet_height = 15 # Size of the bullets height
        self.bullet_colour = 60, 60, 60 # Colour of the bullets
        self.bullets_allowed = 100 # Max amount of bullets on screen
        
        self.alien_points = 50 # Points gained per alien killed
        self.alien_speed_factor = 500 # Alien movement speed (Left to right)
        self.fleet_drop_speed = 100 # Alien fleet drop down speed (From top to bottom)
        
        self.speedup_scale = 1.1 # Multiplier for alien speed
        self.score_scale = 1.5 # Multiplier for score scaling

        self.ship_speed_factor = 1.5 # Ship speed
        self.bullet_speed_factor = 3 # Bullet travel speed
        self.alien_speed_factor = 1 # Alien movement speed (Left to right)
        self.fleet_direction = 1 # 1 is right, -1 is left
```


## Todo
I might add sounds, power ups like shields in front of your spaceship and have the aliens shoot back etc.
Maybe :)
