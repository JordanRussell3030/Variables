#Jordan Russell
#14/09/14
#Revision task - lift and fridge volumes.
lift_height = float(input("Please input the height of the lift: "))
lift_width = float(input("Please input the width of the lift: "))
lift_depth = float(input("Please input the depth of the lift: "))
fridge_height = float(input("Please input the height of the fridge: "))
fridge_width = float(input("Please input the width of the fridge: "))
fridge_depth = float(input("Please input the depth of the fridge: "))
lift_volume = (lift_height * lift_width * lift_depth)
fridge_volume = (fridge_height * fridge_width * fridge_depth)
space_left = (lift_volume - fridge_volume)
print("The space left in the lift is {0} metres cubed".format(space_left))
