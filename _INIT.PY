

bl_info = {
    "name" : "GeoInstancer",
    "author" : "Ayush Yadav",
    "description" : "Instance Geos on Vertices - Similar to Houdini (Copy to Points) - FEEDBACK is appreciated",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}
#imports
import bpy,bmesh
from bpy.props import(
    PointerProperty
)
from . maingeoselector import Main_OT_Geometry
from . Interface_Panel import Interface_PT_Panel
from . maingeoselector import Reset_OT_Geometry
from . properties import addon_Properties

#classestoregister
classes = (Interface_PT_Panel, Main_OT_Geometry, addon_Properties, Reset_OT_Geometry)

#registration
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.Scene.your_properties = PointerProperty(type=addon_Properties) #Propertygroupaccess

def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
    del bpy.types.Scene.your_properties #Propertygroupdelete
