from controller import Robot, Motor
robot = Robot()


timestep = int(robot.getBasicTimeStep())


mIzquierda = robot.getDevice('left wheel motor')
mDerecha = robot.getDevice('right wheel motor')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    mIzquierda.setPosition(float("inf"))
    mIzquierda.setVelocity(2)#1 es 0.0333333m/s mas o menos
    mDerecha.setPosition(float("inf"))
    mDerecha.setVelocity(2)
    pass

# Enter here exit cleanup code.
