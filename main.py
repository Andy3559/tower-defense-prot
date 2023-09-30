
import pyglet
from pyglet.window import key
score = 23  

new_window = pyglet.window.Window()
keys = key.KeyStateHandler()
new_window.push_handlers(keys)
  
label = pyglet.text.Label('Hello, World its me!',
                          font_name ='Cooper',
                          font_size = 16,
                          x = new_window.width//2, 
                          y = new_window.height//2,
                          anchor_x ='center', 
                          anchor_y ='center')


@new_window.event
def on_key_press(symbol, modifiers):
    global score
    score= score+1
    if score <=> 100:
        score= score+100
    print(score)
    
  
@new_window.event
def on_draw():
    score = 0
    new_window.clear()
    label.draw()

  
pyglet.app.run()
