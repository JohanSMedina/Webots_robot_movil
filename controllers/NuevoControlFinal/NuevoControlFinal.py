from controller import Robot, Motor
timestep = 8##Entre ma chiquito mejor
import numpy
import math

def run_robot(robot):
    #TODO Constantes
    max_speed = math.pi
    npmatlab = [1,1],[1,2],[3,2],[3,5],[2,5],[2,6],[1,6],[1,10],[3,10]
    #Vector posicion ([0.5, 0.1], [0.5, 0.3], [0.1, 0.3], [0.1, 0.9], [0.3, 0.9], [0.3, 1.1], [0.5, 1.1], [0.5, 1.9], [0.1, 1.9])
    nuevaPosicion = npmatlab

    for i in range(len(npmatlab)):##TODO for para cambiar al sistema de coordenadas de la simulacion
        nuevaPosicion[i][0] = round(0.6 -(nuevaPosicion[i][0] * 0.2 - 0.1),1)
        nuevaPosicion[i][1] = round(nuevaPosicion[i][1] * 0.2 - 0.1,1)

    print(f"Vector posicion {nuevaPosicion}")#!Mostrar el vector corregido

    ##TODO Constantes declaradas##
    #!Comparadores
    compararGiro = False
    flagGiro = True #! Esta es para saber si debe o no girar
    moverse = False
    #!Vectores
    last_xz = [0.2,0.1]
    xz = [0,0]
    comxz = [0,0]
    posQuerida = []
    #!Constantes
    posActual = 0
    sizeNP = int(numpy.size(nuevaPosicion)/2)
    prueba = 20
    PropRad = 5.654866776/1.89899
    #PropRad = 1.745329252*2
    #PropRad = 2.827433388*1.055058

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

    #TODO Bucle infinito, corre el codigo aqui
    while robot.step(timestep) != -1:

        gps_value = gps.getValues() # * x, z, y de el GPS
        xz[0] = float("{:.8f}".format(gps_value[0]))
        xz[1] = float("{:.8f}".format(gps_value[2]))

        if(posActual < 8):
            comxz = nuevaPosicion[posActual]

        valposi = sIzquierda.getValue()#*Valores de la posicion de los sensores
        valposd = sDerecha.getValue()

        if(posActual == 0):

            #print(f"Movimiento en Z, XZ actual {xz}, posicion siguente {nuevaPosicion[posActual+1]}")
            izq = valposi
            der = valposd
            compararGiro = True
            #posActual += 1

        if(posActual < sizeNP and flagGiro == True and posActual != 0  and  posActual != 8):

            if( comxz[1] == nuevaPosicion[posActual+1][1] ):###* Sentido de giro si z es igual
                print(f"Movimiento en Z, XZ actual {xz}, posicion siguente {nuevaPosicion[posActual+1]}")

                if(last_xz[1]<comxz[1]):##* Si anterior z es menor que el actual mira para abajo en la simulacion

                    if(nuevaPosicion[posActual+1][0]<comxz[0]):##* Girar a la dereccha x nueva menor que la actual
                        iMotor.setVelocity(max_speed)
                        dMotor.setVelocity(max_speed)
                        izq = valposi+PropRad
                        der = valposd-PropRad
                        #izq = valposi+3.14159265359
                        #der = valposd-3.14159265359
                        if (posActual == 7):
                            izq -= 0.125
                            der += 0.125
                        iMotor.setPosition(izq)##TODO GIRO A LA DERECHA 90??
                        dMotor.setPosition(der)
                        compararGiro = True
                        print("C1")

                    else:##* girar a la izquierda ##TODO GIRO A LA IZQUIERDA 90??
                        iMotor.setVelocity(max_speed)
                        dMotor.setVelocity(max_speed)
                        izq = valposi-PropRad
                        der = valposd+PropRad
                        if (posActual == 3):
                            izq -= 0.14
                            der += 0.14

                        if (posActual == 5):
                            izq += 0.08
                            der -= 0.08    
                        
                        iMotor.setPosition(izq)##TODO GIRO A LA Izquierda 90??
                        dMotor.setPosition(der)
                        compararGiro = True
                        print("C2")
                    
                else:##* Si anterior z es mayor que el actual mira para arriba en la simulacion

                    if(nuevaPosicion[posActual+1][0]<comxz[0]):##* Si la nueva x es mayor que la actual gira a la izquierda
                        iMotor.setVelocity(max_speed)
                        dMotor.setVelocity(max_speed)
                        izq = valposi+PropRad
                        der = valposd-PropRad
                        iMotor.setPosition(izq)##TODO GIRO A LA DERECHA 90??
                        dMotor.setPosition(der)
                        compararGiro = True
                        print("C3")

                    else:##*girar a la derecha
                        iMotor.setVelocity(max_speed)
                        dMotor.setVelocity(max_speed)
                        izq = valposi-PropRad
                        der = valposd+PropRad
                        iMotor.setPosition(izq)##TODO GIRO A LA Izquierda 90??
                        dMotor.setPosition(der)
                        compararGiro = True
                        print("C4")
                         
            else:###* Sentido de giro si x es igual

                if(last_xz[0]<comxz[0]):#* Si enterior x es menor que el actual mira para la pared de la mesa
                    
                    if(nuevaPosicion[posActual+1][1]<comxz[1]):#TODO GIRA A LA IZQUIERDA 90??
                        iMotor.setVelocity(max_speed)
                        dMotor.setVelocity(max_speed)
                        izq = valposi-PropRad
                        der = valposd+PropRad
                        iMotor.setPosition(izq)##TODO GIRO A LA Izquierda 90??
                        dMotor.setPosition(der)
                        compararGiro = True
                        print("C5")

                    else:#TODO GIRO A LA DERECHA 90??
                        iMotor.setVelocity(max_speed)
                        dMotor.setVelocity(max_speed)
                        izq = valposi+PropRad
                        der = valposd-PropRad

                        if(posActual == 4):
                            izq -= 0.09
                            der += 0.09

                        if(posActual == 6):
                            izq += 0.16
                            der -= 0.16

                        iMotor.setPosition(izq)##TODO GIRO A LA DERECHA 90??
                        dMotor.setPosition(der)
                        compararGiro = True
                        print("C6")
                else:
                    if(nuevaPosicion[posActual+1][1]<comxz[1]):##TODO GIRO A LA DERECHA 90??
                        iMotor.setVelocity(max_speed)
                        dMotor.setVelocity(max_speed)
                        izq = valposi+PropRad
                        der = valposd-PropRad
                        iMotor.setPosition(izq)##TODO GIRO A LA DERECHA 90??
                        dMotor.setPosition(der)
                        compararGiro = True
                        print("C7")

                    else:
                        iMotor.setVelocity(max_speed)
                        dMotor.setVelocity(max_speed)
                        izq = valposi-PropRad-0.085
                        der = valposd+PropRad+0.085
                        if(posActual == 1):
                            izq -= 0.085
                            der += 0.085

                        iMotor.setPosition(izq)##TODO GIRO A LA Izquierda 90??
                        dMotor.setPosition(der)
                        compararGiro = True
                        print("C8")

            flagGiro = False
        
        #Todo Verificar si ya gir?? como es
        if (compararGiro == True and moverse == False):

            if((valposd - der) <= 0.001 and (valposi - izq) <= 0.001):

                    print("------")
                    print("Termin?? el giro")
                    print("------")
                    #print(prueba)
                    if(prueba == 0):
                        prueba = 20
                        compararGiro = False
                        moverse = True
                    else:
                        prueba -= 1

        #TODO Si ya gir?? para orientarse se puede mover
        if(moverse == True and compararGiro == False):

            iMotor.setPosition(float('inf'))
            iMotor.setVelocity(max_speed)
            dMotor.setPosition(float('inf'))
            dMotor.setVelocity(max_speed)

        #TODO Verificar si lleg?? a la posision querida y detenerse de haber llegado
        #print(f"np: {nuevaPosicion[posActual+1]}")
        if(posActual < 8):
            PosQuerida = nuevaPosicion[posActual+1]
            diffPosQueridaX = abs(PosQuerida[0] - xz[0])
            
            diffPosQueridaY = abs(PosQuerida[1] - xz[1])
        
        
        """if(posActual == 7):
            print(f"diffPosQueridaX: {diffPosQueridaX}")
            print(f"diffPosQueridaY: {diffPosQueridaY}")
            print("----------------------")"""

        if( diffPosQueridaX < 0.001 and diffPosQueridaY < 0.001 and posActual < 8):

            print("------")
            print("Lleg?? al punto")
            print("------")
            iMotor.setPosition(float('inf'))
            iMotor.setVelocity(0)
            dMotor.setPosition(float('inf'))
            dMotor.setVelocity(0)
            last_xz = nuevaPosicion[posActual]
            print(f"Actualizacion de lastXZ: {last_xz}")
            moverse = False
            posActual +=1
            #print(f"Actualizacion de XZ: {nuevaPosicion[posActual]}")
            flagGiro = True
            print(f"PosActual: {posActual}")



        #print("------")

### *Llamado a la funcion main##
if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)