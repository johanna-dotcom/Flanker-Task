from psychopy import core, event, visual
event.globalKeys.add(key='q', modifiers=['ctrl'], func=core.quit)
from psychopy.visual import Window, TextStim
from psychopy.core import wait, Clock
from psychopy.hardware import keyboard
kb = keyboard.Keyboard()
from pathlib import Path
from PIL import Image
import random
import sys
my_win = Window ([800, 400], color="#0000FF")
my_text = TextStim(my_win, color = "#FFFF00" ,text = "Welcome to the Flanker Task Experiment")
info_text = TextStim(my_win, color = "#FFFF00", text = "Proceed to instructions by pressing the space button", pos = [0, -0.8])
my_text.draw()
info_text.draw()
my_win.flip()
kb.waitKeys(keyList = ["space"]) 
my_text.text = "During the experiment, you will see three arrows on the screen. Your job is to identify whether the central arrow is pointing to the right or to the left. To do so as quickly as possible, keep your left index finger on the S key and your right index finger on the K key. Then, if the central arrow points to the left, press S, if the central arrow points to the right, press K. Only the central arrow is relevant for you, you can ignore the other two arrows."
info_text.text = "When you are ready, proceed to the experiment by pressing the space button"
my_text.draw()
info_text.draw()
my_win.flip()
kb.waitKeys(keyList = ["space"]) 
sys.stdout = open("data_output.txt", "a")
list_arrows = ["arrow_right2.png", "arrow_left2.png"]
trial = 1
while trial < 7:
    print(trial)
    my_win.flip()
    wait(2)
    central_image = random.choice(list_arrows)
    arrow_central = visual.ImageStim(my_win, image=central_image)
    side_image = random.choice(list_arrows)
    arrow_side_1 = visual.ImageStim(my_win, image=side_image, pos=0.3)
    arrow_side_2 = visual.ImageStim(my_win, image=side_image, pos=-0.3)
    my_win.callOnFlip( kb.clock.reset ) 
    kb.clearEvents()
    while True:
        arrow_central.draw()
        arrow_side_1.draw()
        arrow_side_2.draw()
        my_win.flip()
        pressd = kb.getKeys()
        if pressd:
            print("key pressed:", pressd[0].name, "reaction time:", pressd[0].rt )
            trial = trial+1
            if central_image == "arrow_right2.png":
                print("correct response: k")
            elif central_image == "arrow_left2.png":
                print("correct response: s")
            if central_image == side_image:
                print("congurent")
            elif central_image != side_image:
                print("incongruent")
            break
        elif kb.clock.getTime() >= 5:
            print("-")
            break   
    if trial > 6:
        print("six trials completed")
        break
my_text.text = "THE END"
thank_you_text = TextStim(my_win, color = "#FFFF00", text = "Thank you for participating!", pos = [0, -0.2])
info_text.text = "Exit by pressing the space button"
my_text.draw()
thank_you_text.draw()
info_text.draw()
my_win.flip()
kb.waitKeys(keyList = ["space"])



