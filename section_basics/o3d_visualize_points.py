import sys
import numpy as np
import open3d as o3d

filename = sys.argv[1]

print("Loading a point cloud from", filename)
# Load as mesh data
# pcd = o3d.io.read_triangle_mesh(filename)
# Load as point cloud
pcd = o3d.io.read_point_cloud(filename)

print(pcd)
print(np.asarray(pcd.points))

o3d.visualization.draw_geometries([pcd])
