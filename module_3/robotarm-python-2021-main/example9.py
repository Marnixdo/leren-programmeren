from RobotArm import RobotArm

robotArm = RobotArm('exercise 9')

robotArm.speed = 3
for b in range(1,5):
    for f in range(b):
        robotArm.grab()
        for c in range(5):
            robotArm.moveRight()
        robotArm.drop()
        for d in range(5):
            robotArm.moveLeft()
    robotArm.moveRight()

robotArm.wait()












# # Jouw python instructies zet je vanaf hier:
# for x in range(5):
#     robotArm.speed = 3
#     robotArm.grab()
#     for x in range(5):
#         robotArm.moveRight()
#     robotArm.drop()
#     for x in range(4):
#         robotArm.moveLeft()
#     robotArm.grab()
# # Na jouw code wachten tot het sluiten van de window:
