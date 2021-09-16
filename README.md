# Blender Better Alt Scroll Wheel  

### Why Even Do this  
there are several options to monitor the transitions in frames but in my experience the best way is to use the mouse scroll wheel since you have more control over speed and its easy to use . It's like classic animation when animators flip back and forth paper between their fingers.  

but when you are making a cycle animation which is used a lot in game animations, there is one thing that is annoying and its how you cant see the transition from end frame to starting over as easy.

it is a small change but I think it worth it.

---
So here is a way to make this work  
basically we disable the old behavior and make a new one that does the same old behavior and just checks for the end and start frame then does the expected thing   

### Disable Default Hotkeys
`` Edit -> Preferences -> Keymap ``  

1. set the search type to **Key-Binding**   
2. search for "wheel"  
3. scroll a bit and find **Frames** section  
4. and disable both **Frame Offsets**  

### How to Make The Script
So to make a function and assign a hotkey to it we need an [Operator][1]   
which has an ``execute`` function where our logic will be  
and when we assign a hotkey to the operator ,when the keys are pressed(event happens) this function will be called

we want to make this as an add-on ,so we add some info about it in ``bl_info``
 
### First Step
 

as you can see the operator class has some basic properties like an ID , label and more that we can fill in and some more info

```python 
bl_info = {
    "name": "Better_Scroll_Time",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy
from bpy.props import *
import addon_utils


class ScrollWheelTime(bpy.types.Operator):
    """Sets the time in range"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.scroll"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Better Time Scroll Wheel"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.
    
    def execute(self, context):        # execute() is called when running the operator.    
        # logic


        return {'FINISHED'}            # Lets Blender know the operator finished successfully.

```  

### Execute

```python
direction: IntProperty()  #outside of execute function as a class member

    def execute(self, context):
        #logic
        scn = context.scene 
        current_frame = scn.frame_current
        current_frame+=self.direction
        scn.frame_set(current_frame)
           
        if not scn.frame_start <= current_frame <= scn.frame_end:
            scn.frame_set(scn.frame_start if self.direction>=1 else scn.frame_end)

        return {'FINISHED'}        

```
+ so if you look at blender keymaps in Preferences you can find Operations with some properties that we can provide too, with ``bpy.props`` functions like ``IntProperty()``  
+ we need a reference to the scene we are in to access things like start and end frame of the scene  
+ increase or decrease current frame with the amount of direction which will be set to +1 and -1 based on the shortcut
+ if current frame is not between start and end frame of the scene based on the direction we decide where to put the frame cursor
+ we tell blender this operation is finished
---

### Register


```python
addon_keymaps = []                 #outside of function


def register():      
    bpy.utils.register_class(ScrollWheelTime)
    # Add the hotkey
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name = "Window",space_type='EMPTY', region_type='WINDOW')
        km_up = km.keymap_items.new(ScrollWheelTime.bl_idname, type='WHEELUPMOUSE', value='PRESS', alt=True)
        km_down = km.keymap_items.new(ScrollWheelTime.bl_idname, type='WHEELDOWNMOUSE', value='PRESS', alt=True)
        
        km_up.properties.direction = -1     # setting the default property value for wheel up
        km_down.properties.direction = +1    # setting the default property value for wheel down
        
        addon_keymaps.append((km, km_up))
        addon_keymaps.append((km, km_down))
```
+ here we register our operation class so we can use if as an addon  
+ then we make a keymap using ``wm.keyconfigs.addon.keymaps.new``
and set its parameters :  
 ``name`` = "Window"  
  ``space_type`` ='EMPTY'  
   ``region_type`` ='WINDOW'  
**so our hotkey works in all editor windows**
+ then we assign our shortcuts to the operation class  
+ we can set a default value to our custom properties that defined as class member using ``bpy.props``  
+ we save this hotkeys so we can remove them in unregister function  

---

to make things clear in unregister function we remove our hotkeys



  [1]: https://docs.blender.org/api/current/bpy.types.Operator.html

### useful links : 
[KeyMaps](https://docs.blender.org/api/blender_python_api_2_76_2/bpy.types.KeyMaps.html?highlight=keymaps.new#bpy.types.KeyMaps.new),
[Operator](https://docs.blender.org/api/current/bpy.types.Operator.html) ,
[Property Definitions](https://docs.blender.org/api/current/bpy.props.html)
