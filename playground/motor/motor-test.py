import explorerhat, time

explorerhat.motor.one.forwards(50)
time.sleep(1)
explorerhat.motor.one.stop()

time.sleep(3)

explorerhat.motor.one.backwards(50)
time.sleep(1)
explorerhat.motor.one.stop()



