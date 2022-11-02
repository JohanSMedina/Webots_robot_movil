from controller import Robot, Motor
import math
pi = 3.14159265359
print(pi)


if __name__ == "__main__":

    robot = Robot()
    
    timestep = 64
    max_speed = 6.28###En radianes
    #-----------------------------------#
    ###Creacion instancias del motor###
    #-----------------------------------#    
    
    ###Declarar objetos
    mIzquierda = robot.getDevice('left wheel motor')
    mDerecha = robot.getDevice('right wheel motor')
    
    ###Rotaciones infinitas y velocidad 0
    mIzquierda.setPosition(float('inf'))
    mIzquierda.setVelocity(0.0)
    
    mDerecha.setPosition(float('inf'))
    mDerecha.setVelocity(0.0)
    
    #-----------------------------------#
    ###Creacion instancias del sensor###
    #-----------------------------------#
    
    sIzqueirda = robot.getPositionSensor('left wheel sensor')
    sIzqueirda.enable(timestep)
    
    sDerecha = robot.getPositionSensor('right wheel sensor')
    sDerecha.enable(timestep)

    ps_values = [0,0]
    dist_values = [0,0]
    
    #-----------------------------------#
    ###Variables para el movimiento###
    #-----------------------------------#
    
    wheel_radius = 0.025
    distance_between_wheels = 0.09
    wheel_cirum = 2 * pi * wheel_radius
    encoder_unit = wheel_cirum/(2*pi)
    
    #-----------------------------------#
            ###Posicion robot###
    #-----------------------------------#
    
    robot_pose = [0,0,0]#x,y,theta
    last_ps_value = [0,0]
    
    #-----------------------------------#
            ###Bucle infinito###
    #-----------------------------------#

    while robot.step(timestep) != -1:
    
        ps_values[0] = sDerecha.getValue()
        ps_values[1] = sIzqueirda.getValue()
        print("------------------------------------------------------------")
        print(f"Posicion derecha {ps_values[0]} y Posicion izquierda {ps_values[1]}")
        
        for ind in range(2):###Terminar el for porque si no peta###
            diff = ps_values[ind] - last_ps_value[ind]
            if diff<0.001:
                diff = 0
                ps_values[ind] = last_ps_value[ind]
            dist_values[ind] = diff * encoder_unit

        #Comptar velocidad linear y anggular
        v = (dist_values[0]+dist_values[1])/2.0
        w = (dist_values[0]+dist_values[1])/distance_between_wheels
        
        dt = 1
        robot_pose[2] += (w * dt)

        vx = v*math.cos(robot_pose[2])
        vy = v*math.sin(robot_pose[2])

        robot_pose[0] += (vx * dt)
        robot_pose[1] += (vy * dt)

        print(f"Posicion del robot {robot_pose}")

        if (ps_values[0] < 8.44 ):
            mIzquierda.setVelocity(max_speed)
            mDerecha.setVelocity(max_speed)
        else:
            mIzquierda.setVelocity(0.0)
            mDerecha.setVelocity(0.0)

        for ind in range(2):
            last_ps_value[ind] = ps_values[ind]
            
        #pass