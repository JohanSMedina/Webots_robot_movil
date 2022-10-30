from controller import Robot, Motor
import math
pi = 3.14159265359
pi2= pi*2

def angleRot(p1,p2,p3):###Anterior, actual y final
    c = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))##p1 a p2
    b = math.sqrt(((p1[0]-p3[0])**2)+((p1[1]-p3[1])**2))##p1 a p3
    a = math.sqrt(((p2[0]-p3[0])**2)+((p2[1]-p3[1])**2))##p2 a p3

    print(f"p1 a p2: {c}\np1 a p3: {b}\np2 a p3: {a}")

    angle = math.acos(((b**2)-(a**2)-(c**2))/(-2*a*c))
    return(angle)

def movToPoint(angle):
    print("Prueba")
    


def run_robot(robot):
    #global angle
    #global iMotor
    #global dMotor

    nuevaPosicion = [0.5,0.2],[0.2,0.2],[0.2,1.8],[0.5,1.8]
    flagAngle  = True

    xyz = [0,0,0]
    xz = [0,0]
    last_xz = [0,0]
    pm = True
    centroRueda = 0.045
    radioRueda = 0.0

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
        
        xz[0]=xyz[0]
        xz[1]=xyz[2]

        print(f"Posicion en X: {xz[0]}, Z: {xz[1]}")
        
        if (last_xz[0] != 0.0 and last_xz[1] != 0.0 and flagAngle == True):##Determinacion del angulo de giro
            flagAngle = False
            angle = angleRot(last_xz,xz,nuevaPosicion[1])###Anterior, actual y final
            """pasos = 0
            while (pasos !=20) :
                pasos += 1
                print(f"Paso: {pasos}")
                iMotor.setVelocity(max_speed)
                dMotor.setVelocity(-max_speed)"""
            









        ##Reemplazo de los valores anteriores de X Z
        last_xz[0] = xyz[0]
        last_xz[1] = xyz[2]
        
        if(pm==True):
            iMotor.setVelocity(max_speed*0.2)
            dMotor.setVelocity(max_speed*0.2)
            pm = False
        else:
            iMotor.setVelocity(-max_speed)
            dMotor.setVelocity(max_speed)

    #-----------------------------------#
        #### Final Bucle infinito ####
    #-----------------------------------# 

if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)