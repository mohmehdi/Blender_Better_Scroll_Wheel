bl_info = {
    "name": "Better_Scroll_Time",
    "blender": (2, 80, 0),
    "category": "Object",
}
#---------------------------------------add-on-info------------------------------------#


import bpy
from bpy.props import *
import addon_utils


class ScrollWheelTime(bpy.types.Operator):
    """Sets the time in range"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.scroll"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Better Time Scroll Wheel"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.
    direction: IntProperty()
    
    def execute(self, context):        # execute() is called when running the operator.    
        # logic
        scn = context.scene 
        current_frame = scn.frame_current
        current_frame+=self.direction
        scn.frame_set(current_frame)
           
        if not scn.frame_start <= current_frame <= scn.frame_end:
            scn.frame_set(scn.frame_start if self.direction>=1 else scn.frame_end)

        return {'FINISHED'}            # Lets Blender know the operator finished successfully.


addon_keymaps = []

def menu_func(self, context):
    self.layout.operator(ScrollWheelUpTime.bl_idname)

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
    
    print("Installed Better Scroll Time !")

def unregister():
    bpy.utils.unregister_class(ScrollWheelUpTime)
    
     # Remove the hotkey
    for km, k in addon_keymaps:
        km.keymap_items.remove(k)
    addon_keymaps.clear()



# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()