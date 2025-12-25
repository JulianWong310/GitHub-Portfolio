"""
2025-12-24
mBot2 Line Following with Color Control 🤖🎨

Project Overview
This project controls an mBot2 robot to follow a black line using a Quad RGB sensor.
In addition to basic line following, the robot reacts differently when it detects specific colors on the track.

Black Line Following Logic
The robot follows a black line using left and right RGB sensors:
- Both sensors detect black → move forward
- Left sensor detects black → turn left
- Right sensor detects black → turn right
- No black detected → slow forward movement

Color-Based Behaviors
- Red : Stop for 1 second, then continue forward
- Yellow : Move slower for a short time
- Green : Turn around, then continue forward
- Blue : Move faster for a short time
"""

import mbot2, event, time, mbuild

@event.start
def color_following():
    # Wait before start
    time.sleep(10)

    while True:
       # Check black line
        left_black = (
                mbuild.quad_rgb_sensor.is_color("black", "L1") or
                mbuild.quad_rgb_sensor.is_color("black", "L2")
        )
        right_black = (
                mbuild.quad_rgb_sensor.is_color("black", "R1") or
                mbuild.quad_rgb_sensor.is_color("black", "R2")
        )

       # Check colors
        yellow = (
                mbuild.quad_rgb_sensor.is_color("yellow", "L1") or
                mbuild.quad_rgb_sensor.is_color("yellow", "L2") or
                mbuild.quad_rgb_sensor.is_color("yellow", "R1") or
                mbuild.quad_rgb_sensor.is_color("yellow", "R2")
        )

        green = (
                mbuild.quad_rgb_sensor.is_color("green", "L1") or
                mbuild.quad_rgb_sensor.is_color("green", "L2") or
                mbuild.quad_rgb_sensor.is_color("green", "R1") or
                mbuild.quad_rgb_sensor.is_color("green", "R2")
        )

        blue = (
                mbuild.quad_rgb_sensor.is_color("blue", "L1") or
                mbuild.quad_rgb_sensor.is_color("blue", "L2") or
                mbuild.quad_rgb_sensor.is_color("blue", "R1") or
                mbuild.quad_rgb_sensor.is_color("blue", "R2")
        )

        red = (
                mbuild.quad_rgb_sensor.is_color("red", "L1") or
                mbuild.quad_rgb_sensor.is_color("red", "L2") or
                mbuild.quad_rgb_sensor.is_color("red", "R1") or
                mbuild.quad_rgb_sensor.is_color("red", "R2")
        )

       # Red: stop, then move forward
        if red:
            mbot2.drive_power(0, 0)
            time.sleep(1)
            mbot2.drive_power(20, -20)
            time.sleep(0.5)

       # Yellow: move slower
        elif yellow:
            mbot2.drive_power(10, -10)
            time.sleep(1)

       # Green: turn around
        elif green:
            mbot2.drive_power(60, 60)
            time.sleep(0.83)
            mbot2.drive_power(20, -20)
            time.sleep(0.5)

       # Blue: move faster
        elif blue:
            mbot2.drive_power(60, -60)
            time.sleep(0.1)

       # Black line following
       # Both sides see black, go straight
        else:
            if left_black and right_black:
                mbot2.drive_power(20, -20)

           # Left side sees black, turn left
            elif left_black:
                mbot2.drive_power(10, -30)

            # Right side sees black, turn right
            elif right_black:
                mbot2.drive_power(30, -10)

            # Lost the line, move slowly to search
            else:
                mbot2.drive_power(10, -10)
