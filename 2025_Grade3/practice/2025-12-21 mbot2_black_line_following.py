"""
2025/12/21
mBot2 Black Line Following (Basic)
This practice implements a basic black line-following behavior for mBot2 using the Quad RGB Line Sensor.
The robot continuously checks the left and right sensors to detect a black line and adjusts its movement accordingly.
Behavior
- Both sensors detect black → move forward
- Left sensor detects black → turn left
- Right sensor detects black → turn right
- No black detected → stop
"""

import mbot2
import mbuild
import event
import time

@event.start
def follow_line():
    time.sleep(5)

    while True:
        left_black = (
        mbuild.quad_rgb_sensor.is_color("black", "L1", 1) or
        mbuild.quad_rgb_sensor.is_color("black", "L2", 1)
        )
        right_black = (
        mbuild.quad_rgb_sensor.is_color("black", "R1", 1) or
        mbuild.quad_rgb_sensor.is_color("black", "R2", 1)
        )


        if left_black and right_black: # go forward
            mbot2.drive_power(20, -20)

        elif left_black: # need turn left
            mbot2.drive_power(10,-30)
            time.sleep(0.01)

        elif right_black: # need turn right
            mbot2.drive_power(30, -10)
            time.sleep(0.01)
        else:
            mbot2.drive_power(0, 0)
