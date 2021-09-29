import math
choices = ["Cube", "Cuboid", "Cylinder"]
choice = int(input("Calculate:\n1.Cube\n2.Cuboid\n3.Cylinder\nYour choice:"))
print("Your choice is ", choices[choice-1])
if choice == 1 :
    side = int(input("Side: "))
    print("Cube Volume:",side**3,"\nCube Surface Area:", 6*side**2)
elif choice == 2:
    l = int(input("Length: "))
    w= int(input("Width: "))
    h = int(input("Height: "))
    print("Cuboid Volume:", l*w*h , "\nCuboid Surface Area:", 2*l*w + 2*w*h + 2*h*l)
elif choice == 3:
    r = int(input("Radius: "))
    h = int(input("Height: "))
    print("Cylinder Volume:",math.pi*h*r**2 , "\nCylinder Surface Area:", 2*math.pi*r*h + 2*math.pi*r**2 )