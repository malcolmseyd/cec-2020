import os

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
            mode = "std"
            idx = 0
            continue
        elif l ==  "unscrambled_image":
            mode = "unstd"
            idx = 0
            continue
        elif l[0:4] == "size":
            size = int(l[5:])
            #print("size = " + str(size))
            continue
        elif l == "":
            # skip blanks
            continue

        #print(l)
        if mode == "std":
            r = l.split("=")
            #print(r)
            s_xyz.append(r[0]) 
            s_rgb.append(r[1][1:-1]) # Remove quotes
            idx += 1
        elif mode == "unstd":
            r = l.split("=")
            #print(r)
            u_xyz.append(r[0]) 
            u_rgb.append(r[1][1:-1]) # Remove quotes
            idx += 1
    #print(s_xyz)
    #print(s_rgb)
    #print(u_xyz)
    #print(u_rgb)
    std = [[ [None for k in range(size)] for j in range(size)] for i in range(size)]
    unstd = [[ [None for k in range(size)] for j in range(size)] for i in range(size)]



    #print(std)

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
        std[x][y][z] = (r, g, b) 

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
        unstd[x][y][z] = (r, g, b)

    return (std, unstd)



def main():
    std, unstd = read_file("./case/easy.txt")
    print("Sorted: " + str(std))
    print("\nUnsorted: " + str(unstd))

if __name__ == "__main__":
    main()