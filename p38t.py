from dronekit import connect
vehicle=connect('tcp:127.0.0.1:5762',wait_ready=True,timeout=60)