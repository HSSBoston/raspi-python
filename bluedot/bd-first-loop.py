from bluedot import BlueDot

bdot = BlueDot()
while True:
    try:
        bdot.wait_for_press()
        print("You just pressed the blue dot on your Android!")
    
    except KeyboardInterrupt:
        break