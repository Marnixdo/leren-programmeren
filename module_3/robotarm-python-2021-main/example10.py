from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
nummer = 9
nummer2 = 8
for x in range(5):
    robotArm.grab()
    for x in range(nummer):
        robotArm.moveRight()
    robotArm.drop()
    for x in range(nummer2):
        robotArm.moveLeft()

    nummer -= 2
    nummer2 -= 2







# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()