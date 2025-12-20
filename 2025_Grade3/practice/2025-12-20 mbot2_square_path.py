"""
2025/12/20
This is my first autonomous robot program using mBot2 and Python.
The robot drives in a square path by:
- Moving forward for a fixed time
- Turning approximately 90 degrees
- Repeating the process 4 times
"""
import mbot2
import event
import time

@event.start
def square():
    time.sleep(10)
    speed = 30
    move_time = 3
    turn_speed = 30
    turn_time = 0.6

    for i in range(4):
        mbot2.drive_power(speed, -speed)
        time.sleep(move_time)
        mbot2.drive_power(turn_speed, turn_speed)
        time.sleep(turn_time)

    mbot2.drive_power(0, 0)