import bpy
import bmesh
import random
from mathutils import Vector

class TestAddon(bpy.types.Panel):
    bl_label = "Test Panel"
    bl_idname = "PT_TestPanel"
    bl_space_type = 'VIEW_3D'
    bl_region_type='UI'
    bl_category = 'Create Objects'
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text= "Add an object", icon = 'CUBE')
        row = layout.row()
        row.operator("mesh.primitive_cube_add",icon="CUBE")
        
        row.operator("mesh.primitive_uv_sphere_add" ,icon="SPHERE")
        row = layout.row()
        row.operator("object.text_add" ,icon="TEXT")
        
obj = bpy.context.active_object

bm = bmesh.new()
bm.from_mesh(obj.data,face_normals=True)

# faces, which could be extruded
faces_copy = [f for f in bm.faces]
new_faces = []
# number of iterations goes here
for i in range(0, 2):
    for face in faces_copy:
        do_inset = random.randint(0,1)
        if do_inset:
            bmesh.ops.inset_region(bm, faces = [face], thickness=random.uniform(0.1, 0.9), depth=0)
            geom = bmesh.ops.inset_region(bm, faces = [face], thickness=0, depth=0)
            bmesh.ops.translate(bm, verts = face.verts, vec = face.normal * random.uniform(0.1, 4))
            new_faces.extend(geom['faces'])
            new_faces.append(face)
            for v in bm.verts:
             v.co.x += 1.0
             v.co.y += 1.0
             v.co.z += 1.0
             faces_copy = new_faces
             new_faces = []

bm.to_mesh(obj.data)
bm.free()
obj.data.update()

def register():
    bpy.utils.register_class(TestAddon)


def unregister():
    bpy.utils.unregister_class(TestAddon)


if __name__ == "__main__":
    register()
