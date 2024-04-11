import bpy

armature = bpy.context.object
mesh = bpy.context.object.data

bpy.ops.object.modifier_apply(modifier='Armature')

bpy.context.view_layer.objects.active = mesh

bpy.ops.object.mode_set(mode='EDIT')

bpy.context.tool_settings.mesh_select_mode = (False, False, True)

bpy.ops.mesh.select_all(action='SELECT')

bpy.ops.object.vertex_group_assign()

bpy.ops.object.mode_set(mode='OBJECT')


# skin
obj = bpy.context.active_object
bone_names = ['Bone1', 'Bone2', 'Bone3']  # Replace with your bone names
for bone_name in bone_names:
    obj.vertex_groups.new(name=bone_name)

vertices = obj.data.vertices
for vertex in vertices:
    for group_index, group in enumerate(vertex.groups):
        bone_name = bone_names[group.group]
        obj.vertex_groups[bone_name].add([vertex.index], group.weight, 'REPLACE')

obj.data.update()
