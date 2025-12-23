"""
2025/12/23
Continued color detection behaviors (from yesterday’s practice):
Yellow: Slow down for 1 second
Blue: Speed up briefly
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
        yellow = (
                mbuild.quad_rgb_sensor.is_color("yellow", "L1") or
                mbuild.quad_rgb_sensor.is_color("yellow", "L2") or
                mbuild.quad_rgb_sensor.is_color("yellow", "R1") or
                mbuild.quad_rgb_sensor.is_color("yellow", "R2")
        )
        blue = (
                mbuild.quad_rgb_sensor.is_color("blue", "L1") or
                mbuild.quad_rgb_sensor.is_color("blue", "L2") or
                mbuild.quad_rgb_sensor.is_color("blue", "R1") or
                mbuild.quad_rgb_sensor.is_color("blue", "R2")
        )

        if red:
            mbot2.drive_power(0, 0)
            time.sleep(1)
            mbot2.drive_power(20, -20)
            time.sleep(0.5)

        if yellow:
            mbot2.drive_power(10, -10)
            time.sleep(1)

        if blue:
            mbot2.drive_power(60, -60)
            time.sleep(0.3)

        if left_black and right_black:
            mbot2.drive_power(20, -20)
        elif left_black:
            mbot2.drive_power(10, -30)
        elif right_black:
            mbot2.drive_power(30, -10)
        else:
            mbot2.drive_power(0, 0)