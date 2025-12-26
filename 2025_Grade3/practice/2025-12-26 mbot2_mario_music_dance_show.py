"""
This practice makes an mBot2 robot play a Mario-style melody while moving and changing LED colors.
Music, motion, and lights are synchronized using event-driven Python code on CyberPi.
"""

import cyberpi, mbot2, event, time

@event.is_press("b")
def play_mario():
    # Play note E
    cyberpi.audio.play_music(64, 0.25)  # E
    mbot2.forward(50, 0.2)
    cyberpi.led.show('red yellow blue yellow red')

    cyberpi.audio.play_music(64, 0.25)
    mbot2.backward(50, 0.2)
    cyberpi.led.show('green yellow blue yellow green')

    cyberpi.audio.play_music(64, 0.25)
    mbot2.forward(50, 0.25)
    cyberpi.led.show('red green blue green red')

    # Play C, then E
    cyberpi.audio.play_music(60, 0.15)  # C
    mbot2.drive_power(-60, -60)
    time.sleep(0.15)
    cyberpi.led.show('red yellow green yellow red')

    cyberpi.audio.play_music(64, 0.15)
    mbot2.forward(50, 0.15)
    cyberpi.led.show('red yellow green yellow red')

    # Play high G, then low G
    cyberpi.audio.play_music(67, 0.5)  # G
    mbot2.forward(50, 0.5)
    cyberpi.led.show('red yellow green yellow red')

    cyberpi.audio.play_music(55, 0.5)  # low G
    mbot2.backward(50, 0.5)
    cyberpi.led.show('red red red red red')

    # Continue the melody
    cyberpi.audio.play_music(60, 0.25)  # C
    mbot2.drive_power(60, 60)
    time.sleep(0.25)
    cyberpi.led.show('orange orange orange orange orange')

    cyberpi.audio.play_music(55, 0.25)  # low G
    mbot2.forward(50, 0.25)
    cyberpi.led.show('yellow yellow yellow yellow yellow')

    cyberpi.audio.play_music(52, 0.25)  # low E
    mbot2.forward(50, 0.25)
    cyberpi.led.show('green green green green green')

    cyberpi.audio.play_music(57, 0.25)  # A
    mbot2.forward(50, 0.25)
    cyberpi.led.show('blue blue blue blue blue')

    cyberpi.audio.play_music(59, 0.2)  # B
    mbot2.backward(50, 0.2)
    cyberpi.led.show('purple purple purple purple purple ')

    cyberpi.audio.play_music(58, 0.2)  # Bb
    mbot2.drive_power(60, 60)
    time.sleep(0.2)
    cyberpi.led.show('red orange yellow green blue')

    cyberpi.audio.play_music(57, 0.25)  # A
    mbot2.forward(50, 0.25)
    cyberpi.led.show('red orange yellow green blue')

    cyberpi.audio.play_music(55, 0.5)  # low G
    mbot2.forward(50, 1)
    cyberpi.led.show('red orange yellow green blue')


