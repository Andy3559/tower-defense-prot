import pyglet
from pyglet.window import key
score = 950 

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

score_label = pyglet.text.Label(text="Score: 0", x=10, y=460)

@new_window.event
def on_key_press(symbol, modifiers):
    global score
    score= score+1
    if score > 1000 :
        score= score+999
    print(score)
    score_str = str(score)
    score_label.text = score_str
    #score_label.update()
    
  
@new_window.event
def on_draw():
    score = 0
    new_window.clear()
    label.draw()
    score_label.draw()


  
pyglet.app.run()
