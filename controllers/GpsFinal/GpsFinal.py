#* Importar librerias y constantes #
from controller import Robot, Motor
import math
import numpy
import time
pi = 3.14159265359
pi2= pi*2
ng = 1.57079632679
#ng = 3.14159265359

timestep = 16##Entre ma chiquito mejor

def run_robot(robot):
    xz = [0,0]
    
    posActual = 0
    last_xz = [0,0]
    flagGiro = True
    nuevaPosicion = [0.5,0.2],[0.2,0.2],[0.2,1.8],[0.5,1.8]
    max_speed = pi2###!Esta cambiarla para que reciba datos por el serial y cuadre con el calculo de matlab

    xz = [0,0]
    last_xz = [0,0]

    ##TODO Instancas de los motores##
    iMotor = robot.getDevice('left wheel motor')
    dMotor = robot.getDevice('right wheel motor')
    iMotor.setPosition(float('inf'))
    iMotor.setVelocity(0.0)
    dMotor.setPosition(float('inf'))
    dMotor.setVelocity(0.0)

    ##TODO Creacion instancias del sensor##
    sIzquierda = robot.getDevice('left wheel sensor')
    sIzquierda.enable(timestep)
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
        
        nuevaPosicion = [0.5,0.2],[0.5,0.3],[0.2,1.8],[0.5,1.8]
        sizeNP = int(numpy.size(nuevaPosicion)/2)

        print(f"Posicion actual: {posActual}")

        gps_value = gps.getValues() # * x, z, y de el GPS
        xz[0] = float("{:.8f}".format(gps_value[0]))
        xz[1] = float("{:.8f}".format(gps_value[2]))
        print(f"Posicion en X: {xz[0]}, Z: {xz[1]}")#!Quitar para cuando ya esté terminado el codigo
        
        #TODO Girar en direccion del nuevo punto
        if((posActual < sizeNP) and (posActual != 0) and (flagGiro == True)):
            SensorD = sDerecha.getValue()
            SensorI = sIzquierda.getValue()
            flagGiro = False
            print("Entra a bucle del giro")
            
            if(xz[0]==nuevaPosicion[posActual][0]):
                print("Entra al if x igual")
                if(xz[1]>nuevaPosicion[posActual][1]):
                    giroI = SensorI - ng
                    giroD = SensorD + ng
                    print("x igual z 1")
                    iMotor.setVelocity(max_speed)
                    dMotor.setVelocity(max_speed)
                    iMotor.setPosition(giroI)
                    dMotor.setPosition(giroD)
                    
                else:
                    giroI = 3.14159265359#SensorI + 
                    giroD = -3.14159265359#SensorD 
                    print("x igual z 2")
                    iMotor.setVelocity(max_speed)
                    dMotor.setVelocity(max_speed)
                    iMotor.setPosition(sIzquierda.getValue() + 3.14159265359)
                    dMotor.setPosition(sDerecha.getValue() -3.14159265359)

            if(xz[1]==nuevaPosicion[posActual][1]):
                print("Entra al if x igual")
                if(xz[0]>nuevaPosicion[posActual][0]):
                    giroI = SensorI - 1.57079632679
                    giroD = SensorD + 1.57079632679
                    print("z igual x 1")
                    iMotor.setVelocity(max_speed)
                    dMotor.setVelocity(max_speed)
                    iMotor.setPosition(giroI)
                    dMotor.setPosition(giroD)
                else:
                    giroI = SensorI + 1.57079632679
                    giroD = SensorD - 1.57079632679
                    print("z igual x 2")
                    iMotor.setVelocity(max_speed)
                    dMotor.setVelocity(max_speed)
                    iMotor.setPosition(giroI)
                    dMotor.setPosition(giroD)

        
        posActual +=1
        print("--------------")


### *Llamado a la funcion main##
if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)