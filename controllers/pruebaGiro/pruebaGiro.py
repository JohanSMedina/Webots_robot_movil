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
    compararGiro = False
    moverse = False

    while robot.step(timestep) != -1:
        valposi = sIzquierda.getValue()
        valposd = sDerecha.getValue()
        print(f"ValPosI: {valposi}, ValPosD: {valposd}")

        if(compararGiro == False and moverse==False):
            print(cont)
            iMotor.setVelocity(max_speed)
            dMotor.setVelocity(max_speed)
            izq = valposi+3.14159265359
            der = valposd-3.14159265359
            iMotor.setPosition(izq)
            dMotor.setPosition(der)
            compararGiro = True

        if (compararGiro == True and moverse == False):
            if((valposd-der) <=0.001 and (valposi-izq) <=0.001):
                    print("Llego a punto")
                    compararGiro = False
                    moverse = True
        
        if(moverse == True):
            iMotor.setPosition(float('inf'))
            iMotor.setVelocity(max_speed)
            dMotor.setPosition(float('inf'))
            dMotor.setVelocity(max_speed)

                    

### *Llamado a la funcion main##
if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)