from controller import Robot, Motor
timestep = 8##Entre ma chiquito mejor
import numpy
import math

def run_robot(robot):
    #TODO Constantes
    max_speed = math.pi
    npmatlab = [1,1],[2,1],[2,3],[5,3],[5,2],[6,2],[6,1],[10,1],[10,3]
    nuevaPosicion = npmatlab

    for i in range(len(npmatlab)):
        print(nuevaPosicion[i])
        nuevaPosicion[i][0] = round(nuevaPosicion[i][0] * 0.2 - 0.1,1)
        nuevaPosicion[i][1] = round(nuevaPosicion[i][1] * 0.2 - 0.1,1)
        #print(nuevaPosicion[i][0])
        #   print(nuevaPosicion[i][1])

    
    print(f"Vector posicion {nuevaPosicion}")

    sizeNP = int(numpy.size(nuevaPosicion)/2)
    posActual = 1
    compararGiro = False
    xz = [0,0]
    last_xz = [0.2,0.1]
    flagGiro = True
    moverse = False
    sDerecha = 0.0
    sIzquierda = 0.0
    posQuerida = []
    
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
        print(posActual)

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
                        iMotor.setPosition(izq)##TODO GIRO A LA Izquierda 90°
                        dMotor.setPosition(der)
                        compararGiro = True

                else:

                    if(nuevaPosicion[posActual][0]<xz[0]):##* Si la nueva x es mayor que la actual gira a la izquierda
                        iMotor.setVelocity(max_speed)
                        dMotor.setVelocity(max_speed)
                        izq = valposi+3.14159265359
                        der = valposd-3.14159265359
                        iMotor.setPosition(izq)##TODO GIRO A LA DERECHA 90°
                        dMotor.setPosition(der)
                        compararGiro = True
                    else:##*girar a la derecha
                        iMotor.setVelocity(max_speed)
                        dMotor.setVelocity(max_speed)
                        izq = valposi-3.14159265359
                        der = valposd+3.14159265359
                        iMotor.setPosition(izq)##TODO GIRO A LA Izquierda 90°
                        dMotor.setPosition(der)
                        compararGiro = True
            
            else:###* Sentido de giro si x es igual

                if(last_xz[0]<xz[0]):#* Si enterior x es menor que el actual mira para la pared de la mesa
                    
                    if(nuevaPosicion[posActual][1]<xz[1]):#TODO GIRA A LA IZQUIERDA 90°
                        iMotor.setVelocity(max_speed)
                        dMotor.setVelocity(max_speed)
                        izq = valposi-3.14159265359
                        der = valposd+3.14159265359
                        iMotor.setPosition(izq)##TODO GIRO A LA Izquierda 90°
                        dMotor.setPosition(der)
                        compararGiro = True
                    else:#TODO GIRO A LA DERECHA 90°
                        iMotor.setVelocity(max_speed)
                        dMotor.setVelocity(max_speed)
                        izq = valposi+3.14159265359
                        der = valposd-3.14159265359
                        iMotor.setPosition(izq)##TODO GIRO A LA DERECHA 90°
                        dMotor.setPosition(der)
                        compararGiro = True
                else:
                    if(nuevaPosicion[posActual][1]<xz[1]):##TODO GIRO A LA DERECHA 90°
                        iMotor.setVelocity(max_speed)
                        dMotor.setVelocity(max_speed)
                        izq = valposi+3.14159265359
                        der = valposd-3.14159265359
                        iMotor.setPosition(izq)##TODO GIRO A LA DERECHA 90°
                        dMotor.setPosition(der)
                        compararGiro = True

                    else:
                        iMotor.setVelocity(max_speed)
                        dMotor.setVelocity(max_speed)
                        izq = valposi-3.14159265359
                        der = valposd+3.14159265359
                        iMotor.setPosition(izq)##TODO GIRO A LA Izquierda 90°
                        dMotor.setPosition(der)
                        compararGiro = True

            
            flagGiro = False
            #posActual += 1
            print(posActual)
            ##TODO Termina el codigo para los giros de orientacio   

        if (compararGiro == True and moverse == False):
            if((valposd-der) <=0.001 and (valposi-izq) <=0.001):
                    print("Terminó el giro")
                    compararGiro = False
                    moverse = True
        
        if(moverse == True):
            iMotor.setPosition(float('inf'))
            iMotor.setVelocity(max_speed)
            dMotor.setPosition(float('inf'))
            dMotor.setVelocity(max_speed)

        PosQuerida = nuevaPosicion[1]
        posx = PosQuerida[0]
        posy = PosQuerida[1]

        if(moverse == True and flagGiro == False and abs(posx-xz[0])<0.01 and abs(posy-xz[1])<0.01):
            iMotor.setPosition(float('inf'))
            iMotor.setVelocity(0)
            dMotor.setPosition(float('inf'))
            dMotor.setVelocity(0)
            posActual+=1
            moverse = False
            flagGiro = True
            compararGiro = False
        
        compararGiro = True
        print("----------------------------------------------------------------------------------------")


### *Llamado a la funcion main##
if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)