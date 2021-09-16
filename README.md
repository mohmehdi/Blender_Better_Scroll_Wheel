# Blender Better Alt Scroll Wheel  

normally when using blender <kbd> Alt </kbd> + <kbd> Wheel Up/Down</kbd>  time cursor will pass the end and start frames in timeline and its a bit annoying for animating something like a walk cycle where you want to see the transition between ending and starting over .  
so if you like to use this shortcut you can use this add-on ( my first add on )  
its a very basic add on (_i encourage you to look at the script as its a good point to start i think_) I'm just checking if current frame is passed the end or start setting it to where it needs to be .   
one thing to mention is I'm setting the hotkeys in registration function of the add on and it doesn't work until you disable default hotkeys (both my addon  and blender frame offset operations try to set frame cursor and it wont work ), you can see here how to disable default one:  

## How to Install

`` Edit -> Prefrences -> Keymap ``  

1. set the search type to **Key-Binding**   
2. search for **wheel**  
3. scroll a bit and find **Frames** section  
4. and disable both **Frame Offsets** 

now those keys are free to use   

from:   
`` Edit -> Prefrences -> Add-Ons ``  
1. click **install**  
2. select `` BetterAltScrollTime.py ``  
3. enable it  
4. enjoy not taking your hand your mouse wheel to put the frame cursor somewhere and save a lot of energy  

### useful links : 
[KeyMaps](https://docs.blender.org/api/blender_python_api_2_76_2/bpy.types.KeyMaps.html?highlight=keymaps.new#bpy.types.KeyMaps.new),
[Operator](https://docs.blender.org/api/current/bpy.types.Operator.html) ,
[Property Definitions](https://docs.blender.org/api/current/bpy.props.html)
