# Blender Better Alt Scroll Wheel  

normally when using blender <kbd> Alt </kbd> + <kbd> Wheel Up/Down</kbd>  time cursor will pass the end and start frames in timeline and its a bit anoying for animating something like a walk cycle where you want to see the transition between ending and starting over .  
so if you like to use this shortcut you can use this add-on ( my first add on )  
its a very basic add on (_i encourage you to look at the script as its a good point to start i think_) im just checking if current frame is passed the end or start setting it to where it needs to be  
one thing to mention is im setting the hotkeys in registeration function of the add on and it doesnt work(becuaze im setting the time frame and defualt hotkey also tries to do that) until you disable default hotkeys, you can see here how:  

## How to Install

`` Edit -> Prefrences -> Keymap ``  

1. set the search type to **Key-Binding**   
2. search for **wheel**  
3. scroll a bit and find **Frames** section  
4. and disable both **Frame Offsets** 

now those keys are free to use   

from:   
`` Edit -> Prefrences -> Add-Ons ``  
6. click **install**  
7. select `` BetterAltScrollTime.py ``  
8. enable it  
9. enjoy not taking your hand your mouse wheel to put the frame cursor somewhere and save a lot of energy  
