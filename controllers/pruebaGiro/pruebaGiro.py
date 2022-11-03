from controller import Robot, Motor
timestep = 16##Entre ma chiquito mejor

def run_robot(robot):
    ##TODO Instancas de los motores##
    iMotor = robot.getDevice('left wheel motor')
    dMotor = robot.getDevice('right wheel motor')
    iMotor.setPosition(float('inf'))
    iMotor.setVelocity(0.0)
    dMotor.setPosition(float('inf'))
    dMotor.setVelocity(0.0)
    max_speed = 3.14159265359

    ##TODO Creacion instancias del sensor##
    sIzquierda = robot.getDevice('left wheel sensor')
    sIzquierda.enable(timestep)
    sDerecha = robot.getDevice('right wheel sensor')
    sDerecha.enable(timestep)
    ps_values = [0,0]
    dist_values = [0,0]
    cont = 0 

    while robot.step(timestep) != -1:
        iMotor.setVelocity(max_speed)
        dMotor.setVelocity(max_speed)

        if(cont == 0):
            print(cont)
            iMotor.setPosition(sIzquierda.getValue()+3.14159265359)
            dMotor.setPosition(sDerecha.getValue()-3.14159265359)
            cont = 1

### *Llamado a la funcion main##
if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)