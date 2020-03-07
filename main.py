from Drone import Drone
import system
import os, sys

import matplotlib.pyplot as plt
import numpy as np  

WAIT = 2

def main():

    if len(sys.argv) != 2:
        print("Usage: python main.py [PATH/FILENAME.txt]")
        exit(0)

    scram, unscram, size = system.read_file(sys.argv[1])
    
    base_filename = sys.argv[1].split('/')[-1][:-4] 

    drone = Drone(size, scram)
    
    plt.ion()
    plt.show()

    system.plot3d(drone.curr_image, size, 111)
    #plt.savefig(f"{base_filename}-scrambled.png")
    plt.draw()
    plt.pause(WAIT)
    plt.close()

    # pickup block
    # drone.movetop()
    block_color = drone.scan()

    system.plot3d_highlight(drone.curr_image, size, 111, drone.x, drone.y, drone.z)
    #plt.savefig(f"{base_filename}-scrambled.png")
    plt.draw()
    plt.pause(WAIT)
    plt.close()

    drone.pickup(block_color)

    system.plot3d(drone.curr_image, size, 111)
    #plt.savefig(f"{base_filename}-scrambled.png")
    plt.draw()
    plt.pause(WAIT*3)
    plt.close()


if __name__ == "__main__":
    main()