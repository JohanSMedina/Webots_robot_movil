from controller import Robot, Motor
timestep = 8##Entre ma chiquito mejor
import numpy
import math

def run_robot(robot):
    #TODO Constantes
    max_speed = math.pi
    nuevaPosicion = [0.2,0.2],[0.1,0.2]
    sizeNP = int(numpy.size(nuevaPosicion)/2)
    posActual = 1
    compararGiro = False
    xz = [0,0]
    last_xz = [0.2,0.1]
    flagGiro = True
    moverse = False
    sDerecha = 0.0
    sIzquierda = 0.0
    
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

    while robot.step(timestep) != -1:
        gps_value = gps.getValues() # * x, z, y de el GPS
        xz[0] = float("{:.8f}".format(gps_value[0]))
        xz[1] = float("{:.8f}".format(gps_value[2]))
        print(f"Posicion en X: {xz[0]}, Z: {xz[1]}")#!Quitar para cuando ya esté terminado el codigo
        valposi = sIzquierda.getValue()
        valposd = sDerecha.getValue()

        if(posActual < sizeNP and flagGiro == True and posActual != 0):

            if(xz[1]==nuevaPosicion[posActual][1]):###* Sentido de giro si z es igual
                print(f"XZ actual {xz}, posicion siguente {nuevaPosicion[posActual]}")

                if(last_xz[1]<xz[1]):##* Si enterior z es menor que el actual mira para abajo en la simulacion

                    if(nuevaPosicion[posActual][0]<xz[0]):##* Girar a la dereccha x nueva menor que la actual
                        #! ESTE ES EL CASO QUE ESTAMS MIRANDO
                        iMotor.setVelocity(max_speed)
                        dMotor.setVelocity(max_speed)
                        izq = valposi+3.14159265359
                        der = valposd-3.14159265359
                        iMotor.setPosition(izq)##TODO GIRO A LA DERECHA 90°
                        dMotor.setPosition(der)
                        compararGiro = True

                    else:##* girar a la izquierda ##TODO GIRO A LA IZQUIERDA 90°
                        iMotor.setVelocity(max_speed)
                        dMotor.setVelocity(max_speed)
                        izq = valposi-3.14159265359
                        der = valposd+3.14159265359
                        iMotor.setPosition(izq)##TODO GIRO A LA Izquiera 90°
                        dMotor.setPosition(der)
                        compararGiro = True

                else:

                    if(nuevaPosicion[posActual][0]<xz[0]):##* Si la nueva x es mayor que la actual gira a la izquierda
                        """iMotor.setVelocity(max_speed)
                        dMotor.setVelocity(max_speed)
                        iMotor.setPosition(sIzquierda.getValue()+3.14159265359)##TODO GIRO A LA DERECHA 90°
                        dMotor.setPosition(sDerecha.getValue()-3.14159265359)
                        sIzquierda = sIzquierda.getValue()
                        sDerecha = sDerecha.getValue()"""
                    else:##*girar a la derecha
                        """iMotor.setVelocity(max_speed)
                        dMotor.setVelocity(max_speed)
                        iMotor.setPosition(sIzquierda.getValue()+3.14159265359)##TODO GIRO A LA IZQUIERDA 90°
                        dMotor.setPosition(sDerecha.getValue()-3.14159265359)
                        sIzquierda = sIzquierda.getValue()
                        sDerecha = sDerecha.getValue()"""
            
            else:###* Sentido de giro si x es igual

                if(last_xz[0]<xz[0]):#* Si enterior x es menor que el actual mira para la pared de la mesa
                    
                    if(nuevaPosicion[posActual][1]<xz[1]):#TODO GIRA A LA IZQUIERDA 90°
                        """iMotor.setVelocity(max_speed)
                        dMotor.setVelocity(max_speed)
                        iMotor.setPosition(sIzquierda.getValue()-3.14159265359)##TODO GIRO A LA IZQUIERDA 90°
                        dMotor.setPosition(sDerecha.getValue()+3.14159265359)
                        sIzquierda = sIzquierda.getValue()
                        sDerecha = sDerecha.getValue()"""
                    else:#TODO GIRO A LA DERECHA 90°
                       """iMotor.setVelocity(max_speed)
                        dMotor.setVelocity(max_speed)
                        iMotor.setPosition(sIzquierda.getValue()+3.14159265359)##TODO GIRO A LA DERECHA 90°
                        dMotor.setPosition(sDerecha.getValue()-3.14159265359)
                        sIzquierda = sIzquierda.getValue()
                        sDerecha = sDerecha.getValue()"""
                else:
                    if(nuevaPosicion[posActual][1]<xz[1]):##TODO GIRO A LA DERECHA 90°
                        """iMotor.setVelocity(max_speed)
                        dMotor.setVelocity(max_speed)
                        iMotor.setPosition(sIzquierda.getValue()+3.14159265359)##TODO GIRO A LA DERECHA 90°
                        dMotor.setPosition(sDerecha.getValue()-3.14159265359)
                        sIzquierda = sIzquierda.getValue()
                        sDerecha = sDerecha.getValue()"""

                    else:
                        """iMotor.setVelocity(max_speed)
                        dMotor.setVelocity(max_speed)
                        iMotor.setPosition(sIzquierda.getValue()-3.14159265359)##TODO GIRO A LA IZQUIERDA 90°
                        dMotor.setPosition(sDerecha.getValue()+3.14159265359)
                        sIzquierda = sIzquierda.getValue()
                        sDerecha = sDerecha.getValue()"""

            #print(posActual)
            #print(f"nuevaPosicion[posActual][0]: {nuevaPosicion[posActual][0]}, xz[0]: {xz[0]}, nuevaPosicion[posActual][1]: {nuevaPosicion[posActual][1]}, xz[1]: {xz[1]}")
            
            flagGiro = False
            posActual += 1
            print(posActual)
            ##TODO Termina el codigo para los giros de orientacio
        
        """if(compararGiro == True):
            sIzquierda = sIzquierda.getValue()
            sDerecha = sDerecha.getValue()
            
            #saIzquierda = sIzquierda.getValue()
            #saDerecha = sDerecha.getValue()
            print(f"saDerecha: {sa  Derecha}, sDerecha: {sDerecha}\nsIzquierda: {sIzquierda}, saIzquierda: {saIzquierda}")
            
            if(sIzquierda == sIzquierda and sDerecha == sDerecha):
                print("ya giró todo")"""

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
        
        
        compararGiro = True
        print("----------------------------------------------------------------------------------------")


### *Llamado a la funcion main##
if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)