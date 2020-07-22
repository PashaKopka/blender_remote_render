import bpy

bpy.context.scene.render.filepath = 'E:/!Files/coding/python/blender_render/main/data/image.jpg'
bpy.ops.render.render(write_still = True)