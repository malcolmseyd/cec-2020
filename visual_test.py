from Drone import Drone
import system
import os, sys, time

import matplotlib.pyplot as plt
import numpy as np  

WAIT = 2

"""def update(title, waittime, opaque):
    system.plot3d(drone.curr_image, size, 111, drone)
    
    plt.title(f"Drone scans the current block (we're displaying it as one above)\n Score: {score}")
    plt.savefig(f"{sys.argv[1].split('/')[-1][:-4]}.png")
    time.sleep(waittime)
   """ 

def main():
    score = 0

    if len(sys.argv) != 2:
        print("Usage: python main.py [PATH/FILENAME.txt]")
        exit(0)

    scram, unscram, size = system.read_file(sys.argv[1])
    
    base_filename = sys.argv[1].split('/')[-1][:-4] 

    drone = Drone(size, scram)
    
    #plt.ion()
    #plt.show()

    system.plot3d(drone.curr_image, size, 111, drone, True)
    plt.title(f"Score: {score}")
    plt.savefig(f"{base_filename}.png")
    time.sleep(WAIT)
    #plt.draw()
    #plt.pause(WAIT)
    #plt.close()

    # pickup block
    block_color = drone.scan(scram)

    system.plot3d(drone.curr_image, size, 111, drone)
    plt.title(f"Drone scans the current block (we're displaying it as one above)\n Score: {score}")
    plt.savefig(f"{base_filename}.png")
    time.sleep(WAIT)
    #plt.draw()
    #plt.pause(WAIT)
    #plt.close()

    drone.pickup(block_color)
    score += 2

    system.plot3d(drone.curr_image, size, 111, drone)
    plt.title(f"Drone picks up block at current position and descends by 1\n Score: {score}")
    plt.savefig(f"{base_filename}.png")
    time.sleep(WAIT)

    drone.moveup(scram)
    score += 1

    system.plot3d(drone.curr_image, size, 111, drone, False)
    plt.title(f"Score: {score}")
    plt.savefig(f"{base_filename}.png")
    time.sleep(WAIT)

    drone.moveup(scram)
    score += 1

    system.plot3d(drone.curr_image, size, 111, drone, False)
    plt.title(f"Score: {score}")
    plt.savefig(f"{base_filename}.png")
    time.sleep(WAIT)

    drone.moveup(scram)
    score += 1

    system.plot3d(drone.curr_image, size, 111, drone, False)
    plt.title(f"Score: {score}")
    plt.savefig(f"{base_filename}.png")
    time.sleep(WAIT)

    drone.dropoff(block_color)
    score += 2

    system.plot3d(drone.curr_image, size, 111, drone, False)
    plt.title(f"Deposits block\nScore: {score}")
    plt.savefig(f"{base_filename}.png")
    time.sleep(WAIT)

    system.plot3d(drone.curr_image, size, 111, drone, True)
    plt.title(f"Deposits block\nScore: {score}")
    plt.savefig(f"{base_filename}.png")
    time.sleep(WAIT)


    #time.sleep(WAIT * 3)
    #plt.draw()
    #plt.pause(WAIT * 3)
    #plt.close()


if __name__ == "__main__":
    main()