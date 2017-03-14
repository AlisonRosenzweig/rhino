import rhinoscriptsyntax as rs 
import mzrhinoutils as mz 

def make_frame(width, height, overhang, depth): 
    origin = [0, 0, 0]
    base_dims = [width, height, depth]
    base_coordinates = mz.box_verts_from_center_extents(origin, base_dims)
    base_box = rs.AddBox(mz.box_verts_from_center_extents(center, base_dims))
    border1 = rs.AddBox(mz.box_verts_from_center_extents
    border2 = 
    border3
    border4 
