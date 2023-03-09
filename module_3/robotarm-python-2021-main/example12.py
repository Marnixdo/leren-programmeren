from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')
# Jouw python instructies zet je vanaf hier:
robotArm.speed = 3
for i in range(9,0,-1):
    robotArm.grab()
    color = robotArm.scan()
    if color != "red":
        robotArm.drop()
        robotArm.moveRight()
    else:
        for c in range(i):
            robotArm.moveRight()
        robotArm.drop()
        for c in range(i-1):
            robotArm.moveLeft()


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
#robotArm.speed = 3
# for x in range(8):
#     robotArm.moveRight()
# for x in range(9):
#     robotArm.grab()
#     scan = robotArm.scan()
#     if scan == "red":
#         for x in range(8):
#             robotArm.moveRight()