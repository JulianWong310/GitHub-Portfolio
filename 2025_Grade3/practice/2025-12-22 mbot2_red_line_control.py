"""
2025/12/22
This project demonstrates a priority-based control system for the mBot2 robot using the quad RGB sensor
1) Black line following using left/right RGB sensors
2) Red color detection with highest priority
3) When red is detected: stop the robot immediately
"""

import mbot2, event, time, mbuild

@event.start
def color_following():
    time.sleep(10)
    while True:
        left_black = (
                mbuild.quad_rgb_sensor.is_color("black", "L1") or
                mbuild.quad_rgb_sensor.is_color("black", "L2")
        )
        right_black = (
                mbuild.quad_rgb_sensor.is_color("black", "R1") or
                mbuild.quad_rgb_sensor.is_color("black", "R2")
        )

        red = (
                mbuild.quad_rgb_sensor.is_color("red", "L1") or
                mbuild.quad_rgb_sensor.is_color("red", "L2") or
                mbuild.quad_rgb_sensor.is_color("red", "R1") or
                mbuild.quad_rgb_sensor.is_color("red", "R2")
        )

        if red:
            mbot2.drive_power(0, 0)
            time.sleep(1)
            mbot2.drive_power(20, -20)
            time.sleep(1)

        if left_black and right_black:
            mbot2.drive_power(20, -20)
        elif left_black:
            mbot2.drive_power(10, -30)
        elif right_black:
            mbot2.drive_power(30, -10)
        else:
            mbot2.drive_power(10, -10)
