bl_info = {
    "name": "Better_Scroll_Time",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy
import addon_utils


class ScrollWheelUpTime(bpy.types.Operator):
    """Sets the time in range"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.scroll_up"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Better Time Scroll Wheel Up"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):        # execute() is called when running the operator.
        
        
        # logic
        scn = bpy.context.scene 
        current_frame = bpy.context.scene.frame_current
        current_frame-=1
        bpy.context.scene.frame_set(current_frame)
           
        if current_frame < scn.frame_start:
            bpy.context.scene.frame_set(scn.frame_end)

        return {'FINISHED'}            # Lets Blender know the operator finished successfully.



class ScrollWheelDownTime(bpy.types.Operator):
    """Sets the time in range"""      # Use this as a tooltip for menu items and buttons.
    bl_idname = "object.scroll_down"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Better Time Scroll Wheel Down"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):        # execute() is called when running the operator.
        
        # logic
        scn = bpy.context.scene 
        current_frame = bpy.context.scene.frame_current
        current_frame+=1
        bpy.context.scene.frame_set(current_frame)
                  
        if current_frame > scn.frame_end:
            bpy.context.scene.frame_set(scn.frame_start)

        return {'FINISHED'}            # Lets Blender know the operator finished successfully.








addon_keymaps = []

def menu_func(self, context):
    self.layout.operator(ScrollWheelUpTime.bl_idname)
    self.layout.operator(ScrollWheelDownTime.bl_idname)

def register():      
    bpy.utils.register_class(ScrollWheelUpTime)
    bpy.utils.register_class(ScrollWheelDownTime)
    # Add the hotkey
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    if kc:
        km = wm.keyconfigs.addon.keymaps.new(name = "Window",space_type='EMPTY', region_type='WINDOW')
        km_up = km.keymap_items.new(ScrollWheelUpTime.bl_idname, type='WHEELUPMOUSE', value='PRESS', alt=True)
        km_down = km.keymap_items.new(ScrollWheelDownTime.bl_idname, type='WHEELDOWNMOUSE', value='PRESS', alt=True)
        addon_keymaps.append((km, km_up))
        addon_keymaps.append((km, km_down))
    
    print("Installed Better Scroll Time !")

def unregister():
    bpy.utils.unregister_class(ScrollWheelUpTime)
    bpy.utils.unregister_class(ScrollWheelDownTime)
    
     # Remove the hotkey
    for km, k in addon_keymaps:
        km.keymap_items.remove(k)
    addon_keymaps.clear()



# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()