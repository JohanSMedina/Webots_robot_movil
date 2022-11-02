##Importar librerias y constantes##
from controller import Robot, Motor
import math
pi = 3.14159265359
pi2= pi*2

timestep = 16##Entre ma chiquito mejor

##*Funcion para determinar el angulo del robot   ##
##*respecto al punto siguiente deseado, mediante ##
##*ley de cosenos                                ##

def angleRot(p1,p2,p3):###Anterior, actual y final
    c = math.sqrt(((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2))##p1 a p2
    b = math.sqrt(((p1[0]-p3[0])**2)+((p1[1]-p3[1])**2))##p1 a p3
    a = math.sqrt(((p2[0]-p3[0])**2)+((p2[1]-p3[1])**2))##p2 a p3

    print(f"p1 a p2: {c}\np1 a p3: {b}\np2 a p3: {a}")#!Quitar para cuando ya esté terminado el codigo

    angle = math.acos(((b**2)-(a**2)-(c**2))/(-2*a*c))
    return(angle)

##*Funcion para mover el robot hasta el punto deseado ##

def movToPoint(angle):
    print("Prueba")

##*Funcion main##

def run_robot(robot):
    flagAngle  = True
    xz = [0,0]
    last_xz = [0,0]
    centroRueda = 0.045
    radioRueda = 0.025
    SGiro = 0.0
    angle = 0.0

    nuevaPosicion = [0.5,0.2],[0.2,0.2],[0.2,1.8],[0.5,1.8]

    max_speed = pi2###!Esta cambiarla para que reciba datos por el serial y cuadre con el calculo de matlab

    ##TODO Instancas de los motores##
    iMotor = robot.getDevice('left wheel motor')
    dMotor = robot.getDevice('right wheel motor')
    iMotor.setPosition(float('inf'))
    iMotor.setVelocity(0.0)
    dMotor.setPosition(float('inf'))
    dMotor.setVelocity(0.0)

    ##TODO Creacion instancias del sensor##
    sIzqueirda = robot.getDevice('left wheel sensor')
    sIzqueirda.enable(timestep)
    sDerecha = robot.getDevice('right wheel sensor')
    sDerecha.enable(timestep)
    ps_values = [0,0]
    dist_values = [0,0]

    ##TODO Creacion instancias del GPS##
    gps = robot.getDevice('gps')
    gps.enable(timestep)
    
    ##TODO ##############################
    ##TODO BUCLE INFINITO PARA EL ROBOT##
    ##TODO ##############################
    while robot.step(timestep) != -1:
        SensorD = sDerecha.getValue()
        print(f"Sensor derecha: {SensorD}")#!Quitar para cuando ya esté terminado el codigo
        SensorI =sIzqueirda.getValue()
        print(f"Sensor izquierda: {SensorI}")#!Quitar para cuando ya esté terminado el codigo
        print("-----")#!Quitar para cuando ya esté terminado el codigo

        gps_value = gps.getValues() # * x, z, y de el GPS
        xz[0] = float("{:.8f}".format(gps_value[0]))
        xz[1] = float("{:.8f}".format(gps_value[2]))
        print(f"Posicion en X: {xz[0]}, Z: {xz[1]}")#!Quitar para cuando ya esté terminado el codigo
        
        if(last_xz[0] != 0.0 and last_xz[1] != 0.0 and flagAngle == True):
            flagAngle = False
            iMotor.setVelocity(max_speed*0.2)
            dMotor.setVelocity(max_speed*0.2)
            iMotor.setVelocity(0)
            dMotor.setVelocity(0)
            angle = angleRot(last_xz,xz,nuevaPosicion[1])###Anterior, actual y final
            print(f"radianes: {angle}")
            #!SGiro = SensorI + angle
            iMotor.setVelocity(max_speed)
            dMotor.setVelocity(max_speed)
            iMotor.setPosition(SensorI - angle)
            dMotor.setPosition(SensorI + angle)

        """if(flagAngle==False and xz[0]!=nuevaPosicion[1][0]) and xz[1]!=nuevaPosicion[1][1]:
            iMotor.setPosition(float('inf'))
            iMotor.setVelocity(max_speed)
            dMotor.setPosition(float('inf'))
            dMotor.setVelocity(max_speed)

        dMotor.setVelocity(0)
        iMotor.setVelocity(0)"""
            


        
        
        
        #iMotor.setVelocity(max_speed)
        #dMotor.setVelocity(max_speed)

        last_xz[0] = gps_value[0]##* Actualizar ultima posicion,##
        last_xz[1] = gps_value[2]##* dejar al final del codigo ##



### *Llamado a la funcion main##
if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)