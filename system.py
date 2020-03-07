import os, sys

# plot3d() inspired by: https://stackoverflow.com/questions/38086972/stacked-3d-bar-chart-with-matplotlib
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np  

def read_file(filename):
    file = open(filename, "r")
    lines = file.readlines()
    mode = ""
    size = 0

    for i in range(0, len(lines)):
        # Remove newlines
        lines[i] = lines[i][:-1]
        if lines[i][0:4] == "size":
            size = int(lines[i][5:]) # anything past the "="
    
    s_xyz = []
    s_rgb = []
    u_xyz = []
    u_rgb = []
    
    #print(lines)
    for l in lines:

        if l == "scrambled_image":
            mode = "scram"
            continue
        elif l ==  "unscrambled_image":
            mode = "unscram"
            continue
        elif l[0:4] == "size":
            size = int(l[5:])
            #print("size = " + str(size))
            continue
        elif l == "":
            # skip blanks
            continue

        #print(l)
        if mode == "scram":
            r = l.split("=")
            #print(r)
            s_xyz.append(r[0]) 
            s_rgb.append(r[1][1:-1]) # Remove quotes
        elif mode == "unscram":
            r = l.split("=")
            #print(r)
            u_xyz.append(r[0]) 
            u_rgb.append(r[1][1:-1]) # Remove quotes
    #print(s_xyz)
    #print(s_rgb)
    #print(u_xyz)
    #print(u_rgb)

    scram = [[ [None for k in range(size)] for j in range(size)] for i in range(size)]
    unscram = [[ [None for k in range(size)] for j in range(size)] for i in range(size)]

    #print(scram)

    for i in range(0, len(s_xyz)):
        coord = s_xyz[i].split(",")

        x = int(coord[0])
        y = int(coord[1])
        z = int(coord[2])

        if s_rgb[i] == "":
            continue

        colors = s_rgb[i].split("_")
        
        r = int(colors[0])
        g = int(colors[1])
        b = int(colors[2])

        #print(coord)
        #print(colors)
        scram[x][y][z] = (r, g, b) 

    for i in range(0, len(u_xyz)):
        coord = u_xyz[i].split(",")

        x = int(coord[0])
        y = int(coord[1])
        z = int(coord[2])

        if u_rgb[i] == "":
            continue

        colors = u_rgb[i].split("_")
        
        r = int(colors[0])
        g = int(colors[1])
        b = int(colors[2])

        #print(coord)
        #print(colors)
        unscram[x][y][z] = (r, g, b)
    # we spent some time tracing, somewhere we flipped, whoops
    return (scram, unscram, size)

def plot3d(map3d, size, scale):

    fig = plt.figure()
    ax = fig.add_subplot(scale, projection = "3d")
    
    ax.set_xlabel("x")
    ax.set_ylabel("y") 
    ax.set_zlabel("z")
    ax.set_xlim3d(0,size)
    ax.set_ylim3d(0,size) 
    ax.set_zlim3d(0,size) 

    alpha_base=1
    
    xpos = [] #x coordinates of each bar
    ypos = [] #y coordinates of each bar
    zpos = [] #z coordinates of each bar
    colors = []
    
    for x in range(0, size):
        for y in range(0, size):
            for z in range(0, size):
                if map3d[x][y][z] != None:
                    xpos.append(x)
                    ypos.append(y)
                    zpos.append(z)
                    
                    r = map3d[x][y][z][0] / 255
                    g = map3d[x][y][z][1] / 255
                    b = map3d[x][y][z][2] / 255

                    colors.append((r, g, b, alpha_base))

    dx = np.ones(1) #width of each bar
    dy = np.ones(1) #depth of each bar
    dz = np.ones(1) #height of each bar

    ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors)


def main():
    #print(sys.argv)
    if len(sys.argv) != 2:
        print("Usage: python main.py [PATH/FILENAME.txt]")
        exit(0)

    scram, unscram, size = read_file(sys.argv[1])
    #print("Sorted: " + str(scram))
    #print("\nUnsorted: " + str(unscram))
    
    base_filename = sys.argv[1].split('/')[-1][:-4] 
    
    plt.ion()
    plt.show()

    plot3d(scram, size, 111)
    #plt.savefig(f"{base_filename}-scrambled.png")
    
    plt.draw()
    plt.pause(1)
    plt.clf()

    plot3d(unscram, size, 111)
    plt.draw()
    plt.pause(1)
    #plt.savefig(f"{base_filename}-unscrambled.png")


if __name__ == "__main__":
    main()