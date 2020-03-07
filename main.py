from Drone import Drone
import system
import os, sys, time

import matplotlib.pyplot as plt
import numpy as np  

WAIT = 1

def main():

    if len(sys.argv) != 2:
        print("Usage: python main.py [PATH/FILENAME.txt]")
        exit(0)

    scram, unscram, size = system.read_file(sys.argv[1])
    
    base_filename = sys.argv[1].split('/')[-1][:-4] 

    drone = Drone(size, scram)
    
    #plt.ion()
    #plt.show()

    system.plot3d(drone.curr_image, size, 111, drone)
    plt.title("Hey you cats")
    plt.savefig(f"{base_filename}.png")
    time.sleep(WAIT)
    #plt.draw()
    #plt.pause(WAIT)
    #plt.close()

    # pickup block
    # drone.movetop()
    block_color = drone.scan()


    time.sleep(WAIT)
    system.plot3d(drone.curr_image, size, 111, drone)
    plt.title("Check this out")
    plt.savefig(f"{base_filename}.png")
    time.sleep(WAIT)
    #plt.draw()
    #plt.pause(WAIT)
    #plt.close()

    drone.pickup(block_color)

    system.plot3d(drone.curr_image, size, 111, drone)
    plt.title("BOOM!")
    plt.savefig(f"{base_filename}.png")
    #time.sleep(WAIT * 3)
    #plt.draw()
    #plt.pause(WAIT * 3)
    #plt.close()


if __name__ == "__main__":
    main()