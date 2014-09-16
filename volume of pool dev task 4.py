#Jordan Russell
#16/09/14
#Development task 4

pool_length = float(input("Please input the length of the pool: "))
pool_width = float(input("Please input the width of the pool: "))
pool_depth_shallow = float(input("Please input the depth of the shallow end of the pool: "))
pool_depth_deep = float(input("Please input the depth of the deep end of the pool: "))

volume_of_shallow_cuboid = (pool_length * pool_width * pool_depth_shallow)
depth_of_triangle = (pool_depth_deep - pool_depth_shallow)
volume_of_deep_section = (depth_of_triangle * pool_length * pool_width)
volume_of_triangle = (volume_of_deep_section / 2)
volume_of_pool = (volume_of_shallow_cuboid + volume_of_triangle)
print("The volume of water required to fill the pool is {0} metres cubed".format(volume_of_pool))
