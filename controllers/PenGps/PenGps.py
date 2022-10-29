from controller import Robot, Motor
import math
pi = 3.14159265359
pi2= pi*2

def angleRot(x1,z1,x0,z0,nuevaPos):
    global angle

    angle = math.acos((x0*x1)+(z0*z1)/(math.sqrt((x0**2)+(z0**2))*math.sqrt((x1**2)+(z1**2))))



def run_robot(robot):
    global angle

    nuevaPosicion = [0.5,0.2],[0.2,0.2],[0.2,1.8],[0.5,1.8]
    flagAngle  = True

    xyz = [0,0,0]
    last_xz = [0,0]

    ##Optener el tiepo de pasos de la simulacion
    timestep = 128
    max_speed = pi2###Esta cambiarla para que reciba datos por el serial y cuadre con la simulacion

    #-----------------------------------#
    ####Creacion instancias del motor####
    #-----------------------------------# 
    iMotor = robot.getDevice('left wheel motor')
    dMotor = robot.getDevice('right wheel motor')
    
    iMotor.setPosition(float('inf'))
    iMotor.setVelocity(0.0)

    dMotor.setPosition(float('inf'))
    dMotor.setVelocity(0.0)

    #-----------------------------------#
    #### Creacion instancias del GPS ####
    #-----------------------------------# 
    
    gps = robot.getDevice('gps')
    gps.enable(timestep)
    
    #-----------------------------------#
            #### Bucle infinito ####
    #-----------------------------------# 

    while robot.step(timestep) != -1:
        
        gps_value = gps.getValues() ###x, z, y
        
    
        for i in range(3):##Llenado del vector con los valores del angulo, 6 decimales
            #xzy[i] = gps_value[i]
            xyz[i] = float("{:.6f}".format(gps_value[i]))
            
        print(f"Posicion en X: {xyz[0]}, Z: {xyz[2]}")
        

        if (last_xz[0] != 0.0 and last_xz[1] != 0.0 and flagAngle == True):##Determinacion delñ angulo de giro
            flagAngle = False

            angleRot(xyz[0],xyz[2],last_xz[0],last_xz[1],nuevaPosicion[0],nuevaPosicion[1])
            print(f"Angulo de rotacion deg: {angle}")
        
        
        ##Reemplazo de los valores anteriores de X Z
        last_xz[0] = xyz[0]
        last_xz[1] = xyz[2]
        
        iMotor.setVelocity(max_speed*0.25)
        dMotor.setVelocity(max_speed*0.25)

    #-----------------------------------#
        #### Final Bucle infinito ####
    #-----------------------------------# 

if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)