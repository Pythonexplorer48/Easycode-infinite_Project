# EasyCode-infinite
**EasyCode-infinite is a python library made specifically so there would be easier and better coding with a lot of simplification added**

EasyCode-infinite simplifies game development in Python by providing high-precision math variables and powerful, easy-to-use base classes for the industry's most popular 2D frameworks.

# Key Features
* it includes of 3 special variables BigDecimal, BigString, and BigVector
* includes of optimizations
* is very fast and can save memory potentially
* has a couple new sprites you can use
* supports arcade, pyglet, and pygame

# Installation
Install EasyCode via `pip` or `uv`:

# Warning:
* A simple mistake in the project happend which was that unfortunately the Bistring doesn't save memory. This happened because the Bigstring tries splitting every byte into 3 smaller bytes and each would carry the characters but actually I recently found out that bytes are not virtual data they are physical levers. This will be fixed in version 1.4.0 but wont be as good as it orriginally would've been because it will add something that takes up memory and in total it will be worth 2 characters per byte.

```bash
pip install easycode_infinite
uv pip install easycode_infinite --system
```

# All Features
**Pygame only features**
* Attribute: get_font
example
```python
import pygame as pg
import easycode as ec

# setup screen & sprites...

ec.get_font("Impact")

# set up loop...
```
This gets the font automatically and gives you a font inless it isn't real if it has a typo it sets it to Arial.

* Attribute: change_axis
example
```python
import pygame as pg
import easycode as ec

# setup screen & sprites...
angle = 20
pivot_offset = (20, 50)

class sprite(ec.pg_sprite): #pg_sprite is a wrapper will get to later
    def __init__(self):
        super().__init__
        self.image = pg.Surface((20, 20))
        self.image.fill(60, 80, 170)
        self.rect = self.image.get_rect(topleft=(100, 100))

sprite = sprite()

ec.change_axis(sprite, angle, pivot_offset)

# set up loop...
```
This changes the axis of it meaning whenever you turn the sprite it rotates on a different axis.

* Sprite: PygameSmartCamera
example
```python
import pygame as pg
import easycode as ec

# setup screen & sprites...

w, h = (ScreenWidth, ScreenHeight)

camera = ec.PygameSmartCamera(w, h, lerp_speed=0.3)

# set up loop...
```
This allows you to control the camera on screen with these attributes
camera.update(self, target_rect)

camera.apply(self, entity_rect)


**Pygame and Pyglet shared features**
* Sprite: PygameDraggableSlider & PygletDraggableSlider
example
```python
import pygame as pg
import pyglet as pyg
import easycode as ec

# based of which library you choose to use anything else you need to do is what you code

color = (128, 197, 83)
startingX = 200
y = 100
min_x = 150
max_x = 250

try: # if your using Pygame do this
    slider = ec.PygameDraggableSlider(color, startingX, y, min_x, max_x)
except: # if your using Pyglet do this
    slider = ec.PygletDraggableSlider(color, startingX, y, min_x, max_x, batch=None, window=None)
```
This creates a Draggable slider that can slide between min_x and max_x is set to where the startingX is and is always at the y you input is colored whatever color you input using the attributes is how it works
*pygame*
handle_input(self, event)
get_value(self)
*pyglet*
on_mouse_press(self, x, y, button, modifiers)
on_mouse_release(self, x, y, button, modifiers)
on_mouse_drag(self, x, y, dx, dy, buttons, modifiers)
get_value(self)

* Sprite: PygameScreenShake & PygletScreenShake
example
```python
import pygame as pg
import pyglet as pyg
import easycode as ec

# based of which library you choose to use anything else you need to do is what you code

screenshaker = ec.PygameScreenShake(seed=None) # if your using Pygame only do this
ec.apply_to_window(window) # if your using Pyglet do this too
```
This will give you a screenshaker that uses an XORshift and dot product to shake the screen you can also set the seed to control how to screen shakes if you want you need to use these attributes
*pygame*
screenshaker._next_xorshift() # not necessary
screenshaker._get_rand_float() # not necessary
screenshaker.shake(intensity=None, duration=None, impact_pos=None, center_pos=None)
*pyglet*
pyglet uses the PygameScreenShaker in order to work so its mostly the same as in pygame

* Sprite: PygameTextBox & PygletTextBox
example
```python
import pygame as pg
import pyglet as pyg
import easycode as ec

# based of which library you choose to use anything else you need to do is what you code

x = 20
y = 20
width = 400
string "Hello World"
font_name = "CourierNew"w
fontsize = 20
fontcolor = (20, 78, 192)

try: # if your using Pygame do this
    Text = ec.PygameTextBox(x, y, width, string, font_name, fontsize, fontcolor, background_t_f=False, backgroundcolor=None, typewrite_t_f=False, time_per_char=50)
except: # if your using Pyglet do this
    Text = ec.PygletTextBox(x, y, width, initial_text="", batch=None, window=None)
```
This will give you a sprite to probably draw in your game it also has these attributes
*pygame*
Text.update()
Text.wrap_text(text)
Text.refresh_text()
*pyglet*
Text.text()

* Sprite: PygameDialogueBox & PygletDialogueBox
example
no example given just explanation
The DialogueBox is exactly like the TextBox, but it includes a special feature it is a group of strings instead of one string and so you can figure out by hovering your mouse over the part that says DialogueBox it does not use the strings it must have a tuple list or group, but these are the attributes to control it
*pygame*
Dialogue._update_display() # not necessary
Dailogue.next_string()
Dialogue.update()
*pyglet*
Dialogue._update_typewriter(dt) # not necessary
Dialogue.next_string(self)


**Arcade only features**
*Sprite: ArcadeGUIComponents
example
```python
import arcade as arc
import easycode as ec

component_1 = ec.create_textbox(manager, x, y, width, text="")
component_2 = ec.create_slider(manager, x, y, width, value=50)
```
This creates a arcade version of the TextBox & DraggableSlider thats it.


**Pygame, Arcade, & Pyglet Features**
* Sprite: PygameHealthBar, PygletHealthBar, & ArcadeHealthBar
example
```python
import pygame as pg
import pyglet as pyg
import arcade as arc
import easycode as ec

x, y = 60, 40
width_per_1hp = 1
max_health = 200
current_health = 100
bar_height = 30
border_color = (255, 10, 15)
health_color = (255, 0, 255)

try: # if your using Pygame do this
    health_bar = ec.PygameHealthBar(x, y, width_per_1hp, max_health, current_health, bar_height, border_color, health_color)
except: # if your using Pyglet / Arcade do this
    try: # if your using Pyglet do this
        # break currently done coding wait for me to update the repository later
    except: # if your using Arcade do this
        # break currently done coding wait for me to update the repository later
# break currently done coding wait for me to update the repository later